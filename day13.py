lines = """
0: 3
1: 2
4: 4
6: 4
""".strip().splitlines()

with open("./resources/day13.txt") as f:
    lines = f.read().strip().splitlines()

i = 0
firewall = []
while i < 100:
    firewall.append(None)
    i += 1

max_firewall = float('-inf')
for line in lines:
    depth, frange = line.split(": ")
    depth = int(depth)
    frange = int(frange)
    firewall[depth] = (0, -1, frange - 1)
    max_firewall = max(max_firewall, depth)

firewall = firewall[0:max_firewall + 1]


def step(firewall):
    firewall = firewall[:]
    for i, val in enumerate(firewall):
        if not val:
            continue
        current, dir, frange = val
        if current == frange or current == 0:
            dir *= -1

        firewall[i] = (current + dir, dir, frange)

    return firewall


def has_been_caught(firewall):
    packet = -1
    for i in range(len(firewall)):
        packet += 1
        if not firewall[i]:
            firewall = step(firewall)
            continue

        current, _, _ = firewall[i]
        if current == 0:
            return True

        firewall = step(firewall)

    return False


def part1(firewall):
    packet = -1
    caught = []
    for i in range(len(firewall)):
        packet += 1
        if not firewall[i]:
            firewall = step(firewall)
            continue

        current, _, _ = firewall[i]
        if current == 0:
            caught.append(i)

        firewall = step(firewall)

    severity = sum([c * (firewall[c][2] + 1) for c in caught])
    print(severity)


def part2(firewall):
    firewall = firewall[:]
    i = 1
    while i < 4_000_000:
        firewall = step(firewall)
        if not has_been_caught(firewall):
            print(i)
            break
        i += 1


part1(firewall[:])
part2(firewall[:])
