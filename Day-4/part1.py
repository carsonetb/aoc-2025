grid = open("input.txt").readlines()

out = 0

directions: list[tuple[int, int]] = [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, 1), (0, -1), (1, 0), (-1, 0)]

for y in range(len(grid)):
    grid[y] = grid[y].strip()
    for x in range(len(grid[y])):
        item: str = grid[y][x]
        if item == ".":
            continue
        adjacent = 0
        for direction in directions:
            if y+direction[1] < 0 or x+direction[0] < 0 or y+direction[1] >= len(grid) or x+direction[0] >= len(grid[y]):
                continue
            char = grid[y+direction[1]][x+direction[0]]
            if char == "@":
                adjacent += 1
        if adjacent < 4:
            out += 1

print(out)
