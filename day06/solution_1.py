import re
from collections import Counter
import math

def distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def get_nearest_cluster(clusters, x, y):
    min_distance = math.inf
    min_index = -1
    for index, xy in enumerate(clusters):
        dist = distance(xy, (x, y))
        if dist < min_distance:
            min_distance = dist
            min_index = index
        elif dist == min_distance:
            min_index = -1
    return min_index

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
                distances[(x, y)] = get_nearest_cluster(centers, x, y)
        
        c = Counter(distances.values())

        for x in [x_range[0] - 1, x_range[1] + 1]:
            for y in [y_range[0] - 1, y_range[1] + 1]:
                infinite_cluster = get_nearest_cluster(centers, x, y)
                c[infinite_cluster] = 0
        
        print(c.most_common(1)[0][1])

if __name__ == "__main__":
    main()
