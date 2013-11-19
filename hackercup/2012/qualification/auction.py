def lcm(a,b):
    gcd, tmp = a,b
    while tmp:
        gcd,tmp = tmp, gcd % tmp
    return a*b/gcd


def isBetter(A, B):
    return (A[0] < B[0] and not A[1] > B[1]) or (A[1] < B[1] and not A[0] > B[0])

def solve(line):
    N, P1, W1, M, K, A, B, C, D = tuple([int(x) for x in line.split()])
    LCM = lcm(M, K)
    #print LCM
    products = [(P1, W1)]
    for i in range(1):
        break
        P1 = ((A*P1 + B) % M) + 1
        W1 = ((C*W1 + D) % K) + 1
        #print "%s %s" % (P1, W1)
        products.append((P1, W1))
        if products[0] == products[-1]:
            products = products[:-1]
            break
    return "%s %s" % (LCM, N)
    bargain = [True for _ in products]
    terrible = [True for _ in products]

    for i in range(len(products)):
        for q in products:
            if products[i] != q:
                if isBetter(q, products[i]):
                    bargain[i] = False
                    break
        for q in products:
            if products[i] != q:
                if isBetter(products[i], q):
                    terrible[i] = False
                    break

    print bargain
    print terrible

    total_bargains = 0
    for i in range(len(products)):
        if bargain[i]:
            total_bargains += N / len(products)
            if N % len(products) > i:
                total_bargains += 1

    total_terrible = 0
    for i in range(len(products)):
        if terrible[i]:
            total_terrible += N / len(products)
            if N % len(products) > i:
                total_terrible += 1

    print "=" * 20
    return "%s %s" % (total_terrible, total_bargains)


lines = open("in.txt", "r").readlines()
T = int(lines[0])
out = open("out.txt", "w")
for test in range(1, T+1):
    result = solve(lines[test].strip())
    out.write("Case #%s: %s\n" % (test, result))
out.close()
