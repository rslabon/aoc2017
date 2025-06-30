with open("./resources/day10.txt") as f:
    puzzle = f.read().strip()


def to_ascii_codes(text):
    return [ord(c) for c in text]


def reverse(numbers, offset, length):
    left = offset
    right = offset + length - 1
    while left < right:
        tmp = numbers[left % len(numbers)]
        numbers[left % len(numbers)] = numbers[right % len(numbers)]
        numbers[right % len(numbers)] = tmp
        left += 1
        right -= 1


def knot_hash(numbers, lengths):
    current = 0
    skip = 0
    for length in lengths:
        reverse(numbers, current, length)
        current += length + skip
        current %= len(numbers)
        skip += 1

    return numbers[0] * numbers[1]


def dense_hash(numbers):
    i = 0
    result = []
    while i < 16:
        j = 1
        n = numbers[i * 16]
        while j < 16:
            n ^= numbers[i * 16 + j]
            j += 1
        result.append(n)
        i += 1

    return result


def to_hex_string(numbers):
    return "".join([f"{n:02x}" for n in numbers])


def full_knot_hush(numbers, lengths):
    current = 0
    skip = 0
    for _ in range(64):
        for length in lengths:
            reverse(numbers, current, length)
            current += length + skip
            current %= len(numbers)
            skip += 1

    return to_hex_string(dense_hash(numbers))


def part1():
    numbers = puzzle.split(",")
    numbers = [int(n) for n in numbers]
    print(knot_hash(list(range(0, 256)), numbers))


def part2():
    lengths = to_ascii_codes(puzzle)
    lengths += [17, 31, 73, 47, 23]
    print(full_knot_hush(list(range(0, 256)), lengths))


part1()
part2()
