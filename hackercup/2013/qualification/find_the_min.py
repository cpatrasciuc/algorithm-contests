import heapq

def solve(test):
    n, k, a, b, c, r = (int(x) for x in test.split())
    m = [a]
    found = [0] * k
    if a < k:
        found[a] = 1
    for _ in range(1, k):
        value = (b * m[-1] + c) % r
        m.append(value)
        if value < k:
            found[value] += 1
    result = []

    q = [x for x in range(k) if not found[x]]
    heapq.heapify(q)
    if not q:
        result = [k] + m
    else:
        current = 0
        while q:
            if current == k - 1:
                pass
            item = heapq.heappop(q)
            result.append(item)
            if (current < k) and (m[current] < k) and (item != m[current]):
                if found[m[current]] == 1:
                    heapq.heappush(q, m[current])
                found[m[current]] -= 1
            current += 1
        result.append(k)
        if current < k:
            result.extend(m[current:])
    return result[(n - k - 1) % len(result)]



lines = open("in.txt", "r").readlines()
T = int(lines[0])
out = open("out.txt", "w")
for test in range(1, T+1):
    result = solve(lines[2*test-1].strip() + " " + lines[2*test].strip())
    out.write("Case #%s: %s\n" % (test, result))
out.close()
