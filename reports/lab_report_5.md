# Lab Report 5

## Title
Breadth-First Search (BFS) Algorithm

## Theory
Breadth-First Search (BFS) is a fundamental graph traversal algorithm. It explores the graph layer by layer, starting from a given source node. It visits all direct neighbors of the source node first, then moves to the neighbors of those neighbors, and so on. To keep track of the nodes to visit next in a First-In-First-Out (FIFO) manner, BFS utilizes a **Queue** data structure.

## Algorithms
Breadth-First Search using a Queue and an Adjacency List representation of a graph.

## Code Implementation
```python
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * (max(self.graph) + 1)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is Breadth First Traversal (starting from vertex 2)")
    g.BFS(2)
```

## Output
```
Following is Breadth First Traversal (starting from vertex 2)
2 0 3 1 
```

## Discussion
The implementation uses `defaultdict(list)` to elegantly handle the adjacency list without needing to pre-initialize empty lists for each vertex. The `visited` array is critical; without it, the algorithm would get trapped in an infinite loop due to cycles in the graph (like the edge from 2 back to 0). Popping from index 0 of a list acts as a queue dequeue operation, fulfilling the FIFO requirement.

## Conclusion
We successfully implemented and executed Breadth-First Search to traverse a directed graph. BFS is essential in AI for problems involving finding the shortest path in unweighted graphs or state-spaces.
