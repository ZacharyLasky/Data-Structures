import sys
# from dll_queue import Queue
# from dll_stack import Stack


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
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each data
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, data):
        pass

    # Print the value of every data, starting with the given data,
    # in an iterative breadth first traversal
    def bft_print(self, data):
        pass

    # Print the value of every data, starting with the given data,
    # in an iterative depth first traversal
    def dft_print(self, data):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, data):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, data):
        pass
