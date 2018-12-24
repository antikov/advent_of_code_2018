INPUT = 5468

import math

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
    for i in range(1, 301):
        for j in range(1, 301):
            grid[(i, j)] = get_power(i, j, INPUT)
    
    max_power = -math.inf
    max_xy = (None, None)
    for i in range(1, 299):
        for j in range(1, 299):
            power = sum([grid[(i+x,j+y)] for x in range(3) for y in range(3)])
            if power > max_power:
                max_power = power
                max_xy = (i, j)
    print(max_xy, max_power)
    
if __name__ == "__main__":
    main()