with open("./resources/day2.txt") as f:
    lines = f.read().strip().splitlines()

rows = []
for line in lines:
    parts = line.split("\t")
    numbers = [int(p.strip()) for p in parts]
    rows.append(numbers)


def find_diff(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers[-1] - sorted_numbers[0]


def find_div(numbers):
    for number in numbers:
        for other_number in numbers:
            if other_number == number:
                continue
            if other_number % number == 0:
                return other_number // number
            if number % other_number == 0:
                return number // other_number

    return None


def part1():
    c = 0
    for row in rows:
        c += find_diff(row)
    print(c)


def part2():
    c = 0
    for row in rows:
        c += find_div(row)
    print(c)


part1()
part2()
