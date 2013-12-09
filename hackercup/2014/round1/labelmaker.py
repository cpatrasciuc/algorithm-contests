
def solve(line):
    letters, N = line.split()
    N = int(N)
    letters = "".join(sorted(letters))

    pow = len(letters)
    letter_count = 1
    while N > pow:
        N -= pow
        letter_count += 1
        pow *= len(letters)

    result = ""
    for i in range(letter_count):
        letter_index = 0
        if N != 0:
            pow /= len(letters)
            if N % pow == 0:
                letter_index = min(len(letters) - 1, N / pow - 1)
                N = pow
            else:
                letter_index = min(len(letters) - 1, N / pow)
                N = N % pow
        result += letters[letter_index]
    return result

lines = open("in.txt", "r").readlines()
T = int(lines[0])
out = open("out.txt", "w")
for test in range(1, T+1):
    result = solve(lines[test].strip())
    out.write("Case #%s: %s\n" % (test, result))
out.close()
