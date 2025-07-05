a = 277
b = 349


# a = 65
# b = 8921


def generate(n, factor):
    return n * factor % 2147483647


def generate2(n, factor, criteria):
    n = generate(n, factor)
    while (n % criteria) != 0:
        n = generate(n, factor)

    return n


def part1(a, b):
    total = 0
    i = 0
    while i < 40_000_000:
        a = generate(a, 16807)
        b = generate(b, 48271)
        if a & 0xFFFF == b & 0xFFFF:
            total += 1
        i += 1
    print(total)


def part2(a, b):
    total = 0
    i = 0
    while i < 5_000_000:
        a = generate2(a, 16807, 4)
        b = generate2(b, 48271, 8)
        if a & 0xFFFF == b & 0xFFFF:
            total += 1
        i += 1
    print(total)


part1(a, b)
part2(a, b)
