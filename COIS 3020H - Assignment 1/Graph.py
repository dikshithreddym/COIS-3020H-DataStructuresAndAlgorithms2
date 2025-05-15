class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, name):
        if name not in self.adjacency_list:
            self.adjacency_list[name] = []

    def add_edge(self, start, end):
        if start not in self.adjacency_list:
            self.add_vertex(start)
        self.adjacency_list[start].append(end)

        if end not in self.adjacency_list:
            self.add_vertex(end)
        self.adjacency_list[end].append(start)
    
    def get_neighbors(self, vertex):
        return self.adjacency_list.get(vertex, [])
    
    def contains_vertex(self, vertex):
        return vertex in self.adjacency_list
    
    def print_adjacency_list(self):
        for vertex in self.adjacency_list:
            neighbors = ", ".join(self.adjacency_list[vertex])
            print(f"{vertex}: {neighbors}")