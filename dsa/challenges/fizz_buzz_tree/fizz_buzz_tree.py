from collections import deque

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:

    def __init__(self):
        self.root = None

    def add(self, value):
        """ This is the default add method that will add nodes to a tree with Breadth First logic
        """
        new_node = Node(value)
        breadth = Queue()
        breadth.enqueue(self.root)

        if not self.root:
            self.root = new_node
            return

        while not breadth.is_empty():
            front = breadth.dequeue()

            if not front.left:
                front.left = new_node
                return
            elif not front.right:
                front.right = new_node
                return

            if front.left:
                breadth.enqueue(front.left)

            if front.right:
                breadth.enqueue(front.right)

    def pre_order(self):
        """This is a Depth First traversal method. It prioritizes printing the `root` first, then looks to print `left` if left is not `None`, and lastly looks `right`."""
        collection = []

        def walk(root):
            if not root:
                return

            # <<< root >>>
            collection.append(root.value)

            # <<< left
            walk(root.left)

            # right >>>
            walk(root.right)

        # end
        walk(self.root)

        return collection

    def in_order(self):
        """This is a Depth First traversal method. It prioritizes printing the `left` first, then prints the `root`, and lastly looks to print `right`."""
        collection = []

        def walk(root):
            if not root:
                return

            # <<< left
            if root.left == None and root.right == None:
                collection.append(root.value)
                return
            else:
                walk(root.left)

            # <<< root >>>
            collection.append(root.value)

            # right >>>
            if root.left == None and root.right == None:
                collection.append(root.value)
                return
            else:
                walk(root.right)

        # Invoke
        walk(self.root)

        return collection

    def post_order(self):

        """This is a Depth First traversal method. It prioritizes print the `left` first, then looks to print the `right` and lastly prints the `root`."""
        collection = []

        def walk(root):
            if not root:
                return

            # <<< left
            if root.left == None and root.right == None:
                collection.append(root.value)
                return
            else:
                walk(root.left)


            # right >>>
            if root.left == None and root.right == None:
                collection.append(root.value)
                return
            else:
                walk(root.right)

            # <<< root >>>
            collection.append(root.value)

        # Invoke
        walk(self.root)

        return collection

    def breadth_first(self):
        """ This is a Breadth first traversal method that iterates through the tree by going through each level of the tree node by node.
        """
        collection = []
        breadth = Queue()
        breadth.enqueue(self.root)

        while not breadth.is_empty():
            front = breadth.dequeue()
            collection.append(front.value)

            if front.left:
                breadth.enqueue(front.left)

            if front.right:
                breadth.enqueue(front.right)

        return collection

class Queue:
    def __init__(self):
        self.storage = deque()

    def enqueue(self, value):
        """Takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time Performance."""
        self.storage.appendleft(value)

    def dequeue(self):
        """Takes no arguments, remove the node from the front of the queue, and returns the node's value."""
        return self.storage.pop()

    def peek(self):
        """Takes no arguments and returns the value of the node located in the front of the queue, without removing it from the queue."""
        return self.storage[-1]

    def is_empty(self):
        """Takes no arguments and returns a boolean indicating whether or not the queue is empty."""
        return len(self.storage) == 0

def fizz_buzz_tree(tree):
    """Takes in a tree as a single argument. Changes values throughout the tree based on Fizzbuzz logic, and returns a new tree in the same order and structure.
    """
    collection = tree.breadth_first()
    new_collection = []

    for i in collection:
        if i % 3 == 0 and i % 5 == 0:
            i = 'FizzBuzz'
            new_collection.append(i)
        elif i % 3 == 0:
            i = 'Fizz'
            new_collection.append(i)
        elif i % 5 == 0:
            i = 'Buzz'
            new_collection.append(i)
        else:
            i = str(i)
            new_collection.append(i)

    new_tree = BinaryTree()

    for i in new_collection:
        new_tree.add(i)

    return new_tree
