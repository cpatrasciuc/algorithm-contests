from scipy.misc import comb

MOD = 1000000007

COMB = []

def solve(test):
    tokens = test.split()
    N, K = int(tokens[0]), int(tokens[1])
    numbers = [long(x) for x in tokens[2:]]
    numbers.sort(reverse=True)
    result = 0L
    print len(numbers)
    for i in range(N-K+1):
        #result += COMB[N-1-i][K-1] * (numbers[i] % MOD)
        result += (long(comb(N-1-i, K-1, exact=True)) % MOD) * (numbers[i] % MOD)
        result %= MOD
    return result

def precompute():
    global COMB
    MAXN = 10001
    COMB = [[-1 for x in range(MAXN)] for y in range(MAXN)]
    for n in range(MAXN):
        COMB[n][0] = 1
        for k in range(1, n):
            COMB[n][k] = (COMB[n-1][k-1] + COMB[n-1][k]) % MOD
        COMB[n][n] = 1

#precompute()

lines = open("in.txt", "r").readlines()
T = int(lines[0])
out = open("out.txt", "w")
for test in range(1, T+1):
    result = solve(lines[2*test-1].strip() + " " + lines[2*test].strip())
    out.write("Case #%s: %s\n" % (test, result))
out.close()