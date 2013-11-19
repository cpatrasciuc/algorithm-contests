INVALID = -100

cache = {}
d = []

def get_time(star, arrival_time, L, t, N):
    if star >= N:
        return arrival_time
    if L > 0:
        if arrival_time >= t:
                remaining = d[star:]
                remaining.sort(reverse=True)
                result = arrival_time + sum(remaining[:L]) + sum(remaining[L:]) * 2
        elif arrival_time + d[star] * 2 > t:
                low_time = t - arrival_time
                low_dist = low_time * 0.5
                high_dist = d[star] - low_dist
                high_time = high_dist / 1
                result = get_time(star + 1, arrival_time + d[star] * 2, L, t, N)
                result = min(result, get_time(star + 1, arrival_time + low_time + high_time, L - 1, t, N))
        else:
            arrival_time += d[star] * 2
            star += 1
            while star < N and (arrival_time + d[star] * 2 <= t):
                arrival_time += d[star] * 2
                star += 1
            result = get_time(star, arrival_time, L, t, N)
    else:
        result = arrival_time + sum(d[star:]) * 2
    return result

def solve(line):
    line = line.split()
    L, t, N, C = (int(x) for x in line[:4])
    a = [int(x) for x in line[4:]]
    global d
    d = a[:]
    while len(d) < N:
        d.extend(a)
    d = d[:N]
    global cache
    cache = {}
    result = get_time(0, 0, L, t, N)
    return int(result)

f = open("in.txt", "r")
T = int(f.readline())
out = open("out.txt", "w")
for test in range(1, T+1):
    result = solve(f.readline().strip())
    out.write("Case #%s: %s\n" % (test, result))
out.close()
