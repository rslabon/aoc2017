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
    left_pin, right_pin = line.split("/")
    left_pin, right_pin = int(left_pin), int(right_pin)
    if left_pin == 0:
        zero_pin.add((left_pin, True, right_pin, False))
    elif right_pin == 0:
        zero_pin.add((left_pin, False, right_pin, True))
    else:
        other_pin.add((left_pin, False, right_pin, False))


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

        cleft_pin, cleft_used, cright_pin, cright_used = current
        for other in others:
            oleft_pin, oleft_used, oright_pin, oright_used = other
            if (not cleft_used and not oleft_used and cleft_pin == oleft_pin) or (
                    not cright_used and not oleft_used and cright_pin == oleft_pin):
                q.append((s + strength(other),
                          (oleft_pin, True, oright_pin, oright_used),
                          others - {other}))
            elif (not cleft_used and not oright_used and cleft_pin == oright_pin) or (
                    not cright_used and not oright_used and cright_pin == oright_pin):
                q.append((s + strength(other),
                          (oleft_pin, oleft_used, oright_pin, True),
                          others - {other}))

    return max_strength


def find_max_longest_strength(current, others):
    q = deque()
    q.append((strength(current), current, others, 1))
    stats = dict()

    while q:
        s, current, others, path_size = q.popleft()
        stats[path_size] = max(stats.get(path_size, 0), s)

        cleft_pin, cleft_used, cright_pin, cright_used = current
        for other in others:
            oleft_pin, oleft_used, oright_pin, oright_used = other
            if (not cleft_used and not oleft_used and cleft_pin == oleft_pin) or (
                    not cright_used and not oleft_used and cright_pin == oleft_pin):
                q.append((s + strength(other),
                          (oleft_pin, True, oright_pin, oright_used),
                          others - {other},
                          path_size + 1))
            elif (not cleft_used and not oright_used and cleft_pin == oright_pin) or (
                    not cright_used and not oright_used and cright_pin == oright_pin):
                q.append((s + strength(other),
                          (oleft_pin, oleft_used, oright_pin, True),
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
