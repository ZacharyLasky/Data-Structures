import sys
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, data):
        if self.value == data:
            return False
        elif data < self.value:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = BinarySearchTree(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = BinarySearchTree(data)
                return True

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value and self.left:
            return self.left.contains(target)
        elif target > self.value and self.right:
            return self.right.contains(target)
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        # if right exists, go right
        # else return self.value
        if self.right:
            return max(self.right)
        else:
            return self.value

    # Call the function `cb` on the value of each data
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
# Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # queue root, if left add left to back if right add right to back.

    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        # While not empty
        while queue.size > 0:
            current = queue.dequeue()
            print(current.value)
            # Children to queue
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        stack = ()
        stack.push(node)
        # While not empty
        while stack.size > 0:
            current = stack.pop()
            print(current.value)
            if current.left:
                stack.push(current.left)
            if current.right:
                stack.push(current.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, data):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, data):
        pass
