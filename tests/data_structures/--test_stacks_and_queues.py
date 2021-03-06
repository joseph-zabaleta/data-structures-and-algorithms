import pytest
from dsa.data_structures.stack_and_queues.stacks_and_queues import (
    LinkedList,
    Node,
    Stack,
    Queue,
)


def test_LinkedList_exists():
    assert LinkedList()


def test_Node_exists():
    assert Node("test")


# Stack Tests
def test_Stack_exists():
    assert Stack()


def test_Stack_push_one_item():
    my_stack = Stack()
    my_stack.push(1)
    actual = my_stack.peek()
    expected = 1
    assert actual == expected


def test_Stack_push_multiple_items():
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    actual = my_stack.peek()
    expected = 3
    assert actual == expected


def test_Stack_pop_empty_Exception():
    with pytest.raises(AttributeError):
        my_stack = Stack()
        actual = my_stack.pop()
        expected = "Can't pop item from an empty stack"
        assert actual == expected


def test_Stack_pop_one_item():
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    actual = my_stack.pop()
    expected = 3
    assert actual == expected


def test_Stack_pop_multiple_items():
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    my_stack.pop()
    actual = my_stack.pop()
    expected = 2
    assert actual == expected


def test_Stack_peek_empty_Exception():
    with pytest.raises(AttributeError):
        my_stack = Stack()
        actual = my_stack.peek()
        expected = "Can't peek top from an empty stack"
        assert actual == expected


def test_Stack_peek_top():
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    actual = my_stack.peek()
    expected = 3
    assert actual == expected


def test_Stack_isEmpty_empty():
    my_stack = Stack()
    actual = my_stack.is_empty()
    expected = True
    assert actual == expected


def test_Stack_isEmpty_not_empty():
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    actual = my_stack.is_empty()
    expected = False
    assert actual == expected


# Queue Tests
def test_Queue_exists():
    assert Queue()


def test_Queue_enqueue_one_item():
    my_queue = Queue()
    my_queue.enqueue(1)
    actual = my_queue.peek()
    expected = 1
    assert actual == expected


def test_Queue_enqueue_multiple_items():
    my_queue = Queue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    actual = my_queue.peek()
    expected = 1
    assert actual == expected


def test_Queue_dequeue_one_item():
    my_queue = Queue()
    my_queue.enqueue(1)
    actual = my_queue.dequeue()
    expected = 1
    assert actual == expected


def test_Queue_dequeue_multiple_items():
    my_queue = Queue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.dequeue()
    actual = my_queue.dequeue()
    expected = 2
    assert actual == expected


def test_Queue_peek_front():
    my_queue = Queue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    actual = my_queue.peek()
    expected = 1
    assert actual == expected


def test_Queue_peek_empty_Exception():
    with pytest.raises(AttributeError):
        my_queue = Queue()
        actual = my_queue.peek()
        expected = "Can't peek front from an empty queue"
        assert actual == expected


def test_Queue_isEmpty_empty():
    my_queue = Queue()
    actual = my_queue.is_empty()
    expected = True
    assert actual == expected


def test_Queue_isEmpty_not_empty():
    my_queue = Queue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    actual = my_queue.is_empty()
    expected = False
    assert actual == expected
