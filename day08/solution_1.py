def parse_data(data, index):
    _sum = 0
    offset = index + 2
    for i in range(data[index]):
        offset, meta = parse_data(data, offset)
        _sum += meta
    for i in range(data[index + 1]):
        _sum += data[offset + i]
    return offset + data[index + 1], _sum

def main():
    with open("input.txt", "r") as fin:
        data = [int(x) for x in fin.read().strip().split(" ")]
        _, meta = parse_data(data, 0)
        print(meta)

if __name__ == "__main__":
    main()