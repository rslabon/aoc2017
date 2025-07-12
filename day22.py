lines = """
..#
#..
...
""".strip().splitlines()

with open("./resources/day22.txt") as f:
    lines = f.read().strip().splitlines()

grid = dict()
for row, line in enumerate(lines):
    for col, cell in enumerate(line):
        grid[(row, col)] = cell



def part1(grid):
    grid = dict(grid)
    mid = len(lines) // 2
    row = mid
    col = mid
    dir = "up"
    infections = 0

    i = 0
    while i < 10_000:
        cell = grid.get((row, col), ".")
        grid[(row, col)] = cell

        if grid[(row, col)] == "#":
            grid[(row, col)] = "."
            if dir == "up":
                dir = "right"
            elif dir == "down":
                dir = "left"
            elif dir == "left":
                dir = "up"
            elif dir == "right":
                dir = "down"

        else:
            grid[(row, col)] = "#"
            infections += 1
            if dir == "up":
                dir = "left"
            elif dir == "down":
                dir = "right"
            elif dir == "left":
                dir = "down"
            elif dir == "right":
                dir = "up"

        if dir == "up":
            row -= 1
        elif dir == "down":
            row += 1
        elif dir == "left":
            col -= 1
        elif dir == "right":
            col += 1

        i += 1

    print(infections)

def part2(grid):
    grid = dict(grid)
    mid = len(lines) // 2
    row = mid
    col = mid
    dir = "up"
    infections = 0

    i = 0
    while i < 10_000_000:
        cell = grid.get((row, col), ".")
        grid[(row, col)] = cell

        if grid[(row, col)] == "#":
            grid[(row, col)] = "F"
            if dir == "up":
                dir = "right"
            elif dir == "down":
                dir = "left"
            elif dir == "left":
                dir = "up"
            elif dir == "right":
                dir = "down"

        elif grid[(row, col)] == "W":
            grid[(row, col)] = "#"
            infections += 1

        elif grid[(row, col)] == "F":
            grid[(row, col)] = "."
            if dir == "up":
                dir = "down"
            elif dir == "down":
                dir = "up"
            elif dir == "left":
                dir = "right"
            elif dir == "right":
                dir = "left"

        elif grid[(row, col)] == ".":
            grid[(row, col)] = "W"
            if dir == "up":
                dir = "left"
            elif dir == "down":
                dir = "right"
            elif dir == "left":
                dir = "down"
            elif dir == "right":
                dir = "up"

        if dir == "up":
            row -= 1
        elif dir == "down":
            row += 1
        elif dir == "left":
            col -= 1
        elif dir == "right":
            col += 1

        i += 1

    print(infections)

part1(grid)
part2(grid)
