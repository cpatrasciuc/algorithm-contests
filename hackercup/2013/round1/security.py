import networkx as nx
import re

def diff(s1, s2, initial):
    result = 0
    found = False
    for i in range(len(s1)):
        if s1[i] == "?" :
            if s2[i] != "?":
                found = True
                result = result*10 + (ord(s2[i]) - ord("a"))
            else:
                result *= 10
        else:
            if s1[i] != s2[i] and s2[i] != "?":
                return None
            result = result*10 + (ord(s1[i]) - ord("a"))
    if found:
        return result * initial
    return 0

def solve(m_str, k1, k2):
    m = int(m_str)
    section_size = len(k1) / m

    k1s = [k1[i*section_size:(i+1)*section_size] for i in range(m)]
    k2s = [k2[i*section_size:(i+1)*section_size] for i in range(m)]
    k2s.sort()
    #print k2s

    G = nx.Graph()
    for i in range(len(k1s)):
        G.add_node((i, 1))
    for i in range(len(k2s)):
        G.add_node((i, 2))

    for i in range(len(k1s)):
        for j in range(len(k2s)):
            d = diff(k1s[i], k2s[j], 10**((len(k1s) - i - 1) * section_size))
            if d is not None:
                #print "%s matches %s: %s" % (k1s[i], k2s[j], d)
                G.add_edge((i, 1), (j, 2), weight=-d)

    matching = nx.max_weight_matching(G, maxcardinality=True)
    #print matching
    #print len(matching)
    if len(matching) / 2 != m:
        return "IMPOSSIBLE"

    result = [None for i in range(len(k1s))]
    for u, v in matching.items():
        if u[1] == 1:
            result[u[0]] = k2s[v[0]]
    result = "".join(result)

    key = [x for x in k1]
    for i in range(len(k1)):
        if k1[i] == "?":
            if result[i] != "?":
                key[i] = result[i]
            else:
                key[i] = "a"

    return "".join(key)

lines = open("in.txt", "r").readlines()
T = int(lines[0])
out = open("out.txt", "w")
for test in range(1, T+1):
    result = solve(lines[3*test-2].strip(), lines[3*test-1].strip(), lines[3*test].strip())
    out.write("Case #%s: %s\n" % (test, result))
out.close()
