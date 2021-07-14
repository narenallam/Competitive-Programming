from queue import Queue
from stack import Stack

class Graph:
    def __init__(self, edges):
        self.adjacency_list = dict()
        for edge in edges:
            self.add_edge(edge)

    def add_vertex(self, v):
        if v not in self.adjacency_list:
            self.adjacency_list[v] = list()

    def add_edge(self, edge):
        x, y = edge

        self.add_vertex(x)
        self.add_vertex(y)

        if x in self.adjacency_list:
            self.adjacency_list[x].append(y)

        if y in self.adjacency_list:
            self.adjacency_list[y].append(x)


    def bfs(self):
        q = Queue()
        visited = set()

        for v in self.adjacency_list:
            if v not in visited:
                q.enque(v)
                visited.add(v)
                while not q.empty():
                    x = q.deque()
                    print(x, end=' ')
                    for y in self.adjacency_list[x]:
                        if y not in visited:
                            q.enque(y)
                            visited.add(y)

    def dfs(self):
        s = Stack()
        visited = set()
        for v in self.adjacency_list:
            if v not in visited:
                s.push(v)
                visited.add(v)
                while not s.empty():
                    x = s.pop()
                    print(x, end=' ')
                    for y in self.adjacency_list[x]:
                        if y not in visited:
                            s.push(y)
                            visited.add(y)

g = Graph([('A', 'B'), ('A', 'D'), ('B', 'D'), ('C', 'E')])
g.bfs()
print()
g.dfs()









