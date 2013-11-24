
def solve(line):
    K, ps, pr, pi, pu, pw, pd, pl = (float(x) for x in line.strip().split())
    K = int(K)

    p = [[0.0 for x in range(K + 2)] for y in range(K + 2)]
    sun = [[None for x in range(K + 2)] for y in range(K + 2)]

    result = 0.0
    p[0][0] = 1.0
    sun[0][0] = pi

    for games in range(2 * K):
        for tennison in range(games + 1):
            other = games - tennison

            if other >= K or tennison > K:
                continue
            if tennison == K and other < K:
                result += p[tennison][other]
                continue

            temp_probability = sun[tennison][other] * ps + (1.0 - sun[tennison][other]) * pr
            p[tennison + 1][other] += p[tennison][other] * temp_probability
            p[tennison][other + 1] += p[tennison][other] * (1.0 - temp_probability)

            new_sun = pw * min(sun[tennison][other] + pu, 1.0) + (1.0 - pw) * sun[tennison][other]
            if sun[tennison + 1][other] is None:
                sun[tennison + 1][other] = new_sun
            else:
                p1 = p[tennison][other]
                p2 = p[tennison + 1][other - 1]
                sun[tennison + 1][other] = p2 / (p1 + p2) * sun[tennison + 1][other] + p1 / (p1 + p2) * new_sun

            new_sun = pl * max(sun[tennison][other] - pd, 0.0) + (1.0 - pl) * sun[tennison][other]
            if sun[tennison][other + 1] is None:
                sun[tennison][other + 1] = new_sun
            else:
                p1 = p[tennison][other]
                p2 = p[tennison - 1][other + 1]
                sun[tennison][other + 1] = p2 / (p1 + p2) * sun[tennison][other + 1] + p1 / (p1 + p2) * new_sun

    return "%.6f" % result


lines = open("in.txt", "r").readlines()
T = int(lines[0])
out = open("out.txt", "w")
for test in range(1, T+1):
    result = solve(lines[test])
    out.write("Case #%s: %s\n" % (test, result))
out.close()

