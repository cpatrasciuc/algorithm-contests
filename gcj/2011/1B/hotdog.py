
def solve(data, D, sum):
    count = len(data)
    if count == 2:
        mid = (data[0] + data[1]) / 2.0
        return max(0, D / 2.0 + mid - data[1])
    min_point = data[0]
    max_point = data[-1]
    mid_left = (data[0] + data[-2]) / 2.0
    mid_right = (data[1] + data[-1]) / 2.0
    distance = D * (count - 1.0)
    need_for_right = max(0, mid_left + distance / 2.0 + D - max_point)
    need_for_left = max(0, min_point - mid_right - distance / 2.0 - D)
    if need_for_left < need_for_right:
        return max(need_for_left, solve(data[1:], D, sum - min_point))
    else:
        return max(need_for_right, solve(data[:-1], D, sum - max_point))

f = open("in.txt", "r")
T = int(f.readline().strip())
out = open("out.txt", "w")
for test in range(1, T+1):
    N, D = (int(x) for x in f.readline().strip().split())
    data = []
    sum = 0
    for _ in range(N):
        P, V = (int(x) for x in f.readline().strip().split())
        data += [P] * V
        sum += P * V
    result = solve(data, D, sum)
    out.write("Case #%s: %s\n" % (test, result))
out.close()
