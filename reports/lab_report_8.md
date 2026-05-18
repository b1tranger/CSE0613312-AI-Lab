# Lab Report 8

## Title
Informed Search: Best First Search (Greedy Best First Search)

## Theory
Informed search strategies utilize problem-specific knowledge to find solutions more efficiently than uninformed strategies. **Best First Search** (specifically, Greedy Best First Search) is an informed search algorithm that uses a heuristic function, `h(n)`, to estimate the cost from node `n` to the goal. The algorithm always selects the next node that appears to be closest to the goal (i.e., has the lowest heuristic value). This greedy approach can rapidly lead to a solution, but it is not guaranteed to find the optimal path.

## Algorithms
The algorithm uses a Priority Queue to expand nodes based on their heuristic evaluations.
1. Initialize a priority queue and insert the start node with its heuristic value.
2. Initialize a set to keep track of visited nodes to avoid cycles.
3. While the queue is not empty, pop the node with the lowest heuristic value.
4. If the node is the goal, return the path.
5. Otherwise, mark it as visited and add all its unvisited neighbors to the priority queue with their respective heuristic values.

## Code Implementation
```python
import heapq

graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('B', 2), ('C', 5), ('G', 12)],
    'B': [('C', 2)],
    'C': [('G', 3)],
    'G': []
}

heuristics = { 'S': 7, 'A': 6, 'B': 4, 'C': 2, 'G': 0 }

def best_first_search(graph, heuristics, start, goal):
    priority_queue = [(heuristics[start], start, [start])]
    visited = set()

    while priority_queue:
        h_val, current_node, path = heapq.heappop(priority_queue)
        
        if current_node in visited: continue
        print(f"Visiting: {current_node} with heuristic: {h_val}")
        visited.add(current_node)

        if current_node == goal:
            return path

        for neighbor, cost in graph[current_node]:
            if neighbor not in visited:
                new_path = list(path)
                new_path.append(neighbor)
                heapq.heappush(priority_queue, (heuristics[neighbor], neighbor, new_path))
                
    return None

if __name__ == "__main__":
    print("--- Best First Search (Informed Search) ---")
    path = best_first_search(graph, heuristics, 'S', 'G')
    print(f"\nGoal reached! Path taken: {' -> '.join(path)}")
```

## Output
```
--- Best First Search (Informed Search) ---
Visiting: S with heuristic: 7
Visiting: B with heuristic: 4
Visiting: C with heuristic: 2
Visiting: G with heuristic: 0

Goal reached! Path taken: S -> B -> C -> G
```

## Discussion
In this implementation, Python dictionaries were utilized to structure both the adjacency list of the graph and the heuristic lookup table. The built-in `heapq` module served as an efficient priority queue. The output shows the algorithm's greedy nature: from `S` (h=7), it preferred `B` (h=4) over `A` (h=6), skipping `A` entirely, even though a shorter cost path might exist. It then navigated to `C` and finally `G`.

## Conclusion
We successfully implemented Best First Search using dictionaries and priority queues in Python. This exercise demonstrated how heuristic guidance focuses the search effort toward the goal, drastically reducing the search space compared to uninformed strategies like BFS or DFS.
