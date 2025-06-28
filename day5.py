with open('./resources/day5.txt') as f:
    lines = f.read().strip().splitlines()

offsets = [int(line) for line in lines]


def find_exit(offsets, part2):
    pc = 0
    steps = 0
    while pc < len(offsets):
        offset = offsets[pc]
        steps += 1
        if part2 and offset >= 3:
            offsets[pc] -= 1
        else:
            offsets[pc] += 1

        pc += offset
        if pc >= len(offsets):
            return steps

    raise ValueError("no exit found")


def part1():
    print(find_exit(offsets[:], False))


def part2():
    print(find_exit(offsets[:], True))


part1()
part2()
