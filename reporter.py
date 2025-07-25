"""
Digital Activity Reporter

A utility script to analyze and generate reports from activity tracking data.
Provides insights into time spent across different digital activities.

Author: Ramthedev
License: MIT
"""

import csv
from collections import defaultdict
from datetime import timedelta

# Configuration
LOG_FILE = 'activity_log.csv'
# This value must match CHECK_INTERVAL in app.py
INTERVAL_SECONDS = 2


def format_timedelta(td: timedelta) -> str:
    """
    Format a timedelta object to a human-readable format.
    
    Args:
        td: Timedelta object to format
        
    Returns:
        Formatted string with hours, minutes, and seconds
    """
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    parts = []
    if hours > 0:
        parts.append(f"{hours} hour(s)")
    if minutes > 0:
        parts.append(f"{minutes} minute(s)")
    if seconds > 0 and not parts:
        parts.append(f"{seconds} second(s)")
    
    return ", ".join(parts) if parts else "0 seconds"


def load_activity_data() -> list:
    """
    Load activity data from the CSV log file.
    
    Returns:
        List of activity records
        
    Raises:
        FileNotFoundError: If the log file doesn't exist
    """
    try:
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            return list(reader)
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Activity log file '{LOG_FILE}' not found. "
            "Make sure to run the tracker first to start recording activity."
        )


def calculate_category_times(records: list) -> dict:
    """
    Calculate total time spent in each activity category.
    
    Args:
        records: List of activity records from CSV
        
    Returns:
        Dictionary mapping categories to total time spent
    """
    category_time = defaultdict(timedelta)
    interval = timedelta(seconds=INTERVAL_SECONDS)
    
    for record in records:
        if len(record) < 4:
            continue  # Skip malformed records
        
        # Category is in the 4th column (index 3)
        category = record[3]
        category_time[category] += interval
    
    return category_time


def display_activity_summary(category_time: dict):
    """
    Display a formatted summary of activity data.
    
    Args:
        category_time: Dictionary mapping categories to time spent
    """
    if not category_time:
        print("📝 No activity data found.")
        return
    
    print("📊 Activity Summary Report")
    print("=" * 50)
    
    # Sort categories by time spent (descending)
    sorted_categories = sorted(
        category_time.items(), 
        key=lambda item: item[1], 
        reverse=True
    )
    
    total_time = sum(category_time.values())
    print(f"Total tracking time: {format_timedelta(total_time)}")
    print(f"Number of categories: {len(category_time)}")
    print()
    
    for i, (category, total_time) in enumerate(sorted_categories, 1):
        percentage = (total_time.total_seconds() / sum(category_time.values()).total_seconds()) * 100
        print(f"{i:2d}. {category:<30} {format_timedelta(total_time):<15} ({percentage:5.1f}%)")


def analyze_activity():
    """
    Main function to analyze activity data and generate a report.
    """
    try:
        # Load activity data
        records = load_activity_data()
        
        if not records:
            print("📝 Activity log is empty.")
            print("Start using your computer to see activity data.")
            return
        
        # Calculate category times
        category_time = calculate_category_times(records)
        
        # Display summary
        display_activity_summary(category_time)
        
    except FileNotFoundError as e:
        print(f"❌ {e}")
        print("💡 Tip: Run 'make run-app' to start the activity tracker.")
    except Exception as e:
        print(f"❌ Error analyzing activity data: {e}")


def main():
    """Main entry point for the reporter script."""
    print("🔍 Digital Activity Reporter")
    print("=" * 30)
    analyze_activity()


if __name__ == "__main__":
    main()
