import sys
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.storage = DoublyLinkedList()
        self.size = 0
        # Why is our DLL a good choice to store our elements?

        # You can iterate forwards and backwards through a DLL. The tradeoff is that it uses more memory than a SLL.

        # self.storage = ?

    def enqueue(self, value):
        self.size += 1
        return self.storage.add_to_head(value)

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_tail()

    def len(self):
        return len(self.storage)
