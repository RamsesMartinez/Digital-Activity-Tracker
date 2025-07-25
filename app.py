"""
Digital Activity Tracker - Flask Application

A real-time activity tracking application that monitors active applications
and browser URLs to provide insights into digital productivity patterns.

Author: Ramthedev
License: MIT
"""

import csv
import json
import os
import subprocess
import threading
import time
from collections import defaultdict
from datetime import datetime, timedelta

from flask import Flask, jsonify, render_template, request

# Global Configuration
LOG_FILE = 'activity_log.csv'
CONFIG_FILE = 'config.json'
CHECK_INTERVAL = 2  # Seconds (faster for real-time tracking)
DEFAULT_PORT = 5000
DEFAULT_HOST = '127.0.0.1'

# Flask application instance
app = Flask(__name__)

# Tracker state management
tracker_state = {
    'is_paused': False,
    'lock': threading.Lock()
}

# AppleScript templates for macOS system interaction
APP_SCRIPT = '''tell application "System Events" to get name of first process whose frontmost is true'''

URL_SCRIPT = '''
if application "{app_name}" is running then
    tell application "{app_name}"
        if its (count of windows) > 0 then
            try
                get URL of active tab of first window
            on error
                try
                    get URL of active tab of front window
                on error
                    "No URL found"
                end try
            end try
        else
            "No windows open"
        end if
    end tell
else
    "App not running"
end if
'''

# Supported browsers for URL tracking
SUPPORTED_BROWSERS = ["Brave Browser", "Google Chrome", "Safari", "Firefox", "Arc"]


def run_applescript(script: str) -> str | None:
    """
    Execute AppleScript and return the result.
    
    Args:
        script: AppleScript code to execute
        
    Returns:
        Script output as string or None if execution fails
    """
    try:
        result = subprocess.run(
            ['osascript', '-e', script], 
            capture_output=True, 
            text=True, 
            check=False
        )
        return result.stdout.strip() if result.returncode == 0 else None
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def get_active_window_info() -> tuple[str, str]:
    """
    Get information about the currently active window.
    
    Returns:
        Tuple of (app_name, window_title/url)
    """
    app_name = run_applescript(APP_SCRIPT)
    window_title = ""
    
    if app_name in SUPPORTED_BROWSERS:
        url = run_applescript(URL_SCRIPT.format(app_name=app_name))
        window_title = url if url and "No URL found" not in url else app_name
    elif app_name:
        window_title = app_name
    else:
        app_name, window_title = "Unknown", "Unknown"
    
    return app_name, window_title


def load_config() -> dict:
    """
    Load application configuration from JSON file.
    
    Returns:
        Configuration dictionary with app mappings and browser keywords
    """
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"app_mappings": {}, "browser_keywords": {}}


def get_category(app_name: str, window_title: str, config: dict) -> str:
    """
    Determine the category for an application and window title.
    
    Args:
        app_name: Name of the active application
        window_title: Window title or URL
        config: Configuration dictionary
        
    Returns:
        Category string for the activity
    """
    category = config['app_mappings'].get(app_name)
    
    if category == "Navegador":
        for keyword, cat in config['browser_keywords'].items():
            if keyword in window_title:
                return cat
        return "Navegando (General)"
    
    return category if category else "Others"


def initialize_log_file():
    """Initialize the activity log file with headers if it doesn't exist."""
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "app_name", "window_title", "category"])


def tracker_thread_func():
    """Main tracking thread function that continuously monitors activity."""
    print("🔄 Activity tracking thread started.")
    config = load_config()
    initialize_log_file()
    
    while True:
        with tracker_state['lock']:
            is_paused = tracker_state['is_paused']
        
        if not is_paused:
            app_name, window_title = get_active_window_info()
            category = get_category(app_name, window_title, config)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            with open(LOG_FILE, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([timestamp, app_name, window_title, category])
        
        time.sleep(CHECK_INTERVAL)


def format_time_display(td: timedelta) -> str:
    """
    Format timedelta object to HH:MM:SS string format.
    
    Args:
        td: Timedelta object
        
    Returns:
        Formatted time string
    """
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    return f"{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}"


# Flask Routes

@app.route('/')
def index():
    """Serve the main dashboard page."""
    return render_template('index.html')


@app.route('/data')
def get_data():
    """API endpoint to get activity data for the dashboard."""
    if not os.path.exists(LOG_FILE):
        return jsonify({"error": "No log file found"}), 404
    
    category_time = defaultdict(lambda: timedelta(0))
    interval = timedelta(seconds=CHECK_INTERVAL)
    
    try:
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                if len(row) >= 4:
                    category_time[row[3]] += interval
    except (IOError, StopIteration):
        pass
    
    sorted_categories = sorted(
        category_time.items(), 
        key=lambda item: item[1], 
        reverse=True
    )
    
    data_out = [{
        "category": cat,
        "time_str": format_time_display(td)
    } for cat, td in sorted_categories]
    
    return jsonify(data_out)


@app.route('/status', methods=['GET'])
def get_status():
    """API endpoint to get current tracking status."""
    with tracker_state['lock']:
        return jsonify({'is_paused': tracker_state['is_paused']})


@app.route('/toggle_pause', methods=['POST'])
def toggle_pause():
    """API endpoint to toggle tracking pause state."""
    with tracker_state['lock']:
        tracker_state['is_paused'] = not tracker_state['is_paused']
        status = tracker_state['is_paused']
    
    action = "paused" if status else "resumed"
    print(f"🔄 Activity tracking {action}.")
    
    return jsonify({'success': True, 'is_paused': status})


@app.route('/shutdown', methods=['POST'])
def shutdown():
    """API endpoint to gracefully shutdown the application."""
    print("🛑 Shutdown request received. Stopping the server.")
    
    # Graceful shutdown for development server
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        # Fallback to force kill if not running with Werkzeug server
        os.kill(os.getpid(), 9)
    else:
        func()
    
    return jsonify({"success": True, "message": "Server shutting down..."})


def main():
    """Main application entry point."""
    # Start tracking thread
    tracking_thread = threading.Thread(target=tracker_thread_func, daemon=True)
    tracking_thread.start()
    
    print(f"🚀 Dashboard started. Open your browser and go to http://{DEFAULT_HOST}:{DEFAULT_PORT}")
    print("📊 Real-time activity tracking is now active!")
    
    # Start Flask development server
    app.run(debug=False, host=DEFAULT_HOST, port=DEFAULT_PORT)


if __name__ == '__main__':
    main()