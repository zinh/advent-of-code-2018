from linked_list import LinkedList

def read_input(file_name):
    with open(file_name) as f:
        data = f.read()
        return list(data)

# List of char
def process(data):
    lst = LinkedList(data)
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

def select_unit():
    lst = read_input('input.txt')
    result = []
    for i in range(ord('a'), ord('z')):
        c = chr(i)
        upper_c = chr(i - 32)
        filtered = list(filter(lambda x: x != c and x != upper_c, lst))
        l = len(process(filtered))
        result.append([c, l])
    result.sort(key=lambda x: x[1])
    return result

print(select_unit())
