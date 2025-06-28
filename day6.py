puzzle = [4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3]


def redistribute(banks):
    banks = banks[:]
    seen = set()
    cycles = 0

    while True:
        if tuple(banks) in seen:
            return cycles, banks
        seen.add(tuple(banks))
        cycles += 1

        max_memory = float('-inf')
        max_index = None
        for i, bank in enumerate(banks):
            if bank > max_memory:
                max_memory = bank
                max_index = i

        banks[max_index] = 0
        i = max_index
        while max_memory > 0:
            i = (i + 1) % len(banks)
            banks[i] += 1
            max_memory -= 1


def part1():
    print(redistribute(puzzle)[0])


def part2():
    print(redistribute(redistribute(puzzle)[1])[0])


part1()
part2()
