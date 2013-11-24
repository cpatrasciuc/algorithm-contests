import heapq


class Player:
    def __init__(self, name, shot_percentage, height):
        self.name = name
        self.shot_percentage = shot_percentage
        self.height = height
        self.min_played = 0
        self.draft_number = -1
        self.on_court = False

    def __cmp__(self, other):
        assert self.on_court == other.on_court
        if self.min_played != other.min_played:
            if not self.on_court:
                return self.min_played - other.min_played
            else:
                return other.min_played - self.min_played
        if not self.on_court:
            return self.draft_number - other.draft_number
        return other.draft_number - self.draft_number


def sort_by_percentage_and_height(p1, p2):
    if p1.shot_percentage != p2.shot_percentage:
        return p1.shot_percentage - p2.shot_percentage
    assert p1.height != p2.height
    return p1.height - p2.height


def simulate_game(team, M, P):
    on_court = []
    for _ in range(P):
        player = heapq.heappop(team)
        player.on_court = True
        heapq.heappush(on_court, player)

    if not team:
        return on_court

    for minute in range(M):
        for i in range(len(on_court)):
            on_court[i].min_played += 1
        player_out = heapq.heappop(on_court)
        player_out.on_court = False
        player_in = heapq.heappop(team)
        player_in.on_court = True
        heapq.heappush(team, player_out)
        heapq.heappush(on_court, player_in)
        print "%s: %s - IN / %s - OUT" % (minute + 1, player_in.name, player_out.name)

    return on_court


def solve(players_str, M, P):
    players = []
    for line in players_str:
        tokens = line.strip().split()
        name, percentage, height = tokens[0], int(tokens[1]), int(tokens[2])
        players.append(Player(name, percentage, height))
    players = sorted(players, sort_by_percentage_and_height, reverse=True)
    print "Initial sort: %s" % [player.name for player in players]

    team_a = []
    team_b = []

    for (i, player) in enumerate(players):
        player.draft_number = i
        if i % 2 == 0:
            heapq.heappush(team_b, player)
        else:
            heapq.heappush(team_a, player)

    on_court_a = simulate_game(team_a, M, P)
    on_court_b = simulate_game(team_b, M, P)

    return " ".join(sorted([player.name for player in on_court_a + on_court_b]))

lines = open("in.txt", "r").readlines()
T = int(lines[0])
idx = 1
out = open("out.txt", "w")
for test in range(1, T+1):
    N, M, P = (int(x) for x in lines[idx].split())
    idx += 1
    players = [line.strip() for line in lines[idx:idx+N]]
    idx += N
    result = solve(players, M, P)
    out.write("Case #%s: %s\n" % (test, result))
out.close()
