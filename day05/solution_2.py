import math

def shrink(polymer):
    react = False
    index = 0
    while True:
        if index >= len(polymer) - 1:
            if react:
                index = 0
                react = False
            else:
                return len(polymer)
        if polymer[index].lower() == polymer[index + 1].lower() and polymer[index] != polymer[index + 1]:
            polymer = polymer[:index] + polymer[index + 2:]
            react = True
        else:
            index += 1

def main():
    with open("input.txt", "r") as fin:
        polymer = fin.readlines()[0].strip()
        all_units = set(polymer.lower())
        best_len = math.inf
        for unit in all_units:
            new_polymer = "".join(polymer.split(unit))
            new_polymer = "".join(new_polymer.split(unit.upper()))
            polymer_len = shrink(new_polymer)
            if best_len > polymer_len:
                best_len = polymer_len

        print(best_len)

if __name__ == "__main__":
    main()