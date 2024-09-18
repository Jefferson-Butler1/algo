class node:
    def __init__(self, val, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.val = val
    def setPrev(self, n):
        self.prev = n
    def setNext(self, n):
        self.next = n


class DoublyLinkedList:
    def __init__(self, vals=[]) -> None:
        self.head = node(None)
        self.tail = node(None, prev=self.head)
        self.head.setNext(self.tail)
        
