## Goal

Build a small Python CLI called `tasks` that lets you:

```text
add a task
list tasks
complete a task
delete a task
```

The tasks should survive after the program closes.

Use:

- Python
- `argparse` for command-line commands
- `pathlib` and `json` for file I/O
- `dataclasses` for task objects
- `rich` as the pip-installed library
- `pytest` later for testing

Install the library inside a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install rich
```

## Suggested project structure

```text
daily_tasks/
    app.py
    task.py
    storage.py
    errors.py
    data/
        tasks.json
```

Start with one file if the structure feels overwhelming. Split the code only after the basic version works.

## Responsibilities

### `Task`

Represents one task.

Possible fields:

```text
id
title
completed
created_at
```

Questions to consider:

- Should task IDs be numbers or strings?
- What should happen if the title is empty?
- How will you represent completion?

### `TaskStorage`

Responsible for file I/O.

It should provide methods such as:

```text
load_tasks()
save_tasks(tasks)
```

Use JSON like:

```json
[
  {
    "id": 1,
    "title": "Read Python documentation",
    "completed": false
  }
]
```

Handle these cases:

- The file does not exist.
- The file is empty.
- The JSON is invalid.
- The program cannot write to the file.

Do not put file-reading code directly inside the CLI command handlers.

### `TaskManager`

Responsible for task operations:

```text
add_task(title)
list_tasks()
complete_task(task_id)
delete_task(task_id)
```

It should contain application rules, such as:

- A task must exist before it can be completed.
- A task title cannot be empty.
- IDs must be unique.

### `app.py`

Responsible for:

- Reading command-line arguments.
- Calling `TaskManager`.
- Printing results.
- Converting errors into friendly messages.

The CLI layer should not know how JSON is stored internally.

## Commands to implement

Your target interface could be:

```bash
python app.py add "Study Python classes"
python app.py list
python app.py complete 1
python app.py delete 1
```

Expected behavior:

```text
$ python app.py add "Study Python classes"
Task added: 1

$ python app.py list
[ ] 1 - Study Python classes

$ python app.py complete 1
Task completed: 1

$ python app.py list
[x] 1 - Study Python classes
```

## Build it in stages

### Stage 1: In-memory tasks

Create a `Task` class and temporarily store tasks in a Python list.

Your goal is to understand:

- Classes
- Objects
- Methods
- Lists
- Searching by ID

Do not add file storage yet.

### Stage 2: Add JSON persistence

Create `TaskStorage`.

The program should:

1. Load tasks when it starts.
2. Modify the list.
3. Save tasks before exiting.

Test it by closing the program and running it again.

The important question is:

> What evidence proves that persistence works?

The answer should be: a task created in one process is visible in a later process.

### Stage 3: Add error handling

Create custom exceptions:

```text
TaskNotFoundError
EmptyTaskTitleError
StorageError
```

Handle errors such as:

```bash
python app.py complete 999
python app.py add ""
```

The user should see:

```text
Error: task 999 does not exist.
```

They should not see an unexplained Python traceback during normal usage.

Do not catch every error with a broad `except Exception` and ignore it. Catch errors where you can explain or recover from them.

### Stage 4: Add `rich`

Use `rich` to make the task list easier to read.

For example:

- Completed tasks in a different color.
- A table for the task list.
- Clear success and error messages.

The library should improve presentation, not hide your core logic.

### Stage 5: Add tests

Test the manager and storage separately.

Important tests:

```text
adding a task creates an ID
empty titles are rejected
completing a task changes completed to true
completing an unknown task raises an error
saving and loading preserves tasks
invalid JSON produces a useful error
```

## Definition of done

Your first version is complete when:

- `add`, `list`, `complete`, and `delete` work.
- Tasks persist in a JSON file.
- The program uses classes.
- The program uses file I/O.
- Expected failures are handled clearly.
- At least one package installed with pip is used.
- The program is split into understandable responsibilities.
- You can explain what each class does without reading the code.

## Avoid these features initially

Do not add these until the basic version is reliable:

- Databases
- User accounts
- Web interfaces
- AI
- Due dates
- Recurring tasks
- Categories
- Synchronization
- Complex configuration files

They are not bad ideas. They simply increase the number of problems before you understand the first one.

## Your learning checkpoints

After each stage, answer these questions yourself:

1. What responsibility does each class own?
2. Where does the task data live?
3. What happens if the storage file is corrupted?
4. Which errors are expected user mistakes?
5. Which errors indicate a programming bug?
6. What would break if two tasks had the same ID?
7. How would you change the design if you later replaced JSON with SQLite?

A strong next step is to write the `Task` class and the four commands in plain English before coding them. Then implement only Stage 1 and test it manually.
