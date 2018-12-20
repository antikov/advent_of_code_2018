import re
from collections import defaultdict

def parse_input(line):
    match = re.match(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)",line,)
    return map(int,match.group(2,3,4,5))

def main():
    grid = defaultdict(int)
    with open("input.txt","r") as fin:
        for line in fin:
            x_init, y_init, width, height = parse_input(line)

            for x in range(x_init, x_init + width):
                for y in range(y_init, y_init + height):
                    grid[x, y] += 1

    ans = map(lambda x: 1 if x > 1 else 0, grid.values())
    print(sum(ans))

if __name__ == "__main__":
    main()