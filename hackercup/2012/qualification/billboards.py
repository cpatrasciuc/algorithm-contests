
def isGoodSize(size, width, height, phrase):
    words = phrase.split()
    lines = [[]]
    line_size = 0
    for i in range(len(words)):
        new_size = line_size
        if new_size > 0:
            new_size += size
        new_size += len(words[i]) * size
        if new_size <= width:
            lines[-1].append(words[i])
            line_size = new_size
        else:
            lines.append([words[i]])
            line_size = len(words[i]) * size
            if line_size > width:
                return False
    return len(lines) * size <= height

def solve(test):
    tokens = test.split()
    width, height = int(tokens[0]), int(tokens[1])
    phrase = " ".join(tokens[2:])
    if not isGoodSize(1, width, height, phrase):
        return 0
    low = 1
    high = 2
    while isGoodSize(high, width, height, phrase):
        high *= 2
    while low < high:
        middle = (low + high) / 2
        if isGoodSize(middle, width, height, phrase):
            low = middle + 1
        else:
            high = middle
    return low - 1

#print isGoodSize(20, 350, 100, "Facebook Hacker Cup 2013")
print isGoodSize(8, 100, 20, "Hack your way to the cup")

lines = open("in.txt", "r").readlines()
T = int(lines[0])
out = open("out.txt", "w")
for test in range(1, T+1):
    result = solve(lines[test].strip())
    out.write("Case #%s: %s\n" % (test, result))
out.close()

