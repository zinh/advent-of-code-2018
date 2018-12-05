from linked_list import LinkedList

def read_input(file_name):
    with open(file_name) as f:
        data = f.read()
        return LinkedList(list(data))

# List of char
def process(lst):
    pointer = lst.head
    while pointer.next is not None:
        #print(pointer.val, list(lst))
        next_char = pointer.next.val
        current_char = pointer.val
        if reversed_sign(next_char, current_char):
            prev = pointer.prev
            nxt = pointer.next.next
            if prev is None:
                pointer = nxt
                nxt.prev = None
                lst.head = nxt
            elif nxt is None:
                prev.next = None
                pointer = prev
            else:
                prev.next = nxt
                nxt.prev = prev
                pointer = prev
        else:
            pointer = pointer.next
    return list(lst)

def reversed_sign(c1, c2):
    return abs(ord(c1) - ord(c2)) == 32

print(len(process(read_input('input.txt'))))
