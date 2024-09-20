class Node:
    def __init__(self, item=None, prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.head.next = self.head
        self.head.prev = self.head
    
    def __repr__(self) -> str:
        if not self.head.next:
            # impossible case, init sets it to a self referencing node
            return "<>"

        curr: Node = self.head.next
        builder = "<"
        while curr != self.head:
            builder += str(curr.item) + ", "
            curr = curr.next
        return builder + ">"

    def add_front(self, val):
        new = Node(item = val, prev = self.head, next = self.head.next)
        if not (self.head.next and new.next):
            # impossible case, init sets new nodes as self referencing 
            return None
        self.head.next = new
        new.next.prev = new



