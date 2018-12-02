def letter_count(input):
    h = {}
    for c in input:
        if c in h:
            h[c] += 1
        else:
            h[c] = 1
    return h

f = open('input')
count2 = 0
count3 = 0

for line in f:
    count = letter_count(line)
    for k, v in count.items():
        if v == 2:
            count2 += 1
            break
    for k, v in count.items():
        if v == 3:
            count3 += 1
            break
f.close()
print(count2 * count3)
