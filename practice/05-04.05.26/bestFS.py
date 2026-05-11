# Graph with weighted edges for neighbors
graph = {
    'S': [('A', 0), ('B', 0)], # Weights here are path costs, not used by Greedy
    'A': [('C', 0)],
    'B': [('D', 0)],
    'C': [('G', 0)],
    'D': [('G', 0)]
}

# Heuristic dictionary (estimated cost to reach goal 'G')
h = {'S': 10, 'A': 8, 'B': 5, 'C': 3, 'D': 4, 'G': 0}

def greedy_best_first(graph, start, goal, h):
    pq = [(h[start], start)] # Priority Queue (heuristic, node)
    visited = set()

    while pq:
        pq.sort() # Ensure we pick the lowest heuristic value
        current_h, current_node = pq.pop(0)

        if current_node == goal:
            print("Goal reached:", current_node)
            return

        if current_node not in visited:
            print("Visited:", current_node)
            visited.add(current_node)
            for neighbor, cost in graph[current_node]:
                if neighbor not in visited:
                    pq.append((h[neighbor], neighbor))

# Execution based on sample data [27]
greedy_best_first(graph, 'S', 'G', h)


# Visited: S
# Visited: B
# Visited: D
# Goal reached: G