import networkx as nx


def solve(K, N, start, chests):
    g = nx.DiGraph()
    start = [int(x) for x in start.split()]
    g.add_node("N0")
    for key in start:
        g.add_edge("K%s" % key, "N0")
    for i, chest in enumerate(chests):
        chest = [int(x) for x in chest.split()]
        assert len(chest) == chest[1] + 2
        g.add_edge("N%s" % (i + 1), "K%s" % 4)


def solve2(K, N, start, chests):
    owned_keys = {}
    start = [int(x) for x in start.split()]
    assert len(start) == K
    for key in start:
        owned_keys.setdefault(key, 0)
        owned_keys[key] += 1
    required_keys_by_chest = {}
    required_keys_count = {}
    chest_contents = {}
    for i, chest in enumerate(chests):
        chest = [int(x) for x in chest.split()]
        assert len(chest) == chest[1] + 2
        required_keys_by_chest[i + 1] = chest[0]
        required_keys_count.setdefault(chest[0], 0)
        required_keys_count[chest[0]] += 1
        chest_contents[i + 1] = chest[2:]
    path = []
    chests_to_visit = range(1, N + 1)
    while chests_to_visit:
        visited_chest = None
        for chest_number in chests_to_visit:
            key = required_keys_by_chest[chest_number]
            owned_keys.setdefault(key, 0)
            if owned_keys[key] > 0:
                can_visit = False
                if required_keys_count[key] > 1:
                    if (owned_keys[key] > 1) or (key in chest_contents[chest_number]):
                        can_visit = True
                else:
                    assert required_keys_count[key] == 1
                    can_visit = True
                if can_visit:
                    visited_chest = chest_number
                    owned_keys[key] -= 1
                    required_keys_count[key] -= 1
                    for new_key in chest_contents[chest_number]:
                        owned_keys.setdefault(new_key, 0)
                        owned_keys[new_key] += 1
                    break
        if visited_chest is not None:
            chests_to_visit.remove(visited_chest)
            path.append(visited_chest)
        else:
            return "IMPOSSIBLE"
    return " ".join(str(chest) for chest in path)

lines = open("in.txt", "r").readlines()
T = int(lines[0])
out = open("out.txt", "w")
index = 1
for test in range(1, T+1):
    K, N = (int(x) for x in lines[index].strip().split())
    start = lines[index+1].strip()
    chests = [line.strip() for line in lines[index+2:index+2+N]]
    result = solve(K, N, start, chests)
    out.write("Case #%s: %s\n" % (test, result))
    index += N + 2
out.close()
