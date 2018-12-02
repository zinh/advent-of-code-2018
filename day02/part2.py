def check_id(s, line):
    diff = 0
    for idx, c in enumerate(s):
        if line[idx] != c:
            diff += 1
    if diff != 1:
        return False
    return True
def run():
    passed = []
    with open('input') as f:
      for line in f:
          passed.append(line)
          for s in passed:
              if check_id(s, line):
                  return s, line
print(run())
