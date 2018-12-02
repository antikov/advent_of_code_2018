def main():
    with open("input.txt","r") as fin:
        lines = fin.readlines()
        for line1 in lines:
            for line2 in lines:
                if line1 == line2 or len(line1) != len(line2):
                    continue
                    
                _count = 0
                last_differ = -1
                for index in range(len(line1)):
                    if line1[index] == line2[index]:
                        _count += 1
                    else:
                        last_differ = index

                if _count == len(line1) - 1:
                    print(line1[:last_differ] + line1[last_differ + 1:])
                    break

if __name__ == "__main__":
    main()