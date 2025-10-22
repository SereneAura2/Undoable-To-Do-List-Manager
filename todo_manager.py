"""
Undoable To-Do List Manager
Author: Rhamseys Garcia
Date: 10/21/25

This module implements a to-do list manager with undo functionality
using a stack for undo operations and a linked list for history tracking.
"""

from typing import List, Optional


class Operation:
    """
    Represents a single operation (add or remove) that can be undone.
    
    Attributes:
        kind (str): Type of operation - either "add" or "remove"
        task (str): The task description
    """
    
    def __init__(self, kind: str, task: str):
        """Initialize an operation with its type and task description."""
        self.kind=kind
        self.task=task
    
    def undo(self, todo_manager):
        """
        Reverse this operation on the given ToDoManager.
        
        Args:
            todo_manager: The ToDoManager instance to perform undo on
        """
        # If the operation was "add", we need to remove it
        if self.kind=="add":
            if self.task in todo_manager.tasks:
                todo_manager.tasks.remove(self.task)
        # If the operation was "remove", we need to add it back
        elif self.kind=="remove":
            todo_manager.tasks.append(self.task)


class HistoryNode:
    """
    Node in the history linked list.
    Each node stores an operation and points to the next node.
    
    Attributes:
        operation (Operation): The operation stored in this node
        next (HistoryNode | None): Reference to the next node in the list
    """
    
    def __init__(self, operation: Operation):
        """Initialize a history node with an operation."""
        self.operation=operation
        self.next=None


class StackNode:
    """
    Node in the undo stack.
    Each node stores an operation and points to the next node.
    
    Attributes:
        operation (Operation): The operation stored in this node
        next (StackNode | None): Reference to the next node in the stack
    """
    
    def __init__(self, operation: Operation):
        """Initialize a stack node with an operation."""
        self.operation=operation
        self.next=None


class ToDoManager:
    """
    Main to-do list manager with undo functionality.
    
    Attributes:
        tasks (List[str]): Current list of active tasks
        history_head (HistoryNode | None): Head of the history linked list
        history_tail (HistoryNode | None): Tail of the history linked list
        undo_stack_top (StackNode | None): Top of the undo stack
    """
    
    def __init__(self):
        """Initialize an empty to-do manager."""
        self.tasks=[]
        self.history_head=None
        self.history_tail=None
        self.undo_stack_top=None
    
    def add(self, task: str):
        """
        Add a new task to the to-do list.
        
        Args:
            task (str): The task description to add
        """
        # Add the task to our current tasks list
        self.tasks.append(task)
        
        # Create an operation record
        operation=Operation("add", task)
        
        # Add to history linked list
        self._append_to_history(operation)
        
        # Push onto undo stack
        self._push_to_stack(operation)
    
    def remove(self, task: str):
        """
        Remove a task from the to-do list.
        
        Args:
            task (str): The task description to remove
        """
        # Only proceed if the task exists in our list
        if task in self.tasks:
            self.tasks.remove(task)
            
            # Create an operation record
            operation=Operation("remove", task)
            
            # Add to history linked list
            self._append_to_history(operation)
            
            # Push onto undo stack
            self._push_to_stack(operation)
    
    def undo(self, k: int):
        """
        Undo the last k operations.
        
        Args:
            k (int): Number of operations to undo
        """
        # Undo up to k operations or until stack is empty
        count=0
        while count<k and self.undo_stack_top is not None:
            # Pop the top operation from the stack
            operation=self.undo_stack_top.operation
            self.undo_stack_top=self.undo_stack_top.next
            
            # Execute the undo operation
            operation.undo(self)
            
            count+=1
    
    def print_history(self):
        """Print the full history of all operations in chronological order."""
        print("Full History:")
        
        # Traverse the history linked list from head to tail
        current=self.history_head
        if current is None:
            print("  No operations yet")
            return
        
        while current is not None:
            # Print each operation in format: "kind: task"
            print(f"  {current.operation.kind}: {current.operation.task}")
            current=current.next
    
    def print_tasks(self):
        """Print the current list of tasks."""
        print("Current tasks:", self.tasks)
    
    def _append_to_history(self, operation: Operation):
        """
        Internal helper to append an operation to the history linked list.
        
        Args:
            operation (Operation): The operation to append
        """
        new_node=HistoryNode(operation)
        
        # If history is empty, this is both head and tail
        if self.history_head is None:
            self.history_head=new_node
            self.history_tail=new_node
        else:
            # Append to the end of the list
            self.history_tail.next=new_node
            self.history_tail=new_node
    
    def _push_to_stack(self, operation: Operation):
        """
        Internal helper to push an operation onto the undo stack.
        
        Args:
            operation (Operation): The operation to push
        """
        new_node=StackNode(operation)
        
        # Push onto the top of the stack
        new_node.next=self.undo_stack_top
        self.undo_stack_top=new_node

