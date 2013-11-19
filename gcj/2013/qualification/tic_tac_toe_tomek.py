
def solve(board):
    for line in board:
        s = set(line)
        s.add('T')
        if s == set(['X', 'T']):
            return "X won"
        if s == set(['O', 'T']):
            return "O won"
    for column in range(4):
        s = set([line[column] for line in board])
        s.add('T')
        if s == set(['X', 'T']):
            return "X won"
        if s == set(['O', 'T']):
            return "O won"
    s = set([board[i][i] for i in range(4)])
    s.add('T')
    if s == set(['X', 'T']):
        return "X won"
    if s == set(['O', 'T']):
        return "O won"
    s = set([board[i][3-i] for i in range(4)])
    s.add('T')
    if s == set(['X', 'T']):
        return "X won"
    if s == set(['O', 'T']):
        return "O won"
    if "".join(board).find('.') >= 0:
        return "Game has not completed"
    return "Draw"

lines = open("in.txt", "r").readlines()
T = int(lines[0])
out = open("out.txt", "w")
index = 1
for test in range(1, T+1):
    result = solve([line.strip() for line in lines[index:index+4]])
    out.write("Case #%s: %s\n" % (test, result))
    assert len(lines[index+4].strip()) == 0, lines[index+4]
    index += 5
out.close()
