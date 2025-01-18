import os
import sys
import json

TODO_FILE = "todo_list.json"

class TodoList:
    def __init__(self, filename=TODO_FILE):
        self.filename = filename
        self.todos = self.load_todos()
    

