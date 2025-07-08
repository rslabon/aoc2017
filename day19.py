lines = """
     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 

""".splitlines()

with open("./resources/day19.txt") as f:
    lines = f.read().splitlines()

grid = []
for line in lines:
    row = []
    for c in line:
        row.append(c)
    if row:
        grid.append(row)

start = None
for i, v in enumerate(grid[0]):
    if v == '|':
        start = (0, i, "down")
        break

row, col, dir = start
letters = []
seen = set()

while True:
    if grid[row][col] == ' ':
        break
    if (row, col, dir) in seen:
        continue
    seen.add((row, col, dir))
    if grid[row][col].isalpha():
        letters.append(grid[row][col])
    if grid[row][col] == '+':
        for di, dj, new_dir in [(1, 0, "down"), (-1, 0, "up"), (0, 1, "right"), (0, -1, "left")]:
            new_row = row + di
            new_col = col + dj
            if (0 <= new_row < len(grid)
                    and 0 <= new_col < len(grid[new_row])
                    and grid[new_row][new_col] != ' '
                    and (new_row, new_col, dir) not in seen
            ):
                row, col, dir = new_row, new_col, new_dir
                break
    elif dir == "down":
        row += 1
    elif dir == "up":
        row -= 1
    elif dir == "right":
        col += 1
    elif dir == "left":
        col -= 1


def part1():
    print("".join(letters))


def part2():
    print(len(seen))


part1()
part2()
