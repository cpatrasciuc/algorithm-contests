
def solve(test):
    low, high = 0, 1
    for i in range(len(test)):
        c = test[i]
        if c.isalpha():
            if c.isupper():
                print "Upper case letter: %s" % test
        elif c == ':' or c == ' ':
            pass
        elif c == '(':
            if i > 0 and test[i-1] == ':':
                high += 1
            else:
                low += 1
                high += 1
        elif c == ')':
            if i > 0 and test[i-1] == ':':
                low -= 1
            else:
                low -= 1
                high -= 1
            if low < 0 and high <= 0:
                return "NO"
        else:
            print "Invalid character: %s" % test
    if low <= 0 < high:
        return "YES"
    return "NO"

lines = open("in.txt", "r").readlines()
T = int(lines[0])
out = open("out.txt", "w")
for test in range(1, T+1):
    result = solve(lines[test].strip())
    out.write("Case #%s: %s\n" % (test, result))
out.close()
