import re

lines = """
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
""".strip().splitlines()

with open("./resources/day8.txt") as f:
    lines = f.read().strip().splitlines()


def satisfy(registers, condition_register, condiction, condition_value):
    if condiction == "==":
        return registers.get(condition_register, 0) == condition_value
    if condiction == "!=":
        return registers.get(condition_register, 0) != condition_value
    if condiction == ">":
        return registers.get(condition_register, 0) > condition_value
    if condiction == "<":
        return registers.get(condition_register, 0) < condition_value
    if condiction == ">=":
        return registers.get(condition_register, 0) >= condition_value
    if condiction == "<=":
        return registers.get(condition_register, 0) <= condition_value

    raise ValueError("Unknown condition")


def execute(action, action_value):
    if action == "inc":
        return action_value
    else:
        return -action_value


registers = dict()
highest = float("-inf")
for line in lines:
    target_register, action, action_value, condition_register, condiction, condition_value = \
        re.findall(r"(\w+)\s+(inc|dec)\s+(-?\d+)\s+if\s+(\w+)\s+(!=|==|>|<|<=|>=)\s+(-?\d+)", line)[0]
    action_value = int(action_value)
    condition_value = int(condition_value)
    if satisfy(registers, condition_register, condiction, condition_value):
        r = registers.get(target_register, 0)
        r += execute(action, action_value)
        registers[target_register] = r
        highest = max(r, highest)


def part1():
    registers_by_value_desc = sorted(registers.items(), key=lambda x: x[1], reverse=True)
    print(registers_by_value_desc[0][1])


def part2():
    print(highest)


part1()
part2()
