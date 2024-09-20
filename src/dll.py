class Node:
    def __init__(self, item=None, prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next

    def __repr__(self):
        return str(self.item)


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.head.next = self.head
        self.head.prev = self.head

    def __repr__(self) -> str:
        values = []
        curr = self.head.next
        while curr != self.head:
            values.append(str(curr.item))
            curr = curr.next
        return "<" + ", ".join(values) + ">"

    def str_reverse(self):
        values = []
        curr = self.head.prev
        while curr != self.head:
            values.append(str(curr.item))
            curr = curr.prev
        return "<" + ", ".join(values) + ">"

    def add_back(self, val):
        new = Node(item=val, prev=self.head.prev, next=self.head)
        if not (self.head.prev and new.next):
            # impossible case, init sets new nodes as self referencing
            return None
        self.head.prev = new
        new.prev.next = new

    def add_front(self, val):
        new = Node(item=val, prev=self.head, next=self.head.next)
        if not (self.head.next and new.next):
            # impossible case, init sets new nodes as self referencing
            return None
        self.head.next = new
        new.next.prev = new

    def remove_back(self):
        target = self.head.prev
        if target == self.head:
            return None
        self.head.prev = self.head.prev.prev
        self.head.prev.next = self.head
        return target.item

    def remove_front(self):
        target = self.head.next
        if target == self.head:
            return None
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        return target.item

    def concatenate(self, more):
        next = more.remove_front()
        while next:
            self.add_back(next)
            next = more.remove_front()

    def reverse(self):
        curr = self.head
        curr.prev, curr.next = curr.next, curr.prev  # switch pointers
        curr = curr.prev  # goes to next
        while curr != self.head:
            curr.prev, curr.next = curr.next, curr.prev  # switch pointers
            curr = curr.prev  # goes to next

    def remove(self, target):
        curr = self.head.next
        while curr != self.head:
            print(target, curr)
            if curr.item == target:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
            curr = curr.next

