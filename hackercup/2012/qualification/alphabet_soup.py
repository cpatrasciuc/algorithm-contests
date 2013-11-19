
def solve(line):
    count = [0 for x in range(ord('A'), ord('Z') + 1)]
    for c in line:
        if c == " ":
            continue
        count[ord(c) - ord('A')] += 1
    count[ord('C') - ord('A')] /= 2
    print count
    return min(count[ord(c) - ord('A')] for c in "HACKERUP")

lines = open("in.txt", "r").readlines()
T = int(lines[0])
out = open("out.txt", "w")
for test in range(1, T+1):
    result = solve(lines[test].strip())
    out.write("Case #%s: %s\n" % (test + 1, result))
out.close()
