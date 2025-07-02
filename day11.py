with open("./resources/day11.txt") as f:
    moves = f.read().strip().split(",")


def double_height_distance(a, b):
    (ax, ay), (bx, by) = a, b
    dcol = abs(ax - bx)
    drow = abs(ay - by)
    return dcol + max(0, (drow - dcol) // 2)


def count_steps(moves):
    x, y = 0, 0
    for move in moves:
        if move == "n":
            y -= 2
        if move == "s":
            y += 2
        elif move == "ne":
            x -= 1
            y -= 1
        elif move == "se":
            x -= 1
            y += 1
        elif move == "nw":
            x += 1
            y -= 1
        elif move == "sw":
            x += 1
            y += 1

    return double_height_distance((0, 0), (x, y))


def furthest(moves):
    x, y = 0, 0
    max_steps = float("-inf")
    for move in moves:
        if move == "n":
            y -= 2
        if move == "s":
            y += 2
        elif move == "ne":
            x -= 1
            y -= 1
        elif move == "se":
            x -= 1
            y += 1
        elif move == "nw":
            x += 1
            y -= 1
        elif move == "sw":
            x += 1
            y += 1

        max_steps = max(max_steps, double_height_distance((0, 0), (x, y)))

    return max_steps


def part1():
    print(count_steps(moves))


def part2():
    print(furthest(moves))


part1()
part2()
