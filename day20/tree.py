class Node:
    def __init__(self, value, succ = None):
        self.value = value
        self.succ = succ

class SyntaxTree:
    def __init__(self):
        pass

    def from_array(self, arr):
        for c in arr:
            if c == '(':
                pass
