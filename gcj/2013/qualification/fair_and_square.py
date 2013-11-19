numbers = set()

def is_palindrome(number):
    s = str(number)
    return s == s[::-1]

def check(digits):
    a = [int(x) for x in digits]
    b = [0 for _ in range(2*len(a)+1)]
    for i in range(len(a)):
        for j in range(len(a)):
            b[i+j] += a[i] * a[j]
            if b[i+j] >= 10:
                return False
    return True

def dfs(digits, pos):
    global numbers
    if not check(digits):
        return
    if digits:
        number = int(digits)
        square = number * number
        if digits and is_palindrome(number) and is_palindrome(square):
            numbers.add(square)
            print square
    if pos >= len(digits) / 2:
        return
    left = pos
    right = len(digits) - pos - 1
    for digit in range(4):
        if pos == 0 and digit == 0:
            continue
        new_number = digits[0:left] + str(digit) + digits[left+1:right] + str(digit) + digits[right+1:]
        dfs(new_number, pos + 1)

def generate():
    for i in range(0, 26):
        s = "0" * i
        dfs("%s%s" % (s, s), 0)
        dfs("%s0%s" % (s, s), 0)
        dfs("%s1%s" % (s, s), 0)
        dfs("%s2%s" % (s, s), 0)
        dfs("%s3%s" % (s, s), 0)

def solve(line):
    A, B = (long(x) for x in line.split())
    count = 0L
    for number in numbers:
        if A <= number <= B:
            count += 1
    return count

cache_filename = "cache.txt"
preprocess = False
if preprocess:
    generate()
    out = open(cache_filename, "w")
    for number in numbers:
        out.write("%s\n" % number)
    out.close()
else:
    numbers = []
    numbers = [long(x.strip()) for x in open(cache_filename).readlines() if x.strip()]
    print len(numbers)
    lines = open("in.txt", "r").readlines()
    T = int(lines[0])
    out = open("out.txt", "w")
    for test in range(1, T+1):
        result = solve(lines[test].strip())
        out.write("Case #%s: %s\n" % (test, result))
    out.close()