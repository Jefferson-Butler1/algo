from collections import deque


class Node:
    def __init__(self, key, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key

    def __str__(self):
        return f"[{self.left} {self.key} {self.right}]"

    def __repr__(self):
        return str(self)


t = Node("C", Node(key="F", left=Node("D")), Node("B", Node("A", Node("G"), Node("E"))))


def level_order(t):
    result = []
    if t:
        d = deque()
        d.append(t)
        while len(d):
            n = d.popleft()
            result.append(n.key)
            if n.left:
                d.append(n.left)
            if n.right:
                d.append(n.right)
    return result
def pre_order(t):
    result = []
    def f(n):
        if n:
            result.append(n.key)
            f(n.left)
            f(n.right)
    f(t)
    return result

def in_order(t):
    result = []
    def f(n):
        if n:
            f(n.left)
            result.append(n.key)
            f(n.right)
    f(t)
    return result

def post_order(t):
    result = []
    def f(n):
        if n:
            f(n.left)
            f(n.right)
            result.append(n.key)
    f(t)
    return result


print(t)
print(level_order(t))
print(pre_order(t))
print(in_order(t))
print(post_order(t))

