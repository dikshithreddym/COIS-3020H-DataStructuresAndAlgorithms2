import Graph
from bfs import BFS  

if __name__ == "__main__":
    graph = Graph.Graph()

    # Add edges to form the graph
    graph.add_edge("a", "s")
    graph.add_edge("a", "b")
    graph.add_edge("b", "c")
    graph.add_edge("c", "d")
    graph.add_edge("s", "e")
    graph.add_edge("s", "d")
    graph.add_edge("d", "g")
    graph.add_edge("d", "f")
    graph.add_edge("e", "f")
    graph.add_edge("e", "g")
    graph.add_edge("f", "g")

    # Print adjacency list for Question 2(a)
    print("Adjacency List of the Graph:")
    graph.print_adjacency_list()

    # Traverse graph and print levels for Question 2(b)
    print("\nTraversal Levels from Starting Point 's':")
    traversal_steps = BFS.traverse_graph_levels(graph, "s")
    for node, level in traversal_steps:
        print(f"Vertex: {node}, Level: {level}")

    # Perform BFS to find all shortest paths for Question 3
    print("\nEnter the starting vertex: ")
    start = input()
    print("Enter the ending vertex: ")
    goal = input()
    paths = BFS.find_all_shortest_paths(graph, start, goal)

    # Print results
    if paths:
        print(f"\nAll shortest paths from {start} to {goal}:")
        for path in paths:
            print(" -> ".join(path))
    else:
        print(f"No path found from {start} to {goal}.")

    # Time complexity analysis for Question 4
    print("\nTime Complexity Analysis:")
    print("The time complexity of BFS traversal is O(V + E), where V is the number of vertices and E is the number of edges.")
    print("Finding all shortest paths may require traversing multiple paths, leading to increased complexity based on the graph structure.")
