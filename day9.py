with open("./resources/day9.txt") as f:
    puzzle = f.read().strip()


def search_groups(s):
    open_groups = 0
    garbage = False
    skip = False
    group_score = 0
    garbage_count = 0
    for c in s:
        if skip:
            skip = False
            continue
        elif garbage and c == "!":
            skip = True
        elif not garbage and c == "{":
            open_groups += 1
        elif not garbage and c == "}":
            group_score += open_groups
            skip = False
            garbage = False
            open_groups -= 1
        elif not garbage and c == "<":
            garbage = True
        elif c == ">":
            garbage = False
        elif garbage:
            garbage_count += 1

    return group_score, garbage_count


def part1():
    print(search_groups(puzzle)[0])


def part2():
    print(search_groups(puzzle)[1])


part1()
part2()
