INPUT = 5468

import math
from collections import defaultdict

def get_power(x, y, serial_number):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_number
    power_level *= rack_id
    power_level = (power_level % 1000) // 100
    power_level -= 5
    return power_level

assert get_power(3, 5, 8) == 4
assert get_power(122, 79, 57) == -5
assert get_power(217, 196, 39) == 0
assert get_power(101, 153, 71) == 4

def main():
    grid = {}
    
    #https://en.wikipedia.org/wiki/Summed-area_table
    grid_sum = defaultdict(int)
    for i in range(1, 301): 
        for j in range(1, 301):
            grid[(i, j)] = get_power(i, j, INPUT)
            grid_sum[(i, j)] = grid_sum[(i - 1, j)] + grid_sum[(i, j - 1)] - grid_sum[(i - 1, j - 1)] + grid[(i, j)]
    max_power = -math.inf
    max_xyk = (None, None, None)
    for k in range(1, 301):
        for i in range(1, 301 - k):
            for j in range(1, 301 - k):
                x0, y0, x1, y1 = i - 1, j - 1, i + k - 1, j + k - 1
                power = grid_sum[(x0, y0)] + grid_sum[(x1, y1)] - grid_sum[(x0, y1)] - grid_sum[(x1, y0)]
                if power > max_power:
                    max_power = power
                    max_xyk = (i, j, k)
    print(max_xyk)

if __name__ == "__main__":
    main()