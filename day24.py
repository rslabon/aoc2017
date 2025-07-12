from collections import deque

lines = """
0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10
""".strip().splitlines()

with open("./resources/day24.txt") as f:
    lines = f.read().strip().splitlines()

zero_pin = set()
other_pin = set()
for line in lines:
    left, right = line.split("/")
    left, right = int(left), int(right)
    if left == 0:
        zero_pin.add((left, True, right, False))
    elif right == 0:
        zero_pin.add((left, False, right, True))
    else:
        other_pin.add((left, False, right, False))


def strength(port):
    return port[0] + port[2]


def find_max_strength(current, others):
    q = deque()
    q.append((strength(current), current, others))
    max_strength = float("-inf")

    while q:
        s, current, others = q.popleft()
        if s > max_strength:
            max_strength = s

        cleft, cleft_used, cright, cright_used = current
        for other in others:
            oleft, oleft_used, oright, oright_used = other
            if (not cleft_used and not oleft_used and cleft == oleft) or (
                    not cright_used and not oleft_used and cright == oleft):
                q.append((s + strength(other),
                          (oleft, True, oright, oright_used),
                          others - {other}))
            elif (not cleft_used and not oright_used and cleft == oright) or (
                    not cright_used and not oright_used and cright == oright):
                q.append((s + strength(other),
                          (oleft, oleft_used, oright, True),
                          others - {other}))

    return max_strength


def find_max_longest_strength(current, others):
    q = deque()
    q.append((strength(current), current, others, 1))
    stats = dict()

    while q:
        s, current, others, path_size = q.popleft()
        stats[path_size] = max(stats.get(path_size, 0), s)

        cleft, cleft_used, cright, cright_used = current
        for other in others:
            oleft, oleft_used, oright, oright_used = other
            if (not cleft_used and not oleft_used and cleft == oleft) or (
                    not cright_used and not oleft_used and cright == oleft):
                q.append((s + strength(other),
                          (oleft, True, oright, oright_used),
                          others - {other},
                          path_size + 1))
            elif (not cleft_used and not oright_used and cleft == oright) or (
                    not cright_used and not oright_used and cright == oright):
                q.append((s + strength(other),
                          (oleft, oleft_used, oright, True),
                          others - {other},
                          path_size + 1))

    max_size = max(stats.keys())
    return max_size, stats[max_size]


def part1():
    max_s = float("-inf")
    for port in zero_pin:
        max_s = max(max_s, find_max_strength(port, frozenset(other_pin)))

    print(max_s)


def part2():
    stats = []
    for port in zero_pin:
        stats.append(find_max_longest_strength(port, frozenset(other_pin)))

    stats.sort(key=lambda x: x[0], reverse=True)
    print(stats[0][1])


part1()
part2()
