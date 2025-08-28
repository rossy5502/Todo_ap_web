import os

FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    if not os.path.exists(filepath):
        with open(filepath, "w", encoding='utf-8') as file:
            pass
        return []
    
    try:
        with open(filepath, "r", encoding='utf-8') as file:
            return file.readlines()
    except UnicodeDecodeError:
        # Fallback in case the file has a different encoding
        with open(filepath, "r", encoding='latin-1') as file:
            return file.readlines()




def write_todos(todos_list, filepath=FILEPATH):
    with open(filepath, 'w', encoding='utf-8') as file:
        file.writelines(todos_list)
