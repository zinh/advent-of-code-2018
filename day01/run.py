f = open('input')
result = 0
for line in f:
    if line[0] == '+':
        result += int(line[1:])
    else:
        result -= int(line[1:])
f.close()
print(result)
