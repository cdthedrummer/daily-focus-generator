import pandas as pd
from datetime import datetime
import random
from collections import defaultdict

class TaskSuggester:
    def __init__(self):
        self.df = self._load_habits_data()
        self.patterns = self._analyze_patterns()
    
    def _parse_date(self, date_str):
        """Parse date string from the CSV format"""
        try:
            # Remove extra spaces and commas
            date_str = date_str.strip().strip(',')
            # Parse the date string
            return pd.to_datetime(date_str, format='%A, %B %d, ')
        except:
            return None
    
    def _load_habits_data(self):
        """Load and process the habits data from CSV"""
        try:
            df = pd.read_csv('Daily Habits - Daily Habits.csv')
            # Clean and convert date strings to datetime objects
            df['Date'] = df['Date'].apply(self._parse_date)
            # Drop any rows with invalid dates
            df = df.dropna(subset=['Date'])
            return df
        except Exception as e:
            print(f"Error loading habits data: {e}")
            return pd.DataFrame()  # Return empty DataFrame if there's an error
    
    def _analyze_patterns(self):
        """Analyze patterns in the data"""
        patterns = {
            'weekday_patterns': defaultdict(list),
            'habit_correlations': defaultdict(list),
            'energy_patterns': defaultdict(list)
        }
        
        if self.df.empty:
            return patterns
        
        # Analyze patterns by weekday
        for _, row in self.df.iterrows():
            weekday = row['Date'].strftime('%A')
            # Add completed habits
            for col in self.df.columns:
                if pd.api.types.is_bool_dtype(self.df[col]) and row[col]:
                    patterns['weekday_patterns'][weekday].append(col)
            
            # Add energy patterns
            if pd.notna(row['Energy Score (Today)']):
                patterns['energy_patterns'][weekday].append(row['Energy Score (Today)'])
        
        return patterns
    
    def get_contextual_suggestions(self, date=None):
        """Get contextual suggestions based on the date and patterns"""
        if date is None:
            date = datetime.now()
        
        weekday = date.strftime('%A')
        suggestions = []
        
        # Get weekday-specific suggestions
        weekday_habits = self.patterns['weekday_patterns'][weekday]
        if weekday_habits:
            suggestions.extend([
                {
                    "text": f"Complete your usual {habit}",
                    "type": "habit",
                    "source": "pattern_analysis",
                    "confidence": 0.8
                }
                for habit in set(weekday_habits)
            ])
        
        # Get energy-based suggestions
        energy_scores = self.patterns['energy_patterns'][weekday]
        if energy_scores:
            avg_energy = sum(energy_scores) / len(energy_scores)
            if avg_energy > 80:
                suggestions.append({
                    "text": "Schedule your most challenging task for today - you typically have high energy on this day",
                    "type": "energy_based",
                    "source": "pattern_analysis",
                    "confidence": 0.7
                })
        
        # Get priority-based suggestions
        if not self.df.empty:
            priorities = []
            for col in ['Priority 1', 'Priority 2', 'Priority 3']:
                priorities.extend(self.df[col].dropna().unique())
            
            # Count frequency of each priority
            priority_counts = pd.Series(priorities).value_counts()
            common_priorities = priority_counts.head(3).index.tolist()
            
            suggestions.extend([
                {
                    "text": priority,
                    "type": "priority",
                    "source": "pattern_analysis",
                    "confidence": 0.6
                }
                for priority in common_priorities
                if pd.notna(priority) and priority.strip()
            ])
        
        # Add some variety with random suggestions
        random_suggestions = [
            "Take a 10-minute break to stretch",
            "Review your progress for the week",
            "Plan tomorrow's tasks",
            "Do a quick mindfulness exercise",
            "Check your email inbox"
        ]
        
        suggestions.extend([
            {
                "text": suggestion,
                "type": "general",
                "source": "variety",
                "confidence": 0.5
            }
            for suggestion in random.sample(random_suggestions, 2)
        ])
        
        # Sort by confidence and return top suggestions
        suggestions.sort(key=lambda x: x['confidence'], reverse=True)
        return suggestions[:5]

# Create a singleton instance
suggester = TaskSuggester()

def get_suggestions(date=None):
    """Get contextual suggestions"""
    return suggester.get_contextual_suggestions(date) 