import sys
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        super(DoublyLinkedList)
        self.size = 0
        # Why is our DLL a good choice to store our elements?

        # You can iterate forwards and backwards through a DLL. The tradeoff is that it uses more memory than a SLL.

        # self.storage = ?

    def enqueue(self, value):
        DoublyLinkedList.add_to_tail(self, value)

    def dequeue(self):
        DoublyLinkedList.remove_from_head(self)

    def len(self):
        return DoublyLinkedList(self).length
