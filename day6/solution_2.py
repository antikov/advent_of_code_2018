import re
import math

def distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def is_nearest_region(clusters, x, y):
    _sum = 0
    for index, xy in enumerate(clusters):
        dist = distance(xy, (x, y))
        _sum += dist
    return 1 if _sum < 10000 else 0

def main():
    centers = []
    distances = {}
    x_range = [math.inf, -math.inf]
    y_range = [math.inf, -math.inf]
    with open("input.txt", "r") as fin:
        for line in fin:
            x, y = re.match(r"(\d+), (\d+)",line).group(1,2)
            x, y = int(x), int(y)
            centers.append((x, y))
            x_range[0] = x if x_range[0] > x else x_range[0]
            x_range[1] = x if x_range[1] < x else x_range[1]
            y_range[0] = y if y_range[0] > y else y_range[0]
            y_range[1] = y if y_range[1] < y else y_range[1]
        
        for x in range(x_range[0], x_range[1] + 1):
            for y in range(y_range[0], y_range[1] + 1):
                distances[(x, y)] = is_nearest_region(centers, x, y)
        
        print(sum(distances.values()))

if __name__ == "__main__":
    main()
