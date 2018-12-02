def main():
    total = 0
    seen = set([0])
    with open("input.txt","r") as fin:
        lines = fin.readlines()
        index = 0
        while True:
            if index >= len(lines):
                index = 0
            total += int(lines[index])
            if total in seen:
                print(total)
                break
            else:
                seen.add(total)
            index += 1

if __name__ == "__main__":
    main()