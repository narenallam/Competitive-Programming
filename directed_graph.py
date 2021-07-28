from simple_queue import Queue
from simple_stack import Stack

infinity = float('inf')


class Vertex:
    def __init__(self, data):
        self.value = data
        self.in_degree = 0
        self.out_degree = 0
        self.neighbors = set()
        self.distance = infinity # distance from source vertex
        self.prev = None # visited from

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def __lt__(self, other):
        return self.distance < other.distance


class UWGraph:
    def __init__(self, edges):
        self.adjacency_set = dict()

        for edge in edges:
            self.add_edge(edge)

    def add_edge(self, edge):
        s, d = edge
        source = self.adjacency_set.get(s)
        destination = self.adjacency_set.get(d)

        if not source :
            source = Vertex(s)
            self.adjacency_set[s] = source

        if not destination:
            destination = Vertex(d)
            self.adjacency_set[d] = destination

        source.neighbors.add(destination)

        source.out_degree += 1
        destination.in_degree += 1

    def bfs(self):
        q = Queue()
        visited = set()
        print("---------- BFS -------------")
        for v in self.adjacency_set.values():
            if v not in visited:
                q.enque(v)
                visited.add(v)
                while not q.empty():
                    cur_vertex = q.deque()
                    print(cur_vertex, end=' ')
                    for y in cur_vertex.neighbors:
                        if y not in visited:
                            q.enque(y)
                            visited.add(y)
        print()

    def dfs(self):
        s = Stack()
        visited = set()
        print("---------- DFS -------------")
        for v in self.adjacency_set.values():
            if v not in visited:
                s.push(v)
                visited.add(v)
                while not s.empty():
                    cur_vertex = s.pop()
                    print(cur_vertex, end=' ')
                    for y in cur_vertex.neighbors:
                        if y not in visited:
                            s.push(y)
                            visited.add(y)
        print()

    def print_graph(self):
        print("---------- Graph -----------")
        for vertex in self.adjacency_set.values():
            print(vertex.value + " --> " + str([x for x in vertex.neighbors]))

    def shortest_path_uwg(self, start_v, end_v):
        # distance and prev vertex initialisation

        for vertex in self.adjacency_set.values():
            vertex.distance = infinity
            vertex.prev = None

        self.adjacency_set[start_v].distance = 0

        q = Queue()
        q.enque(start_v)
        path_exists = False
        while not q.empty():
            v = q.deque()
            cur_vertex = self.adjacency_set[v]
            for node in cur_vertex.neighbors:
                if node.distance == infinity:
                    node.distance = cur_vertex.distance + 1
                    node.prev = cur_vertex
                    q.enque(node.value)
                    if node.value == end_v:
                        q.clear()
                        path_exists = True
                        break

        print("------ Distance Table ------")

        for v in self.adjacency_set.values():
            print(v.value, '->', v.distance, ':', v.prev)

        print(f"------ Shortest Path from {start_v} to {end_v} ------")
        if path_exists:

            node = self.adjacency_set[end_v]
            path = []
            while node:
                path.append(node)
                node = node.prev
            path.reverse()
            print(path)
        else:
            print("Oops! Vertices Not Connected")


if __name__ == '__main__':

    g = UWGraph([('C', 'A'), ('C', 'F'), ('C', 'Z'),
                 ('A', 'B'), ('A', 'D'), ('D', 'F'),
                 ('D', 'G'), ('B', 'D'), ('B', 'E'), ('G', 'F')])
    # g = Graph([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E'), ('C', 'F')])
    g.print_graph()
    g.bfs()
    g.dfs()
    g.shortest_path_uwg('C', 'E')











