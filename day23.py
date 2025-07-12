with open("./resources/day23.txt") as f:
    instructions = f.read().strip().splitlines()

registers = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "h": 0,
}


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def get_value(registers, v):
    if is_int(v):
        return int(v)
    else:
        return registers[v]


def execute(instructions, registers):
    pc = 0
    mul_count = 0
    while 0 <= pc < len(instructions):
        instruction = instructions[pc]
        if instruction.startswith("set"):
            _, X, Y = instruction.split(" ")
            registers[X] = get_value(registers, Y)
            pc += 1
        elif instruction.startswith("sub"):
            _, X, Y = instruction.split(" ")
            registers[X] -= get_value(registers, Y)
            pc += 1
        elif instruction.startswith("mul"):
            _, X, Y = instruction.split(" ")
            registers[X] *= get_value(registers, Y)
            mul_count += 1
            pc += 1
        elif instruction.startswith("jnz"):
            _, X, Y = instruction.split(" ")
            if get_value(registers, X) != 0:
                pc += get_value(registers, Y)
            else:
                pc += 1

    return mul_count


def part1():
    print(execute(instructions, dict(registers)))


def part2():
    def is_not_prime(n):
        if n < 2:
            return True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False

    b = 109900
    c = 126900
    h = 0

    for x in range(b, c + 1, 17):
        if is_not_prime(x):
            h += 1

    print(h)


part1()
part2()
