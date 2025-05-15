from collections import deque

class BFS:
    @staticmethod
    def find_all_shortest_paths(graph, start, goal):
        queue = deque([[start]])
        visited = set()
        all_paths = []
        min_path_length = float('inf')

        if start == goal:
            return [[start]]

        while queue:
            path = queue.popleft()
            node = path[-1]

            if len(path) > min_path_length:
                continue

            if node not in visited or node == goal:
                if node != goal:
                    visited.add(node)

                for neighbor in graph.get_neighbors(node):
                    if neighbor not in path:  # Prevent cycles and revisiting nodes in the same path
                        new_path = list(path)
                        new_path.append(neighbor)

                        if neighbor == goal:
                            if len(new_path) < min_path_length:
                                min_path_length = len(new_path)
                                all_paths = [new_path]
                            elif len(new_path) == min_path_length:
                                all_paths.append(new_path)
                        else:
                            queue.append(new_path)
        return all_paths

    @staticmethod
    def traverse_graph_levels(graph, start):
        queue = deque([(start, 0)])  # (vertex, level)
        visited = set()
        traversal_steps = []

        while queue:
            node, level = queue.popleft()

            if node not in visited:
                visited.add(node)
                traversal_steps.append((node, level))

                for neighbor in graph.get_neighbors(node):
                    if neighbor not in visited:
                        queue.append((neighbor, level + 1))

        return traversal_steps
