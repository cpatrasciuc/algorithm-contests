def solve(X, Y):
    line = 0
    col = 0
    step = 1
    result = ""
    while line != Y:
        print step
        line += step
        if step > 0:
            step = -(step + 1)
            result += 'N'
        else:
            step = -step + 1
            result += 'S'
    if X * step > 0:
        step = -step
    while col != X:
        print step
        col += step
        if step > 0:
            step = -(step + 1)
            result += 'E'
        else:
            step = -step + 1
            result += 'W'
    assert len(result) < 500
    return result

def dist(X, Y, tX, tY):
    return 2 * (abs(X - tX)) + 2 * abs(Y - tY)

def go(X, Y, targetX, targetY, step_size, r):
    #s = [dist(X, Y, targetX, targetY)]
    rs = [solve(X, Y)] #r + ("EW" * (abs(X - targetX))) + ("NS" * abs(Y - targetY))]
    s = [len(rs[0])]
    if abs(X + step_size - targetX) <= abs(X - targetX):
        c, nr = go(X + step_size, Y, targetX, targetY, step_size + 1, r + 'E')
        s.append(1 + c)
        rs.append(nr)
    if abs(X - step_size - targetX) <= abs(X - targetX):
        c, nr = go(X - step_size, Y, targetX, targetY, step_size + 1, r + 'W')
        s.append(1 + c)
        rs.append(nr)
    if abs(Y + step_size - targetY) <= abs(Y - targetY):
        c, nr = go(X, Y + step_size, targetX, targetY, step_size + 1, r + 'N')
        s.append(1 + c)
        rs.append(nr)
    if abs(Y - step_size - targetY) <= abs(Y - targetY):
        c, nr = go(X, Y - step_size, targetX, targetY, step_size + 1, r + 'S')
        s.append(1 + c)
        rs.append(nr)
    m = min(s)
    p = s.index(m)
    return m, rs[p]

def solve_large(line):
    X, Y = (int(x) for x in line.split())
    return go(0, 0, X, Y, 1, "")[1]

f = open("in.txt", "r")
T = int(f.readline())
out = open("out.txt", "w")
for test in range(1, T+1):
    print test
    result = solve_large(f.readline().strip())
    out.write("Case #%s: %s\n" % (test, result))
out.close()
