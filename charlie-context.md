# Charlie's Task Generator - Full Context Document

## USER PROFILE: Charlie Dickerson

### Core Personality & Cognitive Style

Charlie exhibits a blend of creativity, analytical thinking, and entrepreneurial vision. His cognitive style is characterized by:

- **Exceptional ideation capabilities** - Consistently generates novel solutions to everyday problems
- **Strategic-oriented thinking** - Naturally gravitates toward high-level direction and vision
- **Executive function pattern** - High initial energy that gradually diminishes when facing technical execution challenges
- **Professional strengths** - Excels in senior director/leadership roles where he can identify opportunities, create strategic direction, and delegate execution
- **Communication style** - Direct, authentic communication with self-deprecating humor

### Motivational Framework

#### Intrinsic Motivators
1. **Knowledge Acquisition** - Deeply engaged when learning new skills or domains
2. **Problem Solving** - Derives significant satisfaction from solving real problems
3. **Creative Expression** - Most engaged during early creative phases of projects
4. **Recognition of Competence** - Values acknowledgment of capabilities from respected peers

#### External Motivators
1. **Social Validation** - Positive feedback provides significant motivational energy
2. **Resource Efficiency** - Sensitive to time/money investment efficiency
3. **Tangible Results** - Motivated by seeing functional prototypes and working examples

### Current Projects

1. **Laundry Basket (TidyBasket)**
   - A dryer attachment that helps prevent clothes from falling
   - Current state: Working prototype but stalled on consumer-ready version
   - Next steps: Find manufacturing partner

2. **Hourly Wage App**
   - App for comparing local job opportunities for hourly workers
   - Current state: Basic UI mockup and job scraper for one chain
   - Stalled on: Connecting scraper to UI, expanding business listings

3. **Self-Improvement App**
   - Gaming-inspired character building for real-life skill development
   - Current step: Building quiz app as foundation

4. **Quiz App**
   - Personal skills assessment as entry point to self-improvement app
   - Stalled on: Technical implementation and visual design issues

### Common Project Patterns

- **Energy peaks** at project beginnings or during learning phases
- **Interest maintained** when continuously learning and seeing results
- **Momentum fades** with technical implementation challenges
- **Typically completes** the creative/strategic elements (branding, design, marketing) but struggles with technical execution
- **Most successful** when able to delegate implementation details

## PROJECT GOALS: Daily Focus Generator

### Core Concept
A personalized task generation system that creates daily focus suggestions based on Charlie's psychological profile, work patterns, and current projects.

### Key Design Principles

1. **Strength-Based Approach**
   - Frame tasks to leverage strategic and creative strengths
   - Minimize implementation-heavy suggestions or chunk them into small segments

2. **Energy-Aware Scheduling**
   - Suggest strategic/creative tasks during high-energy periods
   - Schedule implementation in brief, focused sessions

3. **Learning-Oriented Framing**
   - Include knowledge acquisition components to maintain engagement
   - Present implementation tasks as learning opportunities

4. **Accountability Through Structure**
   - Create lightweight accountability mechanisms
   - Focus on strategic direction rather than tactical details

5. **Quick Feedback Loops**
   - Provide visible progress indicators
   - Celebrate small wins to maintain momentum

### Technical Implementation Plan

The system should consist of these core components:

1. **Configuration Files**
   - `config.json`: Personal preferences and work patterns
   - `projects.json`: Current project data and next steps
   - `templates.json`: Task suggestion templates by category

2. **Task Generation Engine**
   - `generate_tasks.py`: Core logic for creating daily task suggestions
   - Should intelligently select from templates based on preferences

3. **Optional Interface**
   - `web_app.py`: Simple Streamlit-based web interface for interaction

## DETAILED COMPONENT SPECIFICATIONS

### config.json
This file contains Charlie's personal preferences and work patterns:

```json
{
  "name": "Charlie",
  "preferences": {
    "strategic_weight": 4,
    "creative_weight": 4,
    "implementation_weight": 1,
    "learning_weight": 3,
    "morning_preference": true,
    "afternoon_preference": false,
    "evening_preference": true
  },
  "energy_profiles": {
    "Monday": "morning",
    "Tuesday": "balanced",
    "Wednesday": "balanced",
    "Thursday": "afternoon",
    "Friday": "morning",
    "Saturday": "balanced",
    "Sunday": "evening"
  },
  "motivation_triggers": {
    "learning_new_skills": true,
    "visible_progress": true,
    "recognition": true,
    "problem_solving": true
  },
  "demotivation_triggers": {
    "repetitive_tasks": true,
    "unclear_outcomes": true,
    "excessive_implementation": true,
    "lack_of_feedback": true
  },
  "task_preferences": {
    "max_daily_tasks": 5,
    "prefer_single_project_focus": true,
    "implementation_chunking": 15,
    "include_personal_development": true
  }
}
```

### projects.json
Contains data about Charlie's current projects:

```json
{
  "projects": [
    {
      "name": "Laundry Basket (TidyBasket)",
      "description": "A lightweight attachment that clamps to the open dryer's inside lip, allowing users to scoop clothes out and directly into a laundry basket.",
      "status": "active",
      "priority": 4,
      "last_touched": "2025-02-01",
      "current_focus": "finding a manufacturing partner",
      "next_steps": [
        "Refine consumer-ready prototype",
        "Contact potential manufacturing partners",
        "Create pitch deck for licensing"
      ],
      "strengths_alignment": {
        "strategic": "business model development",
        "creative": "product design refinement",
        "implementation": "prototype creation",
        "learning": "manufacturing processes"
      }
    },
    {
      "name": "Hourly Wage App",
      "description": "A dating-app-like environment where hourly-waged employees could swipe on jobs around their area.",
      "status": "paused",
      "priority": 2,
      "last_touched": "2025-01-15",
      "current_focus": "connecting scraper to UI",
      "next_steps": [
        "Connect existing Aldi scraper to UI",
        "Test basic functionality",
        "Expand scraping to additional businesses"
      ],
      "strengths_alignment": {
        "strategic": "business model development",
        "creative": "UI refinement",
        "implementation": "connecting scraper to UI",
        "learning": "database integration"
      }
    },
    {
      "name": "Self-Improvement App",
      "description": "An app that applies gaming character building to real-life goals, connecting users with local businesses for skill development.",
      "status": "active",
      "priority": 3,
      "last_touched": "2025-03-10",
      "current_focus": "quiz app foundation",
      "next_steps": [
        "Fix remaining quiz app bugs",
        "Improve visual design",
        "Test with small user group"
      ],
      "strengths_alignment": {
        "strategic": "overall product strategy",
        "creative": "quiz question development",
        "implementation": "basic functionality coding",
        "learning": "app development fundamentals"
      }
    }
  ]
}
```

### templates.json
Task templates categorized by type:

```json
{
  "task_templates": {
    "strategic": [
      "Draft a one-page business plan for {project_name} focused on {project_focus}",
      "Create a list of 3 potential business models for {project_name}",
      "Identify 5 companies who might be interested in licensing {project_name}",
      "Research competitors in the {project_name} space and note their strengths/weaknesses",
      "Map out the ideal user journey for {project_name}",
      "Draft a marketing strategy outline for {project_name}",
      "Sketch a roadmap of the next 3 milestones for {project_name}"
    ],
    "creative": [
      "Sketch 3 variations of {project_name} to solve the core problem differently",
      "Create mockups or wireframes for {project_name} focused on {project_focus}",
      "Brainstorm 10 names/taglines for {project_name}",
      "Design a simple logo concept for {project_name}",
      "Draft website copy for a {project_name} landing page",
      "Storyboard a 30-second pitch video for {project_name}",
      "Create a mood board for {project_name} brand identity"
    ],
    "implementation": [
      "Spend 15 minutes fixing one specific bug in {project_name}",
      "Set up a basic project structure for the next phase of {project_name}",
      "Contact 3 potential partners/vendors about {project_focus} for {project_name}",
      "Create a simple prototype demonstrating one key feature of {project_name}",
      "Write documentation for one aspect of {project_name}",
      "Prepare an email template for outreach related to {project_name}",
      "Schedule three 15-minute sessions this week to work on {project_focus} for {project_name}"
    ],
    "learning": [
      "Watch one tutorial on a skill needed for {project_name} (related to {project_focus})",
      "Read an article about the industry relevant to {project_name}",
      "Find and analyze a case study of a similar product to {project_name}",
      "Learn one new technique that would help with {project_focus} in {project_name}",
      "Research manufacturing/development costs for {project_name}",
      "Find a relevant expert on LinkedIn who could advise on {project_focus} for {project_name}",
      "Study a successful product similar to {project_name} and note what makes it work"
    ]
  },
  "personal_development": [
    "Take a 15-minute walk to clear your mind and gain perspective",
    "Practice 10 minutes of focused breathing to reduce stress",
    "Write down 3 wins from yesterday to build momentum",
    "Read one chapter of a book related to entrepreneurship or creativity",
    "Reach out to one person in your network just to catch up",
    "Spend 20 minutes learning something new unrelated to work",
    "Take 15 minutes to organize your workspace",
    "Journal about one challenge you're facing and brainstorm solutions",
    "Schedule a short coffee chat with someone who inspires you",
    "Dedicate 30 minutes to physical exercise"
  ]
}
```

### generate_tasks.py
Core Python script that generates the daily task list:

```python
#!/usr/bin/env python3

import json
import random
import datetime
import os
from typing import List, Dict, Any

class DailyFocusGenerator:
    """Generate personalized daily focus tasks based on user preferences and patterns."""
    
    def __init__(self):
        self.config = self._load_json('config.json')
        self.projects = self._load_json('projects.json')
        self.templates = self._load_json('templates.json')
        self.today = datetime.datetime.now()
    
    def _load_json(self, filename: str) -> Dict[str, Any]:
        """Load JSON data from a file."""
        if not os.path.exists(filename):
            print(f"Warning: {filename} not found. Using default settings.")
            return {}
        
        with open(filename, 'r') as file:
            return json.load(file)
    
    def _get_day_energy_profile(self) -> str:
        """Determine the energy profile for today based on day of week and preferences."""
        day_of_week = self.today.strftime('%A')
        return self.config.get('energy_profiles', {}).get(day_of_week, 'balanced')
    
    def _get_active_projects(self) -> List[Dict[str, Any]]:
        """Get list of currently active projects."""
        return [p for p in self.projects.get('projects', []) if p.get('status') == 'active']
    
    def _select_project_focus(self) -> Dict[str, Any]:
        """Select a project to focus on today based on priority and last touched date."""
        active_projects = self._get_active_projects()
        if not active_projects:
            return None
            
        # Weight projects by priority and days since last touched
        weighted_projects = []
        for project in active_projects:
            last_touched = datetime.datetime.strptime(project.get('last_touched', '2025-01-01'), '%Y-%m-%d')
            days_since = (self.today - last_touched).days
            priority = project.get('priority', 3)  # 1-5 scale
            
            # Higher priority and longer untouched gets higher weight
            weight = priority * (1 + days_since / 7)  # Bonus for each week untouched
            weighted_projects.append((weight, project))
        
        # Sort by weight and take top project, with some randomness
        weighted_projects.sort(reverse=True)
        
        # 70% chance of picking the highest priority, 30% chance of picking another
        if random.random() < 0.7 or len(weighted_projects) == 1:
            return weighted_projects[0][1]
        else:
            return random.choice(weighted_projects[1:])[1] if len(weighted_projects) > 1 else weighted_projects[0][1]
    
    def _generate_task_suggestion(self, category: str, project: Dict[str, Any]) -> str:
        """Generate a specific task suggestion based on category and project."""
        templates = self.templates.get('task_templates', {}).get(category, [])
        if not templates:
            return f"Work on {category} for {project['name']}"
        
        template = random.choice(templates)
        
        # Replace placeholders
        task = template.replace('{project_name}', project['name'])
        task = task.replace('{project_focus}', project.get('current_focus', 'next steps'))
        
        # Add time suggestion based on energy profile
        energy_profile = self._get_day_energy_profile()
        if energy_profile == 'morning':
            task += " (Morning: 9-11am)"
        elif energy_profile == 'afternoon':
            task += " (Afternoon: 2-4pm)"
        elif energy_profile == 'evening':
            task += " (Evening: 7-9pm)"
        
        return task
    
    def generate_daily_focus(self, num_tasks: int = 3) -> List[str]:
        """Generate a list of suggested focus tasks for today."""
        focus_project = self._select_project_focus()
        if not focus_project:
            return ["No active projects found. Add some projects to get started!"]
        
        # Balance task types based on user strengths and preferences
        task_categories = {
            'strategic': self.config.get('preferences', {}).get('strategic_weight', 3),
            'creative': self.config.get('preferences', {}).get('creative_weight', 3),
            'implementation': self.config.get('preferences', {}).get('implementation_weight', 1),
            'learning': self.config.get('preferences', {}).get('learning_weight', 2)
        }
        
        # Normalize weights
        total_weight = sum(task_categories.values())
        for category in task_categories:
            task_categories[category] /= total_weight
        
        # Generate weighted random selection of categories
        categories = []
        for _ in range(num_tasks):
            rand = random.random()
            cumulative = 0
            selected_category = list(task_categories.keys())[-1]  # Default to last category
            
            for category, weight in task_categories.items():
                cumulative += weight
                if rand <= cumulative:
                    selected_category = category
                    break
            
            categories.append(selected_category)
        
        # Generate actual tasks
        tasks = [self._generate_task_suggestion(category, focus_project) for category in categories]
        
        # Add a bonus habit/personal development suggestion
        personal_tasks = self.templates.get('personal_development', [])
        if personal_tasks:
            tasks.append(random.choice(personal_tasks))
            
        return tasks


if __name__ == "__main__":
    generator = DailyFocusGenerator()
    tasks = generator.generate_daily_focus(4)  # Generate 4 focus areas for today
    
    print(f"\n==== Daily Focus: {datetime.datetime.now().strftime('%A, %B %d, %Y')} ====\n")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print("\nRemember: Focus on starting rather than completing. 15 minutes is better than nothing!")
```

### web_app.py (Optional)
A simple Streamlit web interface for interacting with the task generator:

```python
#!/usr/bin/env python3

import streamlit as st
import json
import datetime
import os
from generate_tasks import DailyFocusGenerator

# Set page configuration
st.set_page_config(
    page_title="Daily Focus Generator",
    page_icon="🎯",
    layout="wide"
)

# Initialize session state variables if they don't exist
if 'tasks' not in st.session_state:
    st.session_state.tasks = []
if 'completed_tasks' not in st.session_state:
    st.session_state.completed_tasks = []
if 'history' not in st.session_state:
    st.session_state.history = []

# Helper functions
def save_task_history():
    """Save task history to a JSON file"""
    history_entry = {
        "date": datetime.datetime.now().strftime("%Y-%m-%d"),
        "tasks": st.session_state.tasks,
        "completed": st.session_state.completed_tasks
    }
    st.session_state.history.append(history_entry)
    
    with open('task_history.json', 'w') as f:
        json.dump({"history": st.session_state.history}, f, indent=2)

def load_task_history():
    """Load task history from JSON file"""
    if os.path.exists('task_history.json'):
        with open('task_history.json', 'r') as f:
            data = json.load(f)
            st.session_state.history = data.get('history', [])

# Load history on startup
load_task_history()

# Main app layout
st.title("🎯 Daily Focus Generator")

# Sidebar for configuration
with st.sidebar:
    st.header("Configuration")
    
    # Project management section
    st.subheader("Active Projects")
    
    # Load projects
    projects = []
    if os.path.exists('projects.json'):
        with open('projects.json', 'r') as f:
            projects_data = json.load(f)
            projects = projects_data.get('projects', [])
    
    # Display projects with status toggles
    updated_projects = []
    for project in projects:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(project['name'])
        with col2:
            active = st.checkbox("Active", value=(project['status'] == 'active'), key=f"prj_{project['name']}")
        
        project['status'] = 'active' if active else 'paused'
        updated_projects.append(project)
    
    # Save updated project status
    if st.button("Save Project Status"):
        with open('projects.json', 'w') as f:
            json.dump({"projects": updated_projects}, f, indent=2)
        st.success("Project status updated!")
    
    st.divider()
    
    # Preferences section
    st.subheader("Task Preferences")
    
    # Load config
    config = {}
    if os.path.exists('config.json'):
        with open('config.json', 'r') as f:
            config = json.load(f)
    
    preferences = config.get('preferences', {})
    
    # Simple preference sliders
    strategic = st.slider("Strategic tasks", 1, 5, preferences.get('strategic_weight', 3))
    creative = st.slider("Creative tasks", 1, 5, preferences.get('creative_weight', 3))
    implementation = st.slider("Implementation tasks", 1, 5, preferences.get('implementation_weight', 1))
    learning = st.slider("Learning tasks", 1, 5, preferences.get('learning_weight', 2))
    
    max_tasks = st.number_input("Max daily tasks", 1, 10, preferences.get('max_daily_tasks', 5))
    
    # Save preferences
    if st.button("Save Preferences"):
        preferences['strategic_weight'] = strategic
        preferences['creative_weight'] = creative
        preferences['implementation_weight'] = implementation
        preferences['learning_weight'] = learning
        preferences['max_daily_tasks'] = max_tasks
        
        config['preferences'] = preferences
        
        with open('config.json', 'w') as f:
            json.dump(config, f, indent=2)
        
        st.success("Preferences saved!")

# Main content area
tasks_col, history_col = st.columns([3, 2])

with tasks_col:
    st.header(f"Today's Focus: {datetime.datetime.now().strftime('%A, %B %d')}")
    
    # Generate new tasks button
    if st.button("Generate New Tasks", use_container_width=True):
        generator = DailyFocusGenerator()
        st.session_state.tasks = generator.generate_daily_focus(int(max_tasks))
        st.session_state.completed_tasks = [False] * len(st.session_state.tasks)
        save_task_history()
    
    # Display tasks with checkboxes
    if st.session_state.tasks:
        for i, (task, completed) in enumerate(zip(st.session_state.tasks, st.session_state.completed_tasks)):
            col1, col2 = st.columns([0.9, 0.1])
            with col1:
                st.write(f"{i+1}. {task}")
            with col2:
                st.session_state.completed_tasks[i] = st.checkbox("Done", value=completed, key=f"task_{i}")
        
        # Save completion status
        if st.button("Save Progress", use_container_width=True):
            save_task_history()
            st.success("Progress saved!")
    else:
        st.info("Click 'Generate New Tasks' to get started!")
    
    # Daily reflection
    st.subheader("Daily Reflection")
    reflection = st.text_area("What went well today? What could be improved?", height=100)
    if st.button("Save Reflection", use_container_width=True) and reflection:
        # Add reflection to latest history entry
        if st.session_state.history:
            st.session_state.history[-1]["reflection"] = reflection
            with open('task_history.json', 'w') as f:
                json.dump({"history": st.session_state.history}, f, indent=2)
            st.success("Reflection saved!")

with history_col:
    st.header("Progress History")
    
    # Display recent task history
    if st.session_state.history:
        history_items = list(reversed(st.session_state.history[-7:]))  # Last 7 days
        
        for entry in history_items:
            with st.expander(f"{entry['date']}"):
                completed_count = sum(1 for comp in entry.get('completed', []) if comp)
                total_count = len(entry.get('tasks', []))
                
                if total_count > 0:
                    completion_rate = completed_count / total_count * 100
                    st.progress(completion_rate / 100)
                    st.write(f"Completed: {completed_count}/{total_count} ({completion_rate:.0f}%)")
                
                st.subheader("Tasks:")
                for i, (task, completed) in enumerate(zip(entry.get('tasks', []), entry.get('completed', []))):
                    status = "✅" if completed else "⬜️"
                    st.write(f"{status} {task}")
                
                if "reflection" in entry:
                    st.subheader("Reflection:")
                    st.write(entry["reflection"])
    else:
        st.info("No history yet. Start generating tasks to build your history!")

# Footer
st.divider()
st.caption(
    "Remember: Focus on starting rather than completing. 15 minutes is better than nothing!"
)
```

### requirements.txt

```
streamlit>=1.27.0
python-dateutil>=2.8.2
pandas>=2.0.0
matplotlib>=3.7.0
```

## TECHNICAL DESIGN PRINCIPLES

1. **Modular Architecture**
   - Each file has a clear, specific purpose
   - Configuration is separate from logic

2. **User-Friendly Implementation**
   - Simple command-line interface for basic usage
   - Optional web interface for richer interaction

3. **Extensibility**
   - Easily add new task templates
   - Configuration can be expanded without code changes
   - Project data can grow over time

4. **Minimal Dependencies**
   - Core functionality works with standard Python libraries
   - Web interface uses Streamlit for simple deployment

## DEVELOPMENT ROADMAP

### Phase 1: Core Functionality
1. Create configuration files (config.json, projects.json, templates.json)
2. Implement basic task generation (generate_tasks.py)
3. Test command-line functionality

### Phase 2: User Interface (Optional)
1. Implement Streamlit web app (web_app.py)
2. Add task completion tracking
3. Add history/progress visualization

### Phase 3: Enhancement (Future)
1. Add more sophisticated project selection logic
2. Implement reminder/notification system
3. Add integration with calendar/task apps

## IMPLEMENTATION TIPS

1. **Start Simple**
   - Get basic generation working first
   - Add refinements iteratively

2. **Test With Real Projects**
   - Use your actual current projects
   - Modify task templates to match your specific needs

3. **Maintain Customization**
   - Keep adjusting weights and preferences
   - Add new task templates as needed

4. **Focus on Value**
   - The goal is not a perfect app, but rather a useful tool
   - Even a simple version should provide immediate value

---

Use this document as a comprehensive reference while developing the Daily Focus Generator. Each section provides context and guidance tailored to Charlie's specific needs and work patterns.
