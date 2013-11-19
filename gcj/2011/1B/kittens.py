def solve(N, M, U, V):
    rooms = [range(N)]
    U = [u - 1 for u in U]
    V = [v - 1 for v in V]
    for u, v in zip(U, V):
        room = None
        for r in rooms:
            if (u in r) and (v in r):
                room = r
                break
        rooms.remove(room)
        a = [u, v]
        b = [u ,v]
        if u > v:
            tmp = u
            u = v
            v = tmp
        for x in room:
            if u < x < v:
                a.append(x)
            elif x != u and x != v:
                b.append(x)
        rooms.append(a)
        rooms.append(b)
    adjacent = [[False for x in range(N)] for y in range(N)]
    for u, v in [(i, i + 1) for i in range(N - 1)] + [(N - 1, 0)] + zip(U, V):
        adjacent[u][v] = True
        adjacent[v][u] = True
    C = min(len(x) for x in rooms)
    color = [0] * N
    current_room = None
    while rooms:
        if current_room is None:
            current_room = rooms[0]
        else:
            for room in rooms:
                if len([x for x in room if color[x] != 0]) == 2:
                    current_room = room
                    break
        for v in current_room:
            if color[v] != 0:
                continue
            colors = range(1, C + 1)
            for u in range(N):
                if color[u] != 0 and (color[u] in colors) and adjacent[u][v]:
                    colors.remove(color[u])
            used_colors = [color[u] for u in current_room]
            avail_colors = [c for c in colors if c not in used_colors]
            if avail_colors:
                color[v] = avail_colors[0]
            else:
                color[v] = colors[0]
        rooms.remove(current_room)
    return "%s\n%s" % (C, " ".join(str(c) for c in color))


for i in range(10):
    try:
        for j in range(i):
            print i,
            if i == 5 and j == 3:
                raise Exception("asdas")
    except Exception, e:
        import traceback
        import sys
        traceback.print_exc()
        print sys.exc_info()[0]


f = open("in.txt", "r")
T = int(f.readline().strip())
out = open("out.txt", "w")
for test in range(1, T+1):
    N, M = (int(x) for x in f.readline().strip().split())
    U = [int(x) for x in f.readline().strip().split()]
    V = [int(x) for x in f.readline().strip().split()]
    result = solve(N, M, U, V)
    out.write("Case #%s: %s\n" % (test, result))
    print test
out.close()
