def parse_data(data, index):
    offset = index + 2
    nodes = []
    for i in range(data[index]):
        offset, meta = parse_data(data, offset)
        nodes.append(meta)
    _sum = 0
    for i in range(data[index + 1]):
        value = data[offset + i]
        if data[index] == 0:
            _sum += value
        else:
            _sum += nodes[value - 1] if len(nodes) >= value else 0
    return offset + data[index + 1], _sum

def main():
    with open("input.txt", "r") as fin:
        data = [int(x) for x in fin.read().strip().split(" ")]
        _, meta = parse_data(data, 0)
        print(meta)

if __name__ == "__main__":
    main()