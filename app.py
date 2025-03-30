import streamlit as st
import json
from datetime import datetime, timedelta
import os
from ai_suggestions import get_suggestions

# Set page config for better mobile experience
st.set_page_config(
    page_title="Daily Focus",
    page_icon="🎯",
    layout="wide"
)

# Initialize session state for tasks if it doesn't exist
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Initialize session state for input clearing
if 'clear_input' not in st.session_state:
    st.session_state.clear_input = False

def save_tasks():
    """Save tasks to a JSON file"""
    with open('tasks.json', 'w') as f:
        json.dump(st.session_state.tasks, f)

def load_tasks():
    """Load tasks from JSON file"""
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as f:
            return json.load(f)
    return []

# Load existing tasks
if not st.session_state.tasks:
    st.session_state.tasks = load_tasks()

# Main title with emoji
st.title("🎯 Daily Focus & Goals")

# Create two columns for better layout
col1, col2 = st.columns([2, 1])

with col1:
    # Date selector for viewing different days
    selected_date = st.date_input(
        "📅 Select Date",
        datetime.now(),
        min_value=datetime.now() - timedelta(days=7),
        max_value=datetime.now() + timedelta(days=7)
    )

    # Filter tasks for selected date
    selected_date_str = selected_date.strftime("%Y-%m-%d")
    today_tasks = [task for task in st.session_state.tasks if task["date"] == selected_date_str]

    if not today_tasks:
        st.info("No tasks for this day. Add some tasks in the sidebar! ✨")
    else:
        # Task list with improved styling
        st.markdown("### 📝 Your Tasks")
        for i, task in enumerate(today_tasks):
            task_col1, task_col2 = st.columns([0.9, 0.1])
            with task_col1:
                if task["completed"]:
                    st.markdown(f"~~{task['text']}~~")
                else:
                    st.markdown(f"**{task['text']}**")
            with task_col2:
                if task["completed"]:
                    if st.button("↩", key=f"uncomplete_{i}", help="Mark as incomplete"):
                        task["completed"] = False
                        save_tasks()
                        st.rerun()
                else:
                    if st.button("✓", key=f"complete_{i}", help="Mark as complete"):
                        task["completed"] = True
                        save_tasks()
                        st.rerun()

        # Add a clear completed tasks button
        if st.button("🗑️ Clear Completed Tasks"):
            st.session_state.tasks = [task for task in st.session_state.tasks 
                                    if not (task["date"] == selected_date_str and task["completed"])]
            save_tasks()
            st.rerun()

        # Display task statistics with improved styling
        completed_count = sum(1 for task in today_tasks if task["completed"])
        total_count = len(today_tasks)
        if total_count > 0:
            progress = completed_count / total_count
            st.progress(progress)
            st.markdown(f"**Progress:** {completed_count}/{total_count} tasks completed ({int(progress*100)}%)")

with col2:
    # Sidebar for adding new tasks and suggestions
    st.markdown("### ✨ Add New Task")
    
    # Handle input clearing
    if st.session_state.clear_input:
        st.session_state.clear_input = False
        st.session_state.new_task_input = ""
    
    new_task = st.text_input("Enter a new task:", key="new_task_input")
    
    # Handle Enter key press
    if st.button("➕ Add Task") or new_task and new_task.strip():
        if new_task:
            task = {
                "text": new_task,
                "completed": False,
                "date": datetime.now().strftime("%Y-%m-%d"),
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            st.session_state.tasks.append(task)
            save_tasks()
            st.success("Task added! ✨")
            # Set flag to clear input on next rerun
            st.session_state.clear_input = True
            st.rerun()

    # Task Suggestions with improved styling
    st.markdown("### 💡 Suggested Tasks")
    suggestions = get_suggestions(selected_date)
    
    for suggestion in suggestions:
        if st.button(f"➕ {suggestion['text']}", key=f"suggestion_{suggestion['text']}"):
            task = {
                "text": suggestion['text'],
                "completed": False,
                "date": selected_date_str,
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "suggestion_type": suggestion['type']
            }
            st.session_state.tasks.append(task)
            save_tasks()
            st.success("Suggested task added! ✨")
            st.rerun()

# Add a footer with instructions
st.markdown("---")
st.markdown("""
    <div style='text-align: center'>
        <p>💡 Tip: Press Enter to quickly add a task</p>
        <p>📱 Mobile-friendly: Works great on your phone!</p>
    </div>
""", unsafe_allow_html=True) 