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
    
def main():
    grid = []
    with open("input.txt", "r") as fin:
        for line in fin:
            grid.append([int(x) for x in [line[10:16], line[18:24], line[36:38], line[40:42]]])
        for i in range(10000):
            step(grid)
        value = metric(grid)
        steps = 10000
        while True:
            step(grid)
            new_value = metric(grid)
            if new_value > value:
                print(steps)
                break
            else:
                value = new_value
                steps += 1

if __name__ == "__main__":
    main()