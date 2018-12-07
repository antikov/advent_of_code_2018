def main():
    with open("input.txt", "r") as fin:
        polymer = fin.readlines()[0].strip()
        
        react = False
        index = 0
        while True:
            if index >= len(polymer) - 1:
                if react:
                    index = 0
                    react = False
                else:
                    print(len(polymer))
                    break
            if polymer[index].lower() == polymer[index + 1].lower() and polymer[index] != polymer[index + 1]:
                polymer = polymer[:index] + polymer[index + 2:]
                react = True
            else:
                index += 1

if __name__ == "__main__":
    main()