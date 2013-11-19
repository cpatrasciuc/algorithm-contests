def gcd(a, b):
    while b:
        c = b
        b = a % b
        a = c
    return a


def solve(line):
    N, PD, PG = tuple(int(x) for x in line.split())
    if PG == 0:
        if PD == 0:
            return "Possible"
        else:
            return "Broken"
    if PG == 100:
        if PD == 100:
            return "Possible"
        else:
            return "Broken"
    NumPD = 100 / gcd(PD, 100)
    if NumPD > N:
        return "Broken"
    return "Possible"

lines = open("in.txt", "r").readlines()
T = int(lines[0])
out = open("out.txt", "w")
for test in range(1, T+1):
    result = solve(lines[test].strip())
    out.write("Case #%s: %s\n" % (test, result))
out.close()
