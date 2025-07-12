from enum import Enum

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


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    def right(self):
        if self == Direction.UP:
            return Direction.RIGHT
        elif self == Direction.DOWN:
            return Direction.LEFT
        elif self == Direction.LEFT:
            return Direction.UP
        else:
            return Direction.DOWN

    def left(self):
        if self == Direction.UP:
            return Direction.LEFT
        elif self == Direction.DOWN:
            return Direction.RIGHT
        elif self == Direction.LEFT:
            return Direction.DOWN
        else:
            return Direction.UP

    def reverse(self):
        if self == Direction.UP:
            return Direction.DOWN
        elif self == Direction.DOWN:
            return Direction.UP
        elif self == Direction.LEFT:
            return Direction.RIGHT
        else:
            return Direction.LEFT

    def move(self, row, col):
        if self == Direction.UP:
            row -= 1
        elif self == Direction.DOWN:
            row += 1
        elif self == Direction.LEFT:
            col -= 1
        elif self == Direction.RIGHT:
            col += 1
        return row, col


def part1(grid):
    grid = dict(grid)
    mid = len(lines) // 2
    row = mid
    col = mid
    dir = Direction.UP
    infections = 0

    i = 0
    while i < 10_000:
        cell = grid.get((row, col), ".")
        grid[(row, col)] = cell

        if grid[(row, col)] == "#":
            grid[(row, col)] = "."
            dir = dir.right()
        else:
            grid[(row, col)] = "#"
            infections += 1
            dir = dir.left()

        row, col = dir.move(row, col)

        i += 1

    print(infections)


def part2(grid):
    grid = dict(grid)
    mid = len(lines) // 2
    row = mid
    col = mid
    dir = Direction.UP
    infections = 0

    i = 0
    while i < 10_000_000:
        cell = grid.get((row, col), ".")
        grid[(row, col)] = cell

        if grid[(row, col)] == "#":
            grid[(row, col)] = "F"
            dir = dir.right()
        elif grid[(row, col)] == "W":
            grid[(row, col)] = "#"
            infections += 1
        elif grid[(row, col)] == "F":
            grid[(row, col)] = "."
            dir = dir.reverse()
        elif grid[(row, col)] == ".":
            grid[(row, col)] = "W"
            dir = dir.left()

        row, col = dir.move(row, col)

        i += 1

    print(infections)


part1(grid)
part2(grid)
