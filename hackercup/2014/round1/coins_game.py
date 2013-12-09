
def solve(line):
    n, k, c = (int(x) for x in line.split())
    result = None
    empty_jars = 0
    while n > 0:
        if k % n == 0:
            current_solution = c
        else:
            current_solution = (n - k % n) + c
        if result is None:
            result = current_solution
        else:
            result = min(result, empty_jars + current_solution)
        n -= 1
        empty_jars += 1
    return result

lines = open("in.txt", "r").readlines()
T = int(lines[0])
out = open("out.txt", "w")
for test in range(1, T+1):
    result = solve(lines[test].strip())
    out.write("Case #%s: %s\n" % (test, result))
out.close()
