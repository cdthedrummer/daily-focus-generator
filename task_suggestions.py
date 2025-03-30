import pandas as pd
from datetime import datetime
import random

def clean_date(date_str):
    """Clean and parse date string from the CSV format"""
    # Remove extra spaces and commas
    date_str = date_str.strip().strip(',')
    # Parse the date string
    try:
        return pd.to_datetime(date_str)
    except:
        return None

def load_habits_data():
    """Load and process the habits data from CSV"""
    df = pd.read_csv('Daily Habits - Daily Habits.csv')
    # Clean and convert date strings to datetime objects
    df['Date'] = df['Date'].apply(clean_date)
    # Drop any rows with invalid dates
    df = df.dropna(subset=['Date'])
    return df

def get_priority_suggestions():
    """Generate task suggestions based on historical priority data"""
    try:
        df = load_habits_data()
        
        # Get all unique priorities from the data
        priorities = []
        for col in ['Priority 1', 'Priority 2', 'Priority 3']:
            priorities.extend(df[col].dropna().unique())
        
        # Count frequency of each priority
        priority_counts = pd.Series(priorities).value_counts()
        
        # Get the most common priorities
        common_priorities = priority_counts.head(5).index.tolist()
        
        # Generate suggestions based on common priorities
        suggestions = []
        for priority in common_priorities:
            if pd.notna(priority) and priority.strip():
                suggestions.append({
                    "text": priority,
                    "type": "priority",
                    "source": "historical_data"
                })
        
        return suggestions
    except Exception as e:
        print(f"Error getting priority suggestions: {e}")
        return []

def get_habit_suggestions():
    """Generate task suggestions based on daily habits"""
    try:
        df = load_habits_data()
        
        # Get boolean columns (habits)
        habit_columns = df.select_dtypes(include=['bool']).columns
        
        # Calculate completion rate for each habit
        habit_stats = {}
        for col in habit_columns:
            if col not in ['Tried Something New']:  # Exclude special columns
                completion_rate = df[col].mean()
                if completion_rate > 0.3:  # Only include habits that were done at least 30% of the time
                    habit_stats[col] = completion_rate
        
        # Generate suggestions based on habits
        suggestions = []
        for habit, rate in habit_stats.items():
            if rate < 0.8:  # Only suggest habits that aren't already consistently done
                suggestions.append({
                    "text": f"Complete daily habit: {habit}",
                    "type": "habit",
                    "source": "historical_data",
                    "completion_rate": rate
                })
        
        return suggestions
    except Exception as e:
        print(f"Error getting habit suggestions: {e}")
        return []

def get_suggestions():
    """Get all task suggestions"""
    suggestions = []
    
    # Add priority-based suggestions
    suggestions.extend(get_priority_suggestions())
    
    # Add habit-based suggestions
    suggestions.extend(get_habit_suggestions())
    
    # Shuffle suggestions
    random.shuffle(suggestions)
    
    return suggestions 