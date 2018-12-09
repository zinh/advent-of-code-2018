class Node:
    def __init__(self, val, succ = None, pre = None):
        self.val = val
        self.succ = succ
        self.pre = pre

class LinkedList:
    def __init__(self, val):
        node = Node(val)
        node.succ = node
        node.pre = node
        self.root = node

    def __repr__(self):
        pointer = self.root
        s = f"[{pointer.val}]"
        pre = pointer.pre
        while pointer is not pre:
            pointer = pointer.succ
            s += (" " + str(pointer.val))
        return s

    # Insert pos step from root
    # pos >= 0: clockwise
    # pos < 0: counter-clockwise
    def insert(self, pos, val):
        while pos != 0:
            if pos > 0:
                self.root = self.root.succ
                pos -= 1
            else:
                self.root = self.root.pre
                pos += 1
        succ = self.root.succ
        node = Node(val, self.root.succ, self.root)
        self.root.succ = node
        succ.pre = node
        self.root = node

    def delete(self, pos):
        while pos != 0:
            if pos > 0:
                self.root = self.root.succ
                pos -= 1
            else:
                self.root = self.root.pre
                pos += 1
        val = self.root.val
        pre = self.root.pre
        succ = self.root.succ
        pre.succ = succ
        succ.pre = pre
        self.root = succ
        return val
