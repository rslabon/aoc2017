from collections import deque

lines = """
0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
""".strip().splitlines()

with open("./resources/day12.txt") as f:
    lines = f.read().strip().splitlines()

graph = dict()
for line in lines:
    left, right = line.split(" <-> ")
    left = int(left.strip())
    right = right.strip().split(",")
    adj = graph.get(left, set())
    for n in right:
        n = int(n.strip())
        adj.add(n)
        other_adj = graph.get(n, set())
        other_adj.add(left)
        graph[n] = other_adj
    graph[left] = adj


def find_group(graph, start):
    seen = set()
    q = deque()
    q.append(start)

    while q:
        v = q.popleft()
        if v in seen:
            continue
        seen.add(v)
        for n in graph[v]:
            if n not in seen:
                q.append(n)

    return seen


def part1():
    print(len(find_group(graph, 0)))


def part2():
    groups = set()
    for v in graph.keys():
        groups.add(frozenset(find_group(graph, v)))

    print(len(groups))


part1()
part2()
