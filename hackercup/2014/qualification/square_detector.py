
def solve(board):
    min_x = 100000
    max_x = -1
    min_y = 100000
    max_y = -1
    empty = True
    for (x, line) in enumerate(board):
        for (y, cell) in enumerate(line):
            if cell == "#":
                empty = False
                min_x = min(x, min_x)
                max_x = max(x, max_x)
                min_y = min(y, min_y)
                max_y = max(y, max_y)
    if empty:
        return "NO"
    if max_x - min_x != max_y - min_y:
        return "NO"
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if board[x][y] != "#":
                return "NO"
    return "YES"


lines = open("in.txt", "r").readlines()
T = int(lines[0])
idx = 1
out = open("out.txt", "w")
for test in range(1, T+1):
    N = int(lines[idx])
    idx += 1
    board = [line.strip() for line in lines[idx:idx+N]]
    idx += N
    result = solve(board)
    out.write("Case #%s: %s\n" % (test, result))
out.close()
