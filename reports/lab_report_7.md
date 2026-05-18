# Lab Report 7

## Title
Graph Traversal Algorithms: BFS and DFS Review

## Theory
Graph traversal is a foundational concept in AI, used to systematically visit every node (or vertex) in a graph.
- **Breadth-First Search (BFS):** Explores all immediate neighbors at the current depth before moving deeper. It guarantees the shortest path on unweighted graphs and relies on a Queue (FIFO).
- **Depth-First Search (DFS):** Explores a path all the way to a leaf node before backtracking and trying another path. It relies on a Stack (LIFO) or Recursion.

## Algorithms
- Breadth-First Traversal (Queue-based)
- Depth-First Traversal (Recursion-based)

## Code Implementation
*(Conceptual aggregation based on lab manuals)*
```python
# BFS Setup summary
class Graph:
    def BFS(self, s):
        visited = [False] * (max(self.graph) + 1)
        queue = [s]
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

# DFS Setup summary
def dfsRec(adj, visited, s, res):
    visited[s] = True
    res.append(s)
    for i in adj[s]:
        if not visited[i]:
            dfsRec(adj, visited, i, res)
```

## Output
Both implementations yield a systematic listing of vertices, differing in order:
- **BFS Output:** Layer-by-layer discovery.
- **DFS Output:** Deep-branch discovery.

## Discussion
Through reviewing both algorithms together, their contrasting strategies become clear. BFS is memory intensive for wide graphs because the queue must hold all nodes at the current level. DFS is memory intensive for deep graphs due to the call stack size. BFS is ideal for finding the quickest route between two close points, whereas DFS is optimal for complete exhaustive searches and game-tree analysis.

## Conclusion
We solidified our understanding of fundamental graph traversal strategies. Mastering BFS and DFS is critical, as they form the building blocks for more advanced AI search algorithms like Uniform Cost Search, A* Search, and Minimax.
