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
from flask_socketio import SocketIO, emit

# Global Configuration
LOG_FILE = 'activity_log.csv'
CONFIG_FILE = 'config.json'
CHECK_INTERVAL = 2  # Seconds (faster for real-time tracking)
DEFAULT_PORT = 5000
DEFAULT_HOST = '127.0.0.1'

# Flask application instance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# SocketIO instance for real-time communication
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

# Tracker state management
tracker_state = {
    'is_paused': False,
    'lock': threading.Lock(),
    'connected_clients': set(),
    'startup_time': datetime.now(),
    'last_activity': None
}

print(f"🚀 Digital Activity Tracker starting up...")
print(f"📅 Startup time: {tracker_state['startup_time']}")
print(f"🔧 Configuration: CHECK_INTERVAL={CHECK_INTERVAL}s, PORT={DEFAULT_PORT}")

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
    try:
        # Get active application
        app_name = run_applescript(APP_SCRIPT)
        if not app_name:
            return "Unknown", "Unknown"
        
        # Get URL if it's a supported browser
        if app_name in SUPPORTED_BROWSERS:
            url = run_applescript(URL_SCRIPT.format(app_name=app_name))
            return app_name, url or "No URL"
        else:
            return app_name, "Application Window"
            
    except Exception as e:
        print(f"❌ Error getting active window info: {e}")
        return "Error", "Error"


def load_config() -> dict:
    """
    Load application configuration from JSON file.
    
    Returns:
        Configuration dictionary
    """
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            config = json.load(f)
            print(f"✅ Configuration loaded successfully")
            return config
    except FileNotFoundError:
        print(f"⚠️  Config file not found: {CONFIG_FILE}")
        return {}
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing config file: {e}")
        return {}


def get_category(app_name: str, window_title: str, config: dict) -> str:
    """
    Determine the category for the given application and window title.
    
    Args:
        app_name: Name of the active application
        window_title: Window title or URL
        
    Returns:
        Category string
    """
    app_name_lower = app_name.lower()
    window_title_lower = window_title.lower()
    
    # Check application mappings
    for app_pattern, category in config.get('applications', {}).items():
        if app_pattern.lower() in app_name_lower:
            return f"{category} - {app_name}"
    
    # Check browser keyword mappings
    for keyword, category in config.get('browser_keywords', {}).items():
        if keyword.lower() in window_title_lower:
            return f"{category} - {app_name}"
    
    return f"Other - {app_name}"


def initialize_log_file():
    """Initialize the activity log file with headers."""
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['timestamp', 'app_name', 'window_title', 'category'])
        print(f"📝 Log file initialized: {LOG_FILE}")


def format_time_display(td: timedelta) -> str:
    """
    Format timedelta object to HH:MM:SS string.
    
    Args:
        td: Timedelta object
        
    Returns:
        Formatted time string
    """
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def get_activity_data() -> list:
    """
    Get current activity data from the log file.
    
    Returns:
        List of activity data dictionaries
    """
    try:
        if not os.path.exists(LOG_FILE):
            print(f"📊 No activity data available yet (log file doesn't exist)")
            return []
        
        # Read and aggregate data
        category_times = defaultdict(timedelta)
        
        with open(LOG_FILE, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    timestamp = datetime.fromisoformat(row['timestamp'])
                    category = row['category']
                    category_times[category] += timedelta(seconds=CHECK_INTERVAL)
                except (ValueError, KeyError) as e:
                    print(f"⚠️  Error parsing log row: {e}")
                    continue
        
        # Convert to list format
        data = []
        for category, time_spent in sorted(category_times.items(), key=lambda x: x[1], reverse=True):
            data.append({
                'category': category,
                'time_str': format_time_display(time_spent)
            })
        
        print(f"📊 Activity data retrieved: {len(data)} categories")
        return data
        
    except Exception as e:
        print(f"❌ Error getting activity data: {e}")
        return []


def emit_activity_update():
    """Emit real-time activity update to all connected clients."""
    if not tracker_state['connected_clients']:
        print(f"📡 No connected clients to emit update to")
        return
    
    data = get_activity_data()
    status = {'is_paused': tracker_state['is_paused']}
    
    update_data = {
        'data': data,
        'status': status,
        'timestamp': datetime.now().isoformat()
    }
    
    print(f"📡 Emitting update to {len(tracker_state['connected_clients'])} clients")
    socketio.emit('activity_update', update_data)


def tracker_thread_func():
    """Main tracking thread function that continuously monitors activity."""
    print(f"🔄 Starting activity tracking thread...")
    
    config = load_config()
    initialize_log_file()
    
    last_app = None
    last_window = None
    last_category = None
    
    while True:
        try:
            with tracker_state['lock']:
                is_paused = tracker_state['is_paused']
            
            if is_paused:
                time.sleep(CHECK_INTERVAL)
                continue
            
            # Get current activity
            app_name, window_title = get_active_window_info()
            category = get_category(app_name, window_title, config)
            
            # Check if activity changed
            if (app_name != last_app or window_title != last_window or 
                category != last_category):
                
                # Log the activity
                timestamp = datetime.now()
                with open(LOG_FILE, 'a', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow([timestamp.isoformat(), app_name, window_title, category])
                
                print(f"📝 Activity logged: {category} ({app_name})")
                
                # Update state
                last_app = app_name
                last_window = window_title
                last_category = category
                tracker_state['last_activity'] = timestamp
                
                # Emit real-time update
                emit_activity_update()
            
            time.sleep(CHECK_INTERVAL)
            
        except Exception as e:
            print(f"❌ Error in tracking thread: {e}")
            time.sleep(CHECK_INTERVAL)


@app.route('/')
def index():
    """Serve the main dashboard page."""
    print(f"🌐 Dashboard requested from {request.remote_addr}")
    return render_template('index.html')


@app.route('/data')
def get_data():
    """Get current activity data (fallback for non-WebSocket clients)."""
    print(f"📊 Data requested from {request.remote_addr}")
    data = get_activity_data()
    return jsonify(data)


@app.route('/status', methods=['GET'])
def get_status():
    """Get current tracking status (fallback for non-WebSocket clients)."""
    print(f"📈 Status requested from {request.remote_addr}")
    with tracker_state['lock']:
        status = {
            'is_paused': tracker_state['is_paused'],
            'startup_time': tracker_state['startup_time'].isoformat(),
            'last_activity': tracker_state['last_activity'].isoformat() if tracker_state['last_activity'] else None,
            'connected_clients': len(tracker_state['connected_clients'])
        }
    return jsonify(status)


@app.route('/toggle_pause', methods=['POST'])
def toggle_pause():
    """Toggle pause/resume tracking (fallback for non-WebSocket clients)."""
    print(f"⏸️ Pause toggle requested from {request.remote_addr}")
    with tracker_state['lock']:
        tracker_state['is_paused'] = not tracker_state['is_paused']
        status = tracker_state['is_paused']
    
    action = "paused" if status else "resumed"
    print(f"🔄 Activity tracking {action}")
    
    # Emit update to connected clients
    emit_activity_update()
    
    return jsonify({'is_paused': status})


@app.route('/shutdown', methods=['POST'])
def shutdown():
    """Shutdown the application (fallback for non-WebSocket clients)."""
    print(f"🛑 Shutdown requested from {request.remote_addr}")
    
    # Emit shutdown notification to all clients
    socketio.emit('shutdown_notification', {
        'message': 'Server is shutting down...',
        'timestamp': datetime.now().isoformat()
    })
    
    # Schedule shutdown after a short delay
    def delayed_shutdown():
        time.sleep(2)
        print("🛑 Shutting down application...")
        os._exit(0)
    
    threading.Thread(target=delayed_shutdown, daemon=True).start()
    return jsonify({'message': 'Shutdown initiated'})


@socketio.on('connect')
def handle_connect():
    """Handle client connection."""
    client_id = request.sid
    print(f"🔗 Client connected: {client_id} from {request.remote_addr}")
    tracker_state['connected_clients'].add(client_id)
    
    # Send initial data to the new client
    print(f"📤 Sending initial data to client {client_id}")
    emit_activity_update()


@socketio.on('disconnect')
def handle_disconnect():
    """Handle client disconnection."""
    client_id = request.sid
    print(f"🔌 Client disconnected: {client_id}")
    tracker_state['connected_clients'].discard(client_id)


@socketio.on('toggle_pause')
def handle_toggle_pause():
    """Handle pause toggle via WebSocket."""
    client_id = request.sid
    print(f"⏸️ Pause toggle requested via WebSocket from {client_id}")
    
    with tracker_state['lock']:
        tracker_state['is_paused'] = not tracker_state['is_paused']
        status = tracker_state['is_paused']
    
    action = "paused" if status else "resumed"
    print(f"🔄 Activity tracking {action} via WebSocket")
    
    # Emit status update to all connected clients
    emit_activity_update()
    
    # Send confirmation to requesting client
    emit('pause_toggled', {'is_paused': status})


@socketio.on('request_shutdown')
def handle_shutdown_request():
    """Handle shutdown request via WebSocket."""
    client_id = request.sid
    print(f"🛑 Shutdown request received via WebSocket from {client_id}")
    
    # Emit shutdown notification to all clients
    socketio.emit('shutdown_notification', {
        'message': 'Server is shutting down...',
        'timestamp': datetime.now().isoformat()
    })
    
    # Schedule shutdown after a short delay
    def delayed_shutdown():
        time.sleep(2)
        print("🛑 Shutting down application...")
        os._exit(0)
    
    threading.Thread(target=delayed_shutdown, daemon=True).start()


def main():
    """Main application entry point."""
    print(f"🚀 Starting Digital Activity Tracker...")
    print(f"🌐 Server will be available at: http://{DEFAULT_HOST}:{DEFAULT_PORT}")
    print(f"⚡ WebSocket support enabled for real-time updates")
    
    # Start tracking thread
    tracker_thread = threading.Thread(target=tracker_thread_func, daemon=True)
    tracker_thread.start()
    print(f"🔄 Activity tracking thread started")
    
    # Start Flask-SocketIO server
    print(f"🌐 Starting Flask-SocketIO server...")
    socketio.run(app, debug=False, host=DEFAULT_HOST, port=DEFAULT_PORT)


if __name__ == '__main__':
    main()