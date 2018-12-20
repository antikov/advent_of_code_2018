import re
from collections import defaultdict

def get_available_vertexes(graph, vertexes):
    available = []
    req = set()
    for node in graph.keys():
        req = req | graph[node]
    for vertex in sorted(list(vertexes)):
        if vertex not in req:
            available.append(vertex)
    return available

def workers_tick(workers):
    done = []
    for index, worker in enumerate(workers):
        if worker != None:
            worker[0] -= 1
            if worker[0] < 1:
                done.append(worker[1])
                workers[index] = None
    return done

def set_worker(task, workers):
    for index, worker in enumerate(workers):
        if worker == None:
            length = ord(task) - ord('A') + 61
            workers[index] = [length, task]
            break

def is_available_worker(workers):
    return None in workers

def all_available_workers(workers):
    for worker in workers:
        if worker != None:
            return False
    return True

def print_line(second, workers, done):
    output = f"{second}\t"
    for worker in workers:
        if worker == None:
            output += ".\t"
        else:
            output += worker[1] + "\t"
    output += f"{done}"
    print(output)

def main():
    graph = defaultdict(set)
    vertexes = set()
    with open("input.txt", "r") as fin:
        for line in fin:
            vertex_in, vertex_out = re.match(r"Step (\w+) must be finished before step (\w+) can begin.", line).group(1, 2)
            graph[vertex_in].add(vertex_out)
            vertexes.add(vertex_in)
            vertexes.add(vertex_out)

        _count = 0
        done = ""
        workers = [None for _ in range(5)]
        while len(vertexes) > 0 or not(all_available_workers(workers)):
            
            available_vertexes = get_available_vertexes(graph, vertexes)
            for available_vertex in available_vertexes:
                if is_available_worker(workers):
                    set_worker(available_vertex, workers)
                    vertexes.discard(available_vertex)

            print_line(_count, workers, done)

            _count += 1
            finished_vertexes = workers_tick(workers)
            for finished_vertex in finished_vertexes:
                graph[finished_vertex] = set()
                done += finished_vertex

        print(_count)

if __name__ == "__main__":
    main()