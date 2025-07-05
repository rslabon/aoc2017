import functools

programs = "ABCDEFGHIJKLMNOP".lower()

moves = """s1,x3/4,pe/b"""
with open("./resources/day16.txt") as f:
    moves = f.read().strip()

moves = tuple(moves.split(','))
programs = tuple(programs)


@functools.cache
def dance(programs, moves):
    programs, moves = list(programs), list(moves)
    for move in moves:
        if move.startswith('s'):
            d = move[1:]
            d = int(d)
            programs = programs[len(programs) - d:len(programs)] + programs[0:len(programs) - d]
        elif move.startswith('x'):
            body = move[1:]
            a, b = body.split('/')
            a, b = int(a), int(b)
            tmp = programs[a]
            programs[a] = programs[b]
            programs[b] = tmp
        elif move.startswith('p'):
            body = move[1:]
            a, b = body.split('/')
            a, b = programs.index(a), programs.index(b)
            tmp = programs[a]
            programs[a] = programs[b]
            programs[b] = tmp

    return tuple(programs)


def part1(programs, moves):
    print("".join(dance(programs, moves)))


def part2(programs, moves):
    original = tuple(programs)
    i = 0
    cycle_size = 0
    cycle = []
    while i < 1_000_000_000:
        if i > 0 and programs == original:
            cycle_size = i
            break
        cycle.append(programs)
        programs = dance(programs, moves)
        i += 1

    offset = 1_000_000_000 % cycle_size
    print("".join(cycle[offset]))


part1(programs, moves)
part2(programs, moves)
