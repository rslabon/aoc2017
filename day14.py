from collections import Counter, deque

from day10 import final_knot_hash

hex = "hxtvlmkl"


def part1():
    used = 0
    for i in range(0, 128):
        hash = final_knot_hash(f"{hex}-{i}")
        bin_value = bin(int(hash, 16))[2:].zfill(128)
        used += Counter(bin_value)['1']

    print(used)


def find_region(grid, i, j):
    q = deque()
    q.append((i, j))
    region = set()

    while q:
        i, j = q.popleft()
        if (i, j) in region:
            continue

        region.add((i, j))
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            next_i, next_j = i + di, j + dj
            if (next_i, next_j) in region:
                continue
            if not (0 <= next_i < 128 and 0 <= next_j < 128):
                continue
            if grid[next_i][next_j] == 0:
                continue
            q.appendleft((next_i, next_j))

    return region


def part2():
    grid = []
    for i in range(0, 128):
        hash = final_knot_hash(f"{hex}-{i}")
        bin_value = bin(int(hash, 16))[2:].zfill(128)
        row = []
        for b in bin_value:
            row.append(int(b))
        grid.append(row)

    seen = set()
    regions = 0
    for i in range(0, 128):
        for j in range(0, 128):
            if (i, j) in seen:
                continue
            if grid[i][j] == 0:
                continue

            regions += 1
            seen |= find_region(grid, i, j)

    print(regions)


part1()
part2()
