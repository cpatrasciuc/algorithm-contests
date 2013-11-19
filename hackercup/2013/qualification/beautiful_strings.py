
def solve(test):
    test = filter(lambda c: c.isalpha(), test.upper())
    count = [(0, chr(i)) for i in range(ord('A'), ord('Z') + 1)]
    for c in test:
        count[ord(c) - ord('A')] = (count[ord(c) - ord('A')][0] + 1, count[ord(c) - ord('A')][1])
    count.sort(reverse=True)
    total = 0
    value = 26
    for c, _ in count:
        total += value * c
        value -= 1
        if value == 0:
            break
    return total

lines = open("in.txt", "r").readlines()
T = int(lines[0])
out = open("out.txt", "w")
for test in range(1, T+1):
    result = solve(lines[test].strip())
    out.write("Case #%s: %s\n" % (test, result))
out.close()
