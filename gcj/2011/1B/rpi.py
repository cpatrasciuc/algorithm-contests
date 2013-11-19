WP = {}
OWP = {}

def solve(N, data):
    global WP
    global OWP
    WP = {}
    OWP = {}
    result = []
    for team_id in range(N):
        win_count = 0
        match_count = 0
        for match in data[team_id]:
            if match == '1':
                win_count += 1
                match_count += 1
            elif match == '0':
                match_count += 1
        WP[team_id] = float(win_count) / float(match_count)
    for team_id in range(N):
        opponent_count = 0
        partial_sum = 0
        for opponent_id in range(N):
            win_count = 0
            match_count = 0
            if data[team_id][opponent_id] == '.':
                continue
            opponent_count += 1
            for oo_id, match in enumerate(data[opponent_id]):
                if oo_id == team_id:
                    continue
                if match == '1':
                    win_count += 1
                    match_count += 1
                elif match =='0':
                    match_count += 1
            partial_sum += float(win_count) / float(match_count)
        OWP[team_id] = partial_sum / opponent_count
    for team_id in range(N):
        wp = WP[team_id]
        owp = OWP[team_id]
        oowp = 0
        oo_count = 0
        for opponent_id in range(N):
            if data[team_id][opponent_id] != '.':
                oo_count += 1
                oowp += OWP[opponent_id]
        oowp /= oo_count
        result.append(0.25 * wp + 0.50 * owp + 0.25 * oowp)
    return "".join("\n%.6f" % x for x in result)


f = open("in.txt", "r")
T = int(f.readline().strip())
out = open("out.txt", "w")
for test in range(1, T+1):
    N = int(f.readline().strip())
    data = []
    for _ in range(N):
        data.append(f.readline().strip())
    result = solve(N, data)
    out.write("Case #%s: %s\n" % (test, result))
out.close()
