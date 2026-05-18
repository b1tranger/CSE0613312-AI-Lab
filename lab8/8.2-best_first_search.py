import heapq

# Dictionary representing the graph as an adjacency list
# graph[node] = [(neighbor, cost), ...]
graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('B', 2), ('C', 5), ('G', 12)],
    'B': [('C', 2)],
    'C': [('G', 3)],
    'G': []
}

# Dictionary representing the heuristic values (h) for each node
# Estimated distance to the goal node 'G'
heuristics = {
    'S': 7,
    'A': 6,
    'B': 4,
    'C': 2,
    'G': 0
}

def best_first_search(graph, heuristics, start, goal):
    # Priority queue to store (heuristic_value, node, path)
    # The heapq module sorts based on the first element in the tuple (heuristic_value)
    priority_queue = [(heuristics[start], start, [start])]
    visited = set()

    while priority_queue:
        # Get the node with the lowest heuristic value
        h_val, current_node, path = heapq.heappop(priority_queue)

        # If already visited, skip
        if current_node in visited:
            continue
            
        print(f"Visiting: {current_node} with heuristic: {h_val}")
        visited.add(current_node)

        # Check if we have reached the goal
        if current_node == goal:
            return path

        # Explore unvisited neighbors
        for neighbor, cost in graph[current_node]:
            if neighbor not in visited:
                new_path = list(path)
                new_path.append(neighbor)
                # In Best First Search, we prioritize entirely based on the heuristic value
                heapq.heappush(priority_queue, (heuristics[neighbor], neighbor, new_path))
                
    return None

if __name__ == "__main__":
    start_node = 'S'
    goal_node = 'G'
    
    print("--- Best First Search (Informed Search) ---")
    path = best_first_search(graph, heuristics, start_node, goal_node)
    
    if path:
        print(f"\nGoal reached! Path taken: {' -> '.join(path)}")
    else:
        print("\nGoal cannot be reached.")
