# Lab Report 6

## Title
Depth-First Search (DFS) Algorithm

## Theory
Depth-First Search (DFS) is a graph traversal algorithm that explores as deeply as possible along each branch before backtracking. Unlike BFS which explores level-by-level, DFS dives deep into the graph. It requires a Last-In-First-Out (LIFO) tracking mechanism. This can be implemented manually using a **Stack** data structure or implicitly by utilizing the program's call stack via **Recursion**.

## Algorithms
Depth-First Search using Recursion and an Adjacency List.

## Code Implementation
```python
def inGraph(adj,u,v): 
    adj[u].append(v)
    adj[v].append(u)
    
def dfsRec(adj, visited, s, res):
    visited[s] = True
    res.append(s)
    
    for i in adj[s]:
        if not visited[i]:
            dfsRec(adj, visited, i, res)

def dfs(adj):
    visited = [False] * len(adj)
    res = []
    dfsRec(adj, visited, 0, res)
    return res

v = 5
adj = []

for i in range(v): 
    adj.append([])

inGraph(adj,1,2)
inGraph(adj,1,0)
inGraph(adj,2,0)
inGraph(adj,2,3)
inGraph(adj,2,4)

res = dfs(adj) 
print(res)
```

## Output
```
[0, 1, 2, 3, 4]
```

## Discussion
The recursive approach (`dfsRec`) simplifies the implementation by offloading the stack management to the Python interpreter. The `inGraph` function sets up an undirected graph by appending both endpoints to each other's lists. DFS is highly effective for tasks where you need to visit every node, such as finding connected components, solving mazes, or topological sorting.

## Conclusion
We successfully implemented DFS traversal using recursion. This exercise highlighted how backtracking operates intrinsically when returning from recursive function calls after hitting a dead end in the graph.
