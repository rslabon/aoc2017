with open("./resources/day4.txt") as f:
    lines = f.read().strip().splitlines()

passphrases = []
for line in lines:
    words = line.split(" ")
    passphrases.append(words)


def part1():
    valid_count = 0
    for words in passphrases:
        if len(set(words)) == len(words):
            valid_count += 1

    print(valid_count)


def part2():
    valid_count = 0
    for words in passphrases:
        words = ["".join(sorted(word)) for word in words]
        if len(set(words)) == len(words):
            valid_count += 1

    print(valid_count)


part1()
part2()
