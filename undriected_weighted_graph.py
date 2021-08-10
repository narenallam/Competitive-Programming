from simple_queue import SimpleQueue
from simple_stack import SimpleStack
from collections import defaultdict
import heapq

infinity = float('inf')


class Graph:
    def __init__(self, edges):
        self.graph = defaultdict(dict)
        self.distance_table = defaultdict(dict)

        for edge in edges:
            self.add_edge(edge)

    def add_edge(self, edge):
        s, d, wt = edge
        self.graph[s][d] = wt
        self.graph[d][s] = wt

    def bfs(self):
        q = SimpleQueue()
        visited = set()
        print("---------- BFS -------------")
        for v in self.graph:
            if v not in visited:
                q.enque(v)
                visited.add(v)
                while not q.empty():
                    cur_vertex = q.deque()
                    print(cur_vertex, end=' ')
                    for y in self.graph[cur_vertex].keys():
                        if y not in visited:
                            q.enque(y)
                            visited.add(y)
        print()

    def dfs(self):
        s = SimpleStack()
        visited = set()
        print("---------- DFS -------------")
        for v in self.graph:
            if v not in visited:
                s.push(v)
                visited.add(v)
                while not s.empty():
                    cur_vertex = s.pop()
                    print(cur_vertex, end=' ')
                    for y in self.graph[cur_vertex].keys():
                        if y not in visited:
                            s.push(y)
                            visited.add(y)
        print()

    def print_graph(self):
        print("---------- Graph -----------")
        for vertex, neighbours in self.graph.items():
            print(vertex + " --> " + str(neighbours))

    # Dijkstra's Algorithm
    def shortest_path(self, start_v, end_v):
        # distance and prev vertex initialisation

        for vertex in self.graph:
            self.distance_table[vertex]['distance'] = infinity
            self.distance_table[vertex]['prev'] = None

        self.distance_table[start_v]['distance'] = 0
        print(self.distance_table)
        q = []
        heapq.heapify(q)
        heapq.heappush(q, (0, start_v))
        visited = set()

        while q:
            d, v = heapq.heappop(q)
            if v not in visited:
                for neighbour in self.graph[v]:

                    if neighbour not in visited:
                        cur_distance = self.distance_table[v]['distance'] + self.graph[v][neighbour]
                        prev_distance = self.distance_table[neighbour]['distance']
                        if cur_distance < prev_distance:
                            self.distance_table[neighbour]['distance'] = cur_distance
                            self.distance_table[neighbour]['prev'] = v
                            heapq.heappush(q, (cur_distance, neighbour))

                    visited.add(v)

        print("------ Distance Table ------")

        for vertex in self.distance_table:
            print(vertex, self.distance_table[vertex]['distance'],  self.distance_table[vertex]['prev'])

        print(f"------ Shortest Path from {start_v} to {end_v} ------")
        path = []
        node = end_v
        while node:
            path.append(node)
            node = self.distance_table[node]['prev']
        path.reverse()
        print('->'.join(path))


if __name__ == '__main__':

    # # g = Graph([('C', 'A', 2), ('C', 'F', 2), ('C', 'Z', 4),
    #              ('A', 'B', 1), ('A', 'D', 3), ('D', 'F', 1),
    #              ('D', 'G', 5), ('B', 'D', 1), ('B', 'E', 7), ('G', 'F', 2)])
    g = Graph([('A', 'B', 3), ('A', 'C', 5), ('B', 'C', 1), ('C', 'F', 3), ('A', 'E', 2), ('E', 'F', 4)])
    g.print_graph()
    # g.bfs()
    # g.dfs()
    # g.shortest_path(C', 'G')
    g.shortest_path('A', 'F')











