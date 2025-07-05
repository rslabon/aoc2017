step = 349


def part1():
    buffer = [0]
    i = 0
    current = 0
    value = 1
    while i < 2017:
        next = (current + step) % len(buffer)
        next += 1
        current = next
        buffer = buffer[0:next] + [value] + buffer[next:]
        value += 1
        i += 1

    print(buffer[current + 1])


def part2():
    i = 0
    current = 0
    value = 1
    size = 1
    answer = None
    while i < 50_000_000:
        next = (current + step) % size
        next += 1
        current = next
        size += 1
        if next == 1:
            answer = value
        value += 1
        i += 1

    print(answer)


part1()
part2()
