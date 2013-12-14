import Queue
import sys

FROM_TOP = 1
FROM_LEFT = (1 << 1)


class Solver:
    def __init__(self, N, M, board):
        self.N = N
        self.M = M
        self.board = board
        self.visited = [[0 for y in range(M)] for x in range(N)]
        self.distances = [[None for y in range(M)] for x in range(N)]

    def get_directions(self):
        q = Queue.Queue()
        self.visited[0][0] = FROM_TOP | FROM_LEFT
        q.put((0, 0))
        while not q.empty():
            x, y = q.get()
            if x + 1 < self.N and self.board[x + 1][y] == ".":
                if self.visited[x + 1][y] == 0:
                    q.put((x + 1, y))
                self.visited[x + 1][y] |= FROM_TOP
            if y + 1 < self.M and self.board[x][y + 1] == ".":
                if self.visited[x][y + 1] == 0:
                    q.put((x, y + 1))
                self.visited[x][y + 1] |= FROM_LEFT

    def get_distances(self, x, y):
        if x >= self.N:
            return 0
        if y >= self.M:
            return 0
        if self.distances[x][y] is not None:
            return self.distances[x][y]
        if self.board[x][y] == "#":
            self.distances[x][y] = 0
            return 0
        self.distances[x][y] = 1 + max(self.get_distances(x + 1, y), self.get_distances(x, y + 1))
        return self.distances[x][y]

    def solve(self):
        self.get_directions()

        result = self.get_distances(0, 0)

        for x in range(self.N):
            y = self.M
            while y > 0:
                y -= 1
                if x == 0 and y == 0:
                    continue
                if self.visited[x][y] == 0:
                    continue
                if self.visited[x][y] & FROM_TOP:
                    y2 = y - 1
                    while y2 >= 0 and self.board[x][y2] == ".":
                        result = max(result, x + y + 1 + (y - y2) + self.get_distances(x + 1, y2))
                        if result == 23:
                            print x, y, y2
                        y2 -= 1
                    y = y2

        for y in range(self.M):
            x = self.N
            while x > 0:
                x -= 1
                if x == 0 and y == 0:
                    continue
                if self.visited[x][y] == 0:
                    continue
                if self.visited[x][y] & FROM_LEFT:
                    x2 = x - 1
                    while x2 >= 0 and self.board[x2][y] == ".":
                        result = max(result, x + y + 1 + (x - x2) + self.get_distances(x2, y + 1))
                        if result == 23:
                            print x, y, x2
                        x2 -= 1
                    x = x2
        return result


sys.setrecursionlimit(5000)
lines = open("in.txt", "r").readlines()
T = int(lines[0])
index = 1
out = open("out.txt", "w")
for test in range(1, T + 1):
    N, M = (int(x) for x in lines[index].strip().split())
    index += 1
    board = lines[index:index + N]
    index += N
    s = Solver(N, M, board)
    result = s.solve()
    out.write("Case #%s: %s\n" % (test, result))
out.close()