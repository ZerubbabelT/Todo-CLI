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
            json.dump(self.filename, file, indent=4)
    # adding todos
    def add_todos(self, item):
        self.filename.append(item)
        self.save_todos() 