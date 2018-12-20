from collections import Counter

def main():
    doubles = 0
    triples = 0
    with open("input.txt","r") as fin:
        for lines in fin:
            c = Counter(lines)
            items = {item[1] for item in c.items()}
            doubles += 1 if 2 in items else 0
            triples += 1 if 3 in items else 0
    print(doubles * triples)

if __name__ == "__main__":
    main()