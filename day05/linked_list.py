# Double linked list

class Node:
    def __init__(self, val, prevNode=None, nextNode=None):
        self.val = val
        self.next = nextNode
        self.prev = prevNode

class LinkedList:
    def __init__(self, arr):
        head = Node(arr[0])
        pointer = head
        for item in arr[1:]:
            node = Node(item, prevNode=pointer)
            pointer.next = node
            pointer = node
        self.head = head

    def __iter__(self):
        self.pointer = self.head
        return self

    def __next__(self):
        if self.pointer is None:
            raise StopIteration
        val = self.pointer.val
        self.pointer = self.pointer.next
        return val


