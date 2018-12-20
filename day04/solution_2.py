import re
from operator import itemgetter

def parse_input(line):
    match = re.search(r"^\[(\d+)\-(\d+)\-(\d+) (\d+):(\d+)\] (\S+) (\S+)", line)
    return match.group(1, 2, 3, 4, 5, 6, 7)

def main():
    guards = dict()
    with open("input.txt", "r") as fin:
        lines = list(map(parse_input, fin))
        lines.sort(key=itemgetter(0,1,2,3,4))
        
        guard_id = None
        for line in lines:
            action = line[5]
            minute = int(line[4])
            if action == "Guard":
                guard_id = int(line[6][1:])
                if guard_id not in guards:
                    guards[guard_id] = [0 for _ in range(60)]
            elif action == "wakes":
                guards[guard_id][minute] -= 1
            elif action == "falls":
                guards[guard_id][minute] += 1

        max_summator = -1
        max_index = -1
        max_guard_id = -1

        for guard_id, values in guards.items():
            summator = 0
            for index in range(60):
                item = values[index]
                summator += item
                if summator > max_summator:
                    max_summator = summator
                    max_index = index
                    max_guard_id = guard_id

        print(max_guard_id * max_index)

if __name__ == "__main__":
    main()