from collections import Counter

lines = """
../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#
""".strip().splitlines()

with open("./resources/day21.txt") as f:
    lines = f.read().strip().splitlines()


def rotate(pattern):
    result = []
    for col, _ in enumerate(pattern[0]):
        s = ""
        for row, _ in enumerate(pattern):
            s += pattern[len(pattern) - row - 1][col]
        result.append(s)

    return tuple(result)


def flip(pattern):
    result = []
    for row in pattern:
        result.append(row[::-1])

    return tuple(result)


def split_by(pattern, n):
    result = []
    line = []
    row = 0
    col = 0
    while row < len(pattern):
        square = []
        i = 0
        while i < n:
            j = 0
            s = ""
            while j < n:
                s += pattern[row + i][col + j]
                j += 1
            i += 1
            square.append(s)

        line.append(tuple(square))
        col += n
        if col >= len(pattern) - 1:
            row += n
            col = 0
            result.append(line)
            line = []

    return result


def split(pattern):
    if len(pattern) % 2 == 0:
        return split_by(pattern, 2)
    else:
        return split_by(pattern, 3)


rules = dict()
for line in lines:
    left, right = line.split(" => ")
    input_pattern = tuple(left.split("/"))
    output_pattern = tuple(right.split("/"))
    rules[input_pattern] = output_pattern
    r0 = input_pattern
    r1 = rotate(input_pattern)
    r2 = rotate(r1)
    r3 = rotate(r2)
    rules[r0] = output_pattern
    rules[flip(r0)] = output_pattern
    rules[r1] = output_pattern
    rules[flip(r1)] = output_pattern
    rules[r2] = output_pattern
    rules[flip(r2)] = output_pattern
    rules[r3] = output_pattern
    rules[flip(r3)] = output_pattern


def consolidate(split_pattern):
    new_grid = []
    for row in split_pattern:
        new_row = [""] * len(row[0])
        for square in row:
            for idx, cell in enumerate(square):
                new_row[idx] += cell
        new_grid += new_row

    return new_grid


def generate(times):
    grid = (".#.", "..#", "###")
    for _ in range(times):
        split_grid = split(grid)
        new_split_grid = []
        for row in split_grid:
            new_row = []
            new_split_grid.append(new_row)
            for cell in row:
                new_row.append(rules[cell])
        grid = consolidate(new_split_grid)

    c = Counter("".join(grid))
    print(c["#"])


def part1():
    generate(5)


def part2():
    generate(18)


part1()
part2()
