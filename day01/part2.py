def change(s):
    if s[0] == '+':
        return int(s[1:])
    else:
        return -int(s[1:])

def run():
    with open('input') as f:
        content = f.read()
        lines = content.split("\n")
        result = 0
        h = {}
        while True:
            for line in lines[:-1]:
                result += change(line)
                if result in h:
                    return result
                else:
                    h[result] = 1

print(run())
