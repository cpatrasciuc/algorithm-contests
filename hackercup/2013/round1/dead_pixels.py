nodes = []

class Node:
    def __init__(self):
        self.st = None
        self.dr = None
        self.count = 0
        self.left = None
        self.right = None

    def add(self, a, b):
        if self.left is None:
            self.count += 1
            if self.count == 1:
                return 1
            else:
                return 0
        else:
            mij = (self.st + self.dr) / 2
            added = 0
            if a <= mij:
                added += self.left.add(a, b)
            if b > mij:
                added += self.right.add(a, b)
            self.count += added
            return added

    def remove(self, a, b):
        if self.left is None:
            if self.count == 1:
                self.count = 0
                return 1
            else:
                self.count = max(0, self.count - 1)
                return 0
        else:
            mij = (self.st + self.dr) / 2
            removed = 0
            if a <= mij:
                removed += self.left.remove(a, b)
            if b > mij:
                removed += self.right.remove(a, b)
            self.count -= removed
            return removed

def buildInitialTree(a, b):
    node = Node()
    node.st = a
    node.dr = b
    if a == b:
        return node
    mij = (a + b) / 2
    node.left = buildInitialTree(a, mij)
    node.right = buildInitialTree(mij + 1, b)
    return node

def printTree(node):
    print "[%s %s]" % (node.st, node.dr)
    if node.left is not None:
        printTree(node.left)
        printTree(node.right)

def solve(test):
    W, H, P, Q, N, X, Y, a, b, c, d = (int(x) for x in test.split())
    x = [X]
    y = [Y]
    for i in range(1, N):
        x.append((x[i - 1] * a + y[i - 1] * b + 1) % W)
        y.append((x[i - 1] * c + y[i - 1] * d + 1) % H)

    events = []
    for i in range(N):
        events.append((max(0, x[i] - P + 1), "START", max(0, y[i] - Q + 1), min(H - Q, y[i])))
        events.append((min(x[i], W - P) + 1, "STOP", max(0, y[i] - Q + 1), min(H - Q, y[i])))
    events.sort(cmp=lambda x, y: x[0] - y[0])


    tree = buildInitialTree(0, H-1)
    total_area = 0
    old_x = None
    for i in range(len(events)):
        event = events[i]
        if old_x is not None and event[0] != old_x:
            total_area += tree.count * (event[0] - old_x)
        if event[1] == "START":
            tree.add(event[2], event[3])
        if event[1] == "STOP":
            tree.remove(event[2], event[3])
        old_x = event[0]
    return (W - P + 1) * (H - Q + 1) - total_area

lines = open("in.txt", "r").readlines()
T = int(lines[0])
out = open("out2.txt", "w")
for test in range(1, T+1):
    result = solve(lines[test].strip())
    out.write("Case #%s: %s\n" % (test, result))
out.close()
