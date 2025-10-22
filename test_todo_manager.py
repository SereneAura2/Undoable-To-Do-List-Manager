"""
Test Suite for Undoable To-Do List Manager
Author: Rhamseys Garcia
Date: 10/21/25

This script contains various test scenarios to verify the functionality
of the ToDoManager class including edge cases.
"""

from todo_manager import ToDoManager


def test_basic_operations():
    """Test basic add and remove operations."""
    print("="*50)
    print("Test 1: Basic Add and Remove Operations")
    print("="*50)
    
    mgr=ToDoManager()
    
    # Add some tasks
    mgr.add("Buy milk")
    mgr.add("Write report")
    mgr.add("Call dentist")
    
    print("After adding three tasks:")
    mgr.print_tasks()
    
    # Remove a task
    mgr.remove("Buy milk")
    
    print("\nAfter removing 'Buy milk':")
    mgr.print_tasks()
    
    print("\n")


def test_undo_operations():
    """Test undo functionality."""
    print("="*50)
    print("Test 2: Undo Operations")
    print("="*50)
    
    mgr=ToDoManager()
    
    # Add tasks
    mgr.add("Buy milk")
    mgr.add("Write report")
    mgr.add("Call dentist")
    
    print("Current tasks:")
    mgr.print_tasks()
    
    # Undo last operation
    print("\nUndoing last operation (add 'Call dentist')...")
    mgr.undo(1)
    mgr.print_tasks()
    
    # Undo another operation
    print("\nUndoing one more operation (add 'Write report')...")
    mgr.undo(1)
    mgr.print_tasks()
    
    print("\n")


def test_undo_remove():
    """Test undoing a remove operation."""
    print("="*50)
    print("Test 3: Undo Remove Operation")
    print("="*50)
    
    mgr=ToDoManager()
    
    mgr.add("Buy milk")
    mgr.add("Write report")
    mgr.remove("Buy milk")
    
    print("After adding two tasks and removing 'Buy milk':")
    mgr.print_tasks()
    
    # Undo the remove operation
    print("\nUndoing the remove operation...")
    mgr.undo(1)
    mgr.print_tasks()
    
    print("\n")


def test_undo_beyond_history():
    """Test undoing more operations than exist in history."""
    print("="*50)
    print("Test 4: Undo Beyond History")
    print("="*50)
    
    mgr=ToDoManager()
    
    # Only add two tasks
    mgr.add("Buy milk")
    mgr.add("Write report")
    
    print("Current tasks:")
    mgr.print_tasks()
    
    # Try to undo 5 operations (more than we have)
    print("\nAttempting to undo 5 operations (only 2 exist)...")
    mgr.undo(5)
    mgr.print_tasks()
    
    print("\n")


def test_history_tracking():
    """Test that history correctly tracks all operations."""
    print("="*50)
    print("Test 5: History Tracking")
    print("="*50)
    
    mgr=ToDoManager()
    
    mgr.add("Buy milk")
    mgr.add("Write report")
    mgr.remove("Buy milk")
    mgr.add("Call dentist")
    mgr.undo(1)
    
    # History should show all operations even after undo
    mgr.print_history()
    
    print("\nCurrent tasks after all operations:")
    mgr.print_tasks()
    
    print("\n")


def test_remove_nonexistent():
    """Test removing a task that doesn't exist."""
    print("="*50)
    print("Test 6: Remove Nonexistent Task")
    print("="*50)
    
    mgr=ToDoManager()
    
    mgr.add("Buy milk")
    mgr.add("Write report")
    
    print("Current tasks:")
    mgr.print_tasks()
    
    # Try to remove a task that doesn't exist
    print("\nTrying to remove 'Call dentist' (doesn't exist)...")
    mgr.remove("Call dentist")
    
    print("Tasks unchanged:")
    mgr.print_tasks()
    
    # History should not record this operation
    print("\nHistory (should only show 2 add operations):")
    mgr.print_history()
    
    print("\n")


def test_complex_scenario():
    """Test a complex scenario with multiple operations and undos."""
    print("="*50)
    print("Test 7: Complex Scenario")
    print("="*50)
    
    mgr=ToDoManager()
    
    # Perform various operations
    mgr.add("Task 1")
    mgr.add("Task 2")
    mgr.add("Task 3")
    print("After adding 3 tasks:")
    mgr.print_tasks()
    
    mgr.remove("Task 2")
    print("\nAfter removing Task 2:")
    mgr.print_tasks()
    
    mgr.add("Task 4")
    print("\nAfter adding Task 4:")
    mgr.print_tasks()
    
    # Undo last 2 operations
    print("\nUndoing last 2 operations...")
    mgr.undo(2)
    mgr.print_tasks()
    
    print("\nFull operation history:")
    mgr.print_history()
    
    print("\n")


def test_empty_manager():
    """Test operations on an empty manager."""
    print("="*50)
    print("Test 8: Empty Manager")
    print("="*50)
    
    mgr=ToDoManager()
    
    print("Trying to undo on empty manager...")
    mgr.undo(1)
    
    print("\nCurrent tasks (should be empty):")
    mgr.print_tasks()
    
    print("\nHistory (should be empty):")
    mgr.print_history()
    
    print("\n")


def run_all_tests():
    """Run all test cases."""
    print("\n")
    print("#"*50)
    print("# TESTING UNDOABLE TO-DO LIST MANAGER")
    print("# Author: Rhamseys Garcia")
    print("# Date: 10/21/25")
    print("#"*50)
    print("\n")
    
    test_basic_operations()
    test_undo_operations()
    test_undo_remove()
    test_undo_beyond_history()
    test_history_tracking()
    test_remove_nonexistent()
    test_complex_scenario()
    test_empty_manager()
    
    print("="*50)
    print("ALL TESTS COMPLETED")
    print("="*50)


if __name__=="__main__":
    run_all_tests()

