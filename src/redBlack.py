from collections import deque


class Color:
    RED = "R"
    BLACK = "B"


class Node:
    def __init__(self, key, color=Color.RED, left=None, right=None, parent=None):
        self.key = key
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        # ANSI escape codes for colors
        RED = "\033[91m"  # Bright red
        BLACK = "\033[30m"  # Black
        RESET = "\033[0m"  # Reset to default color

        # Choose color based on node's color
        color_code = RED if self.color == Color.RED else BLACK
        return f"{color_code}{self.key}{RESET}"

    def __repr__(self):
        return str(self)


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(key=None, color=Color.BLACK)
        self.root = self.NIL

    def insert(self, key):
        new_node = Node(key, parent=self.NIL, left=self.NIL, right=self.NIL)
        self._insert_node(new_node)
        self._fix_insert(new_node)

    def _insert_node(self, node):
        y = self.NIL
        x = self.root
        while x != self.NIL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y == self.NIL:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

    def _fix_insert(self, k):
        while k.parent.color == Color.RED:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == Color.RED:
                    u.color = Color.BLACK
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    self._left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == Color.RED:
                    u.color = Color.BLACK
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    self._right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = Color.BLACK

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y


    def to_ascii(self):
        if self.root == self.NIL:
            return "Empty tree"

        # Helper function to calculate tree height
        def get_height(node):
            if node == self.NIL:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))

        height = get_height(self.root)
        width = 2**height - 1

        lines = []
        level = [self.root]

        while level and any(node != self.NIL for node in level):
            # Calculate padding for current level
            current_spacing = width // len(level)
            level_padding = "  " * int(2**height - len(level))
            level_str = level_padding

            next_level = []

            # Process each node in current level
            for node in level:
                if node != self.NIL:
                    level_str += str(node).center(current_spacing) + "  "
                    next_level.extend([node.left, node.right])
                else:
                    level_str += " " * current_spacing
                    next_level.extend([self.NIL, self.NIL])

            lines.append(level_str.center(width))
            level = next_level
            width //= 2

        return "\n".join(lines)


rbt = RedBlackTree()
#for key in ["C", "F", "D", "B", "A", "G", "E"]:
for key in ["EASYQUTION"]:
    rbt.insert(key)

print("ASCII representation of the tree:")
print(rbt.to_ascii())

#print("\nLevel-order traversal:", " ".join(level_order(rbt.root)))
#print("Pre-order traversal:", " ".join(pre_order(rbt.root)))
#print("In-order traversal:", " ".join(in_order(rbt.root)))
#print("Post-order traversal:", " ".join(post_order(rbt.root)))
