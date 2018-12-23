import re
import numpy as np
import math

def metric(grid):
    mean_x, mean_y, _,_ = np.mean(grid, axis=0)
    ans = 0
    for line in grid:
        ans += abs(line[0] - mean_x) + abs(line[1] - mean_y)
    return ans

def step(grid):
    for coords in grid:
        coords[0], coords[1] = coords[0] + coords[2], coords[1] + coords[3]

def step_back(grid):
    for coords in grid:
        coords[0], coords[1] = coords[0] - coords[2], coords[1] - coords[3]
    
def print_grid(grid):
    min_x, min_y, _, _ = np.min(grid, axis = 0)
    max_x, max_y, _, _ = np.max(grid, axis = 0)
    new_grid = []
    for _ in range(max_y - min_y + 1):
        new_grid.append([0] * (max_x - min_x + 1))
    for line in grid:
        x, y = line[0] - min_x, line[1] - min_y
        new_grid[y][x] = 1
    for line in new_grid:
        print("".join(["#" if el else '.' for el in line]))

def main():
    grid = []
    with open("input.txt", "r") as fin:
        for line in fin:
            grid.append([int(x) for x in [line[10:16], line[18:24], line[36:38], line[40:42]]])
        for i in range(10000):
            step(grid)
        value = metric(grid)
        while True:
            step(grid)
            new_value = metric(grid)
            if new_value > value:
                step_back(grid)
                print_grid(grid)
                break
            else:
                value = new_value

if __name__ == "__main__":
    main()