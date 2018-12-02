def main():
    total = 0
    with open("input.txt","r") as fin:
        for line in fin:
            total += int(line)
    print(total)

if __name__ == "__main__":
    main()