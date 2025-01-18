import os
import sys
import json

TODO_FILE = "todo_list.json"

class TodoList:
    def __init__(self, filename=TODO_FILE):
        self.filename = filename
        self.todos = self.load_todos()
    # loading the json file
    def load_todos(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []
    # save todos
    def save_todos(self):
        with open(self.filename) as file:
            json.dump(self.todos, file, indent=4)
    # adding todos
    def add_todos(self, item):
        self.todos.append(item)
        self.save_todos()
    # list todos
    def list_todos(self):
        for idx, item in enumerate(self.todos, start=1):
            print(f"{idx}. {item}")
    # removing todos
    def remove_todos(self, index):
        try:
            removed_item = self.todos.pop(index - 1)
            self.save_todos()
            print(f"Deleted, {removed_item}")
        except IndexError:
            print("Invalid number")
    
def print_usage():
    print("Usage:")
    print("  python todo.py add [item]       Add a new todo item")
    print("  python todo.py list             List all todo items")
    print("  python todo.py remove [index]   Remove a todo item by index")