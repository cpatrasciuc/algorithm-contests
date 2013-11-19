score = {}
masks = {}

def dfs(words, letters, depth):
    #print depth, letters, words
    classes = {}
    letter = letters[0]
    for word in words:
        pattern = masks[word][letter]
        classes[pattern] = classes.get(pattern, []) + [word]
    if len(classes.keys()) == 1:
        for pattern in classes.keys():
            if len(classes[pattern]) == 1:
                word = classes[pattern][0]
                score[word] = depth
                return
            else:
                dfs(classes[pattern], letters[1:], depth)
    else:
        for pattern in classes.keys():
            if pattern.find("X") < 0:
                dfs(classes[pattern], letters[1:], depth + 1)
            else:
                dfs(classes[pattern], letters[1:], depth)

def solve_internal(words, letters):
    global score
    score = {}
    max_length = max(len(x) for x in words)
    classes = [[] for x in range(max_length + 1)]
    for word in words:
        classes[len(word)].append(word)
    for clazz in classes:
        if len(clazz):
            dfs(clazz, letters, 0)
    #print score
    max_word = ""
    max_score = -1
    for word in words:
        if score[word] > max_score:
            max_word = word
            max_score = score[word]
    return max_word

def solve(words, letters):
    global score
    global masks
    result = []
    alphabet = [chr(c) for c in range(ord('a'), ord('z') + 1)]
    for word in words:
        for letter in alphabet:
            pattern = ""
            for c in word:
                if c == letter:
                    pattern += "X"
                else:
                    pattern += "_"
            masks.setdefault(word, {})
            masks[word][letter] = pattern
    for letter in letters:
        result.append(solve_internal(words, letter))
    return " ".join(result)

f = open("in.txt", "r")
T = int(f.readline())
out = open("out.txt", "w")
for test in range(1, T+1):
    N, M = (int(x) for x in f.readline().split())
    words = []
    letters = []
    for _ in range(N):
        words.append(f.readline().strip())
    for _ in range(M):
        letters.append(f.readline().strip())
    result = solve(words, letters)
    out.write("Case #%s: %s\n" % (test, result))
out.close()
