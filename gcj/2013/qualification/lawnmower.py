
def solve(N, M, land):
    land = [[int(x) for x in line.split()] for line in land]
    for height in range(1, 101):
        for i in range(N):
            for j in range(M):
                if land[i][j] == height:
                    valid_line = True
                    for column in range(M):
                        if land[i][column] != land[i][j]:
                            valid_line = False
                            break
                    valid_column = True
                    for line in range(N):
                        if land[line][j] != land[i][j]:
                            valid_column = False
                            break
                    if (not valid_line) and (not valid_column):
                        return "NO"
        for i in range(N):
            for j in range(M):
                if land[i][j] == height:
                    land[i][j] += 1
    return "YES"

lines = open("in.txt", "r").readlines()
T = int(lines[0])
out = open("out.txt", "w")
index = 1
for test in range(1, T+1):
    N, M = tuple([int(x) for x in lines[index].strip().split()])
    land = [lines[index + i].strip() for i in range(1, N+1)]
    result = solve(N, M, land)
    out.write("Case #%s: %s\n" % (test, result))
    index += N + 1
out.close()

