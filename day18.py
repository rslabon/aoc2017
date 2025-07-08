import queue
import threading

instructions = """
set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2
""".strip().splitlines()

with open("./resources/day18.txt") as f:
    instructions = f.read().strip().splitlines()


# instructions = """
# snd 1
# snd 2
# snd p
# rcv a
# rcv b
# rcv c
# rcv d
# """.strip().splitlines()


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def get_value(value, registers):
    if is_int(value):
        return int(value)
    else:
        return registers.get(value, 0)


def execute(instructions):
    registers = dict()
    last_sound = None
    pc = 0
    while 0 <= pc < len(instructions):
        instruction = instructions[pc]
        if instruction.startswith("snd"):
            _, X = instruction.split()
            last_sound = registers.get(X, 0)
            pc += 1
        elif instruction.startswith("rcv"):
            _, X = instruction.split()
            pc += 1
            if registers.get(X, 0) != 0:
                return last_sound
            pc += 1
        elif instruction.startswith("set"):
            _, X, Y = instruction.split()
            registers[X] = get_value(Y, registers)
            pc += 1
        elif instruction.startswith("add"):
            _, X, Y = instruction.split()
            registers[X] = registers.get(X, 0) + get_value(Y, registers)
            pc += 1
        elif instruction.startswith("mul"):
            _, X, Y = instruction.split()
            registers[X] = registers.get(X, 0) * get_value(Y, registers)
            pc += 1
        elif instruction.startswith("mod"):
            _, X, Y = instruction.split()
            registers[X] = registers.get(X, 0) % get_value(Y, registers)
            pc += 1
        elif instruction.startswith("jgz"):
            _, X, Y = instruction.split()
            if registers.get(X, 0) > 0:
                pc += get_value(Y, registers)
            else:
                pc += 1


def execute2(instructions, program_id, send_queue, recv_queue):
    registers = {"p": program_id}
    pc = 0
    send_count = 0
    while 0 <= pc < len(instructions):
        instruction = instructions[pc]
        if instruction.startswith("snd"):
            _, X = instruction.split()
            send_count += 1
            send_queue.put(get_value(X, registers))
            pc += 1
        elif instruction.startswith("rcv"):
            _, X = instruction.split()
            try:
                registers[X] = recv_queue.get(timeout=0.5)
                recv_queue.task_done()
                pc += 1
            except queue.Empty:
                return send_count
        elif instruction.startswith("set"):
            _, X, Y = instruction.split()
            registers[X] = get_value(Y, registers)
            pc += 1
        elif instruction.startswith("add"):
            _, X, Y = instruction.split()
            registers[X] = registers.get(X, 0) + get_value(Y, registers)
            pc += 1
        elif instruction.startswith("mul"):
            _, X, Y = instruction.split()
            registers[X] = registers.get(X, 0) * get_value(Y, registers)
            pc += 1
        elif instruction.startswith("mod"):
            _, X, Y = instruction.split()
            registers[X] = registers.get(X, 0) % get_value(Y, registers)
            pc += 1
        elif instruction.startswith("jgz"):
            _, X, Y = instruction.split()
            if get_value(X, registers) > 0:
                pc += get_value(Y, registers)
            else:
                pc += 1

    return send_count


def part1():
    print(execute(instructions))


send_queue = queue.Queue()
recv_queue = queue.Queue()


def program0():
    execute2(instructions[:], 0, send_queue, recv_queue)


def program1():
    send_count = execute2(instructions[:], 1, recv_queue, send_queue)
    print(send_count)


def part2():
    t1 = threading.Thread(target=program0)
    t2 = threading.Thread(target=program1)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


part1()
part2()
