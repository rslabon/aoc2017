# 37 36  35  34  33  32 31
# 38 17  16  15  14  13 30
# 39 18   5   4   3  12 29
# 40 19   6   1   2  11 28
# 41 20   7   8   9  10 27
# 42 21  22  23  24  25 26
# 43 44  45  46  47  48 49

# movements
# R 1U 2L 2D 2R
# R 3U 4L 4D 4R
# R 5U 6L 6D 6R
# R 7U 8L 8D 8R

def distance(target):
    x, y, v = 0, 0, 1

    u = 1
    l = 2
    d = 2
    r = 2
    while True:
        x += 1
        v += 1
        if v == target:
            return abs(x) + abs(y)

        i = 0
        while i < u:
            y -= 1
            v += 1
            i += 1
            if v == target:
                return abs(x) + abs(y)

        i = 0
        while i < l:
            x -= 1
            v += 1
            i += 1
            if v == target:
                return abs(x) + abs(y)

        i = 0
        while i < d:
            y += 1
            v += 1
            i += 1
            if v == target:
                return abs(x) + abs(y)

        i = 0
        while i < r:
            x += 1
            v += 1
            i += 1
            if v == target:
                return abs(x) + abs(y)

        u += 2
        l += 2
        d += 2
        r += 2


def store(grid, x, y):
    v = 0
    for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
        v += grid.get((x + dx, y + dy), 0)

    grid[(x, y)] = v
    return v


def next_larger(target):
    grid = dict()
    x, y = 0, 0
    grid[(x, y)] = 1

    u = 1
    l = 2
    d = 2
    r = 2
    while True:
        x += 1
        v = store(grid, x, y)
        if v > target:
            return v

        i = 0
        while i < u:
            y -= 1
            i += 1
            v = store(grid, x, y)
            if v > target:
                return v

        i = 0
        while i < l:
            x -= 1
            i += 1
            v = store(grid, x, y)
            if v > target:
                return v

        i = 0
        while i < d:
            y += 1
            i += 1
            v = store(grid, x, y)
            if v > target:
                return v

        i = 0
        while i < r:
            x += 1
            i += 1
            v = store(grid, x, y)
            if v > target:
                return v

        u += 2
        l += 2
        d += 2
        r += 2


def part1():
    print(distance(312051))


def part2():
    print(next_larger(312051))


part1()
part2()
