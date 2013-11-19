def solve(grid):
    R = len(grid)
    C = len(grid[0])
    result = [[grid[x][y] for y in range(C)] for x in range(R)]
    for x in range(R):
        for y in range(C):
            if result[x][y] == '#':
                if x > R - 2 or y > C - 2:
                    return "\nImpossible"
                if result[x + 1][y] != "#" or result[x + 1][y + 1] != "#" or result[x][y + 1] != "#":
                    return "\nImpossible"
                result[x][y] = "/"
                result[x][y + 1] = "\\"
                result[x + 1][y] = "\\"
                result[x + 1][y + 1] = "/"
    return "\n%s" % "\n".join("".join(line) for line in result)

f = open("in.txt", "r")
T = int(f.readline())
out = open("out.txt", "w")
for test in range(1, T+1):
    R, C = (int(x) for x in f.readline().split())
    grid = []
    for _ in range(R):
        grid.append(f.readline().strip())
    result = solve(grid)
    out.write("Case #%s: %s\n" % (test, result))
out.close()