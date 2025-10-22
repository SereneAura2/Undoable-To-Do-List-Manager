# Undoable To-Do List Manager

**Author:** Rhamseys Garcia  
**Date:** 10/21/25

## Overview

This project implements a to-do list manager with full undo functionality. The implementation uses two key data structures:
- **Stack** for managing undo operations
- **Linked List** for tracking the complete operation history

## Design

### Classes

#### 1. `Operation`
Represents a single operation (add or remove) that can be undone.
- **Attributes:**
  - `kind`: Type of operation ("add" or "remove")
  - `task`: The task description
- **Methods:**
  - `undo(todo_manager)`: Reverses the operation

#### 2. `HistoryNode`
Node in the history linked list for chronological tracking.
- **Attributes:**
  - `operation`: The operation stored
  - `next`: Reference to next node

#### 3. `StackNode`
Node in the undo stack.
- **Attributes:**
  - `operation`: The operation stored
  - `next`: Reference to next node

#### 4. `ToDoManager`
Main manager class that coordinates all operations.
- **Attributes:**
  - `tasks`: Current list of active tasks
  - `history_head`: Head of history linked list
  - `history_tail`: Tail of history linked list
  - `undo_stack_top`: Top of undo stack
- **Methods:**
  - `add(task)`: Add a task
  - `remove(task)`: Remove a task
  - `undo(k)`: Undo last k operations
  - `print_history()`: Display full operation history
  - `print_tasks()`: Display current tasks

## How It Works

### Adding a Task
1. Task is appended to the current tasks list
2. An "add" operation is created
3. Operation is added to history linked list (for audit trail)
4. Operation is pushed onto undo stack (for potential undo)

### Removing a Task
1. Task is removed from current tasks list (if it exists)
2. A "remove" operation is created
3. Operation is added to history linked list
4. Operation is pushed onto undo stack

### Undoing Operations
1. Pop up to k operations from the undo stack
2. For each operation:
   - If it was an "add", remove the task
   - If it was a "remove", add the task back
3. History remains unchanged (operations are still recorded)

## Assumptions

1. **Duplicate Tasks:** The system allows duplicate task names. Each add/remove operates on one instance.
2. **Remove Nonexistent Task:** Attempting to remove a task that doesn't exist is silently ignored and not recorded in history.
3. **Undo Beyond History:** Undoing more operations than exist will undo all available operations without error.
4. **History Persistence:** The history linked list records all operations permanently, even after undo. This provides a complete audit trail.
5. **Undo Stack Modification:** When operations are undone, they are removed from the undo stack but remain in history.

## Limitations

1. **No Redo:** The current implementation doesn't support redoing undone operations.
2. **Memory Usage:** All operations remain in memory via the history linked list, which could grow large with many operations.
3. **No Persistence:** Tasks and history are not saved to disk; they exist only in memory during runtime.
4. **Single-Level Undo:** Each undo operation is atomic; you cannot undo parts of an operation.
5. **No Task Editing:** Tasks can only be added or removed, not modified.

## Files

- `todo_manager.py`: Main implementation with all classes
- `test_todo_manager.py`: Comprehensive test suite
- `README.md`: This documentation file

## Running the Tests

To run the test suite:

```bash
python test_todo_manager.py
```

## Example Usage

```python
from todo_manager import ToDoManager

# Create a new manager
mgr=ToDoManager()

# Add tasks
mgr.add("Buy milk")
mgr.add("Write report")

# Show current tasks
mgr.print_tasks()  # Output: Current tasks: ["Buy milk", "Write report"]

# Remove a task
mgr.remove("Buy milk")

# Undo the remove operation
mgr.undo(1)

# Show history
mgr.print_history()
# Output:
#   add: Buy milk
#   add: Write report
#   remove: Buy milk
```

## Time Complexity

- **add():** O(1) - appends to list, linked list, and stack
- **remove():** O(n) - needs to search for task in list
- **undo(k):** O(k) - pops k items from stack
- **print_history():** O(n) - traverses entire history linked list
- **print_tasks():** O(n) - prints all current tasks

## Space Complexity

O(n) where n is the total number of operations performed, as all operations are stored in both the history linked list and initially in the undo stack.

