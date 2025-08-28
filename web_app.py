import streamlit
import functions

def add_todo():
    """Add a new todo from the input field."""
    if hasattr(streamlit.session_state, 'new_todo_key') and streamlit.session_state.new_todo_key.strip() != "":
        # Format the new todo with a bullet point and newline
        new_todo = f"▸ {streamlit.session_state.new_todo_key.strip().title()}\n"
        todos = functions.get_todos()
        todos.append(new_todo)
        functions.write_todos(todos)
        # Clear the input box
        streamlit.session_state.new_todo_key = ""

def remove_completed_todos():
    """Remove todos that have been checked off."""
    todos = functions.get_todos()
    # Get all todo items that are not checked
    updated_todos = [
        todo for i, todo in enumerate(todos)
        if not streamlit.session_state.get(f"todo_{i}", False)
    ]
    # Only update if there are changes
    if len(updated_todos) < len(todos):
        functions.write_todos(updated_todos)
        streamlit.rerun()

# Initialize the app
streamlit.title("My Todo App")

# Get todos from file
todos = functions.get_todos()

# Display checkboxes for each todo
for index, todo in enumerate(todos):
    if todo.strip() != "":
        streamlit.checkbox(
            todo.strip(),
            key=f"todo_{index}",
            value=False,
            on_change=remove_completed_todos
        )

# Add new todo input
streamlit.text_input(
    "",
    placeholder="Add a new todo...",
    on_change=add_todo,
    key="new_todo_key",
    label_visibility="collapsed"
)

# Add some spacing
streamlit.write("")
streamlit.caption("Click the checkbox to mark a todo as complete")


