from collections import deque

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)

    def bfs(self, start_vertex):
        visited = set()
        queue = deque()
        queue.append(start_vertex)
        visited.add(start_vertex)

        while queue:
            current_vertex = queue.popleft()
            print(current_vertex)

            for neighbor in self.adjacency_list[current_vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

# Exemplo de uso:
graph = Graph()

# Adicionando vértices ao grafo
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')
graph.add_vertex('F')

# Adicionando arestas ao grafo
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('B', 'E')
graph.add_edge('C', 'E')
graph.add_edge('E', 'F')

# Executando a busca em largura (BFS) a partir do vértice 'A'
print("Busca em Largura (BFS):")
graph.bfs('A')
