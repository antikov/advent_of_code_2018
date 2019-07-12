import re


def get_registers(string):
    return list(map(int, re.findall(r"\d+", string)))


def main():
    r = [0, 0, 0, 0]

    COMMANDS = {
        "addr" : lambda a, b: r[a] + r[b],
        "addi" : lambda a, b: r[a] + b,
        
        "mulr" : lambda a, b: r[a] * r[b],
        "muli" : lambda a, b: r[a] * b,
        
        "banr" : lambda a, b: r[a] & r[b],
        "bani" : lambda a, b: r[a] & b,
        
        "borr" : lambda a, b: r[a] | r[b],
        "bori" : lambda a, b: r[a] | b,
        
        "setr" : lambda a, b: r[a],
        "seti" : lambda a, b: a, 
        
        "gtir" : lambda a, b: 1 if a > r[b] else 0,
        "gtri" : lambda a, b: 1 if r[a] > b else 0,
        "gtrr" : lambda a, b: 1 if r[a] > r[b] else 0,
        
        "eqir" : lambda a, b: 1 if a == r[b] else 0,
        "eqri" : lambda a, b: 1 if r[a] == b else 0,
        "eqrr" : lambda a, b: 1 if r[a] == r[b] else 0,
    }

    total_count = 0
    with open("input.txt", "r") as fin:
        lines = fin.readlines()
        for index, line in enumerate(lines):
            if line.startswith("Before"):
                before = get_registers(lines[index])
                _,a,b,c = get_registers(lines[index+1])
                after = get_registers(lines[index+2])
                
                _count = 0
                for command in COMMANDS.keys():
                    r = before.copy()
                    r[c] = COMMANDS[command](a, b)
                    if r == after:
                        _count += 1

                if _count >= 3:
                    total_count += 1

    print(total_count)


if __name__ == "__main__":
    main()
