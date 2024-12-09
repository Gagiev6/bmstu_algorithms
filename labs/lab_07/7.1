class Graph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def add_edge(self, from_vertex, to_vertex, weight=1):
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        self.graph[from_vertex][to_vertex] = weight
        if not self.directed:
            self.graph[to_vertex][from_vertex] = weight

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for other_vertex in self.graph:
                if vertex in self.graph[other_vertex]:
                    del self.graph[other_vertex][vertex]

    def remove_edge(self, from_vertex, to_vertex):
        if from_vertex in self.graph and to_vertex in self.graph[from_vertex]:
            del self.graph[from_vertex][to_vertex]
            if not self.directed:
                del self.graph[to_vertex][from_vertex]

    def get_vertices(self):
        return list(self.graph.keys())

    def get_edges(self):
        edges = []
        for from_vertex in self.graph:
            for to_vertex, weight in self.graph[from_vertex].items():
                edges.append((from_vertex, to_vertex, weight))
        return edges

    def is_connected(self):
        if not self.graph:
            return False

        visited = set()
        stack = [next(iter(self.graph))]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(self.graph[vertex])

        return len(visited) == len(self.graph)

    def find_eulerian_cycle(self):
        if not self.is_connected():
            return None

        degrees = {vertex: len(neighbors) for vertex, neighbors in self.graph.items()}
        odd_degree_vertices = [vertex for vertex, degree in degrees.items() if degree % 2 != 0]

        if len(odd_degree_vertices) > 0:
            return None

        def find_cycle(start):
            cycle = []
            stack = [start]
            while stack:
                vertex = stack[-1]
                if self.graph[vertex]:
                    next_vertex = next(iter(self.graph[vertex]))
                    self.remove_edge(vertex, next_vertex)
                    stack.append(next_vertex)
                else:
                    cycle.append(stack.pop())
            return cycle[::-1]

        return find_cycle(next(iter(self.graph)))

    def find_hamiltonian_cycle(self):
        if not self.is_connected():
            return None

        def hamiltonian_cycle_util(path, pos):
            if pos == len(self.graph):
                if path[0] in self.graph[path[-1]]:
                    return path + [path[0]]
                return None

            for next_vertex in self.graph[path[pos - 1]]:
                if next_vertex not in path:
                    path[pos] = next_vertex
                    result = hamiltonian_cycle_util(path, pos + 1)
                    if result:
                        return result
                    path[pos] = None

            return None


graph = Graph()


edges = [
    (1, 2), (2, 3), (3, 17), (4, 10), (10, 35), (13, 5), (11, 6), (6, 15),
    (7, 1), (1, 6), (12, 10), (10, 20), (8, 13)
]

for from_vertex, to_vertex in edges:
    graph.add_edge(from_vertex, to_vertex)

print("Граф:")
for vertex, neighbors in graph.graph.items():
    print(f"{vertex}: {neighbors}")
