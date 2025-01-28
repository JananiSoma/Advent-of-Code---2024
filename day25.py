import sys


with open(sys.argv[1], 'r') as f:
    inputs = list(map(str.strip, f.read().split('\n\n')))

items = {"#": [], ".": []}
for grid_str in inputs:
    grid = list(zip(*grid_str.split('\n')))
    items[grid[0][0]].append([len([r for r in c if r == "#"]) for c in grid])

part1 = 0
for lock in items["#"]:
    for key in items["."]:
        if all(l + k <= 7 for l, k in zip(lock, key)):
            part1 += 1
    
print(f'Part 1: {part1}')