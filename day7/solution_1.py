import re
from collections import defaultdict

def main():
    graph = defaultdict(set)
    vertexes = set()
    with open("input.txt", "r") as fin:
        for line in fin:
            vertex_in, vertex_out = re.match(r"Step (\w+) must be finished before step (\w+) can begin.", line).group(1, 2)
            graph[vertex_in].add(vertex_out)
            vertexes.add(vertex_in)
            vertexes.add(vertex_out)

        answer = ""
        while len(vertexes) > 0:
            req = set()
            for node in graph.keys():
                req = req | graph[node]
            for vertex in sorted(list(vertexes)):
                if vertex not in req:
                    answer += vertex
                    vertexes.remove(vertex)
                    graph[vertex] = set()
                    break
        print(answer)
            
if __name__ == "__main__":
    main()