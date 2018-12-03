import re
from collections import defaultdict

def parse_input(line):
    match = re.match(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)",line,)
    return map(int,match.group(1,2,3,4,5))

def main():
    grid = defaultdict(int)
    possible_answers = set()
    with open("input.txt","r") as fin:
        for line in fin:
            index, x_init, y_init, width, height = parse_input(line)
            possible_answers.add(index)

            for x in range(x_init, x_init + width):
                for y in range(y_init, y_init + height):
                    if grid[x, y] != 0:
                        possible_answers.discard(grid[x, y])
                        possible_answers.discard(index)
                    grid[x, y] = index
    print(*possible_answers)
    
if __name__ == "__main__":
    main()