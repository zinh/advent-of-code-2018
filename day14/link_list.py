import pdb

def digits(n):
    if n == 0:
        return [0]
    results = []
    while n != 0:
        results.append(n % 10)
        n = n // 10
    return results[::-1]

class Node:
    def __init__(self, val, succ = None, prev = None):
        self.val = val
        self.succ = succ
        self.prev = prev

    def __repr__(self):
        return str(self.val)

    def __str__(self):
        return str(self.val)

class LinkList:
    def __init__(self):
        self.head = Node(3)
        self.tail = Node(7, self.head, self.head)
        self.head.succ = self.tail
        self.head.prev = self.tail
        self.pointers = [self.head, self.tail]
        self.total_recipes = 2

    def insert(self, val):
        node = Node(val, self.head, self.tail)
        self.tail.succ = node
        self.head.prev = node
        self.tail = node
        self.total_recipes += 1

    def create_recipes(self, pattern):
        #pdb.set_trace()
        val = sum([pointer.val for pointer in self.pointers])
        ds = digits(val)
        for d in ds:
            self.insert(d)
            if self.grep_tail(len(pattern)) == pattern:
                #pdb.set_trace()
                return True
        return False

    def move_pointers(self):
        new_pointers = []
        for pointer in self.pointers:
            step = pointer.val + 1
            while step > 0:
                pointer = pointer.succ
                step -= 1
            new_pointers.append(pointer)
        self.pointers = new_pointers

    def get_tail(self, ignore):
        p = self.head
        while ignore > 0:
            p = p.succ
            ignore -= 1
        result = []
        while p != self.head:
            result.append(p.val)
            p = p.succ
        return result

    def grep_tail(self, n):
        result = []
        p = self.tail
        while n > 0:
            result.append(str(p.val))
            p = p.prev
            n -= 1
        return ''.join(result[::-1])


    def to_s(self):
        p = self.head.succ
        s = str(self.head.val) + ' '
        while p != self.head:
            s += (str(p.val) + ' ')
            p = p.succ
        return s

    def count_node_from_tail(self, c):
        p = self.tail
        while c > 0:
            p = p.prev
            c -= 1
        h = self.head
        step = 1
        while h != p:
            h = h.succ
            step += 1
        return step

    def __repr__(self):
        return self.to_s()

    def __str__(self):
        return self.to_s()

def run(max_loop):
    lst = LinkList()
    while lst.total_recipes < max_loop:
        lst.create_recipes()
        lst.move_pointers()
    return lst

def run2(pattern):
    lst = LinkList()
    while not lst.create_recipes(pattern):
        lst.move_pointers()
        #print(lst)
    return lst.count_node_from_tail(len(pattern))

print(run2('503761'))
