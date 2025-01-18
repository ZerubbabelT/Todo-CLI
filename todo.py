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