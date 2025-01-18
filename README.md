# Todo-CLI

A simple command-line interface (CLI) tool to manage your to-do list. This program allows users to add, list, and remove tasks conveniently using Python.

---

## Features

- **Add Tasks:** Add a new to-do task to your list.
- **List Tasks:** View all the tasks in your to-do list.
- **Remove Tasks:** Remove a specific task by its index.
- **Persistent Storage:** All tasks are saved to a JSON file for easy storage and retrieval.

---

## Requirements

- Python 3.6 or later

---

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Todo-CLI.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Todo-CLI
   ```
3. Ensure you have Python installed. Verify by running:
   ```bash
   python --version
   ```

---

## Usage

Run the `todo.py` script with the following commands:

### Add a Task

```bash
python todo.py add <task>
```

Example:

```bash
python todo.py add Buy groceries
```

### List All Tasks

```bash
python todo.py list
```

Example Output:

```
1. Buy groceries
2. Finish homework
```

### Remove a Task

```bash
python todo.py remove <index>
```

Example:

```bash
python todo.py remove 1
```

This removes the first task in the list.

---

## File Structure

```plaintext
Todo-CLI/
├── todo.py           # Main script for the Todo-CLI
├── todo_list.json    # JSON file to persist the to-do tasks
└── README.md         # Project documentation
```

---

## How It Works

1. When you add a task, it appends the task to the `todo_list.json` file.
2. Tasks can be viewed anytime using the `list` command.
3. To remove a task, use the `remove` command by providing the index of the task.

---

## Troubleshooting

### Common Errors

- **File Not Writable**: Ensure `todo_list.json` exists and is writable.
  - Solution: Delete the `todo_list.json` file and rerun the program to create a new one.
  - Ensure that todo\_list.json contains an empty list ([]) at initialization.

\
Happy Coding!

