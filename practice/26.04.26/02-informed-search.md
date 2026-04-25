# Greedy Best First Search

---
https://www.geeksforgeeks.org/artificial-intelligence/informed-search-algorithms-in-artificial-intelligence/

```py
import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def greedy_best_first_search(maze, start, end):
    open_list = []
    heapq.heappush(open_list, (heuristic(start, end), start))
    came_from = {start: None}
    visited = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while open_list:
        _, current = heapq.heappop(open_list)
        if current == end:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]
        visited.add(current)
        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            if (0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and
                    maze[neighbor[0]][neighbor[1]] == 0 and neighbor not in visited):
                visited.add(neighbor)
                came_from[neighbor] = current
                heapq.heappush(open_list, (heuristic(neighbor, end), neighbor))
    return None

path = greedy_best_first_search(maze, start, end)
print("Greedy Best-First path:", path)
```

```py
# Function to perform Best First Search
from heapq import heappush, heappop

def bestFirstSearch(edges, src, target, n):
    
    # create the adjacency list
    adj = [[] for _ in range(n)]
    for edge in edges:
        adj[edge[0]].append([edge[1], edge[2]])
        adj[edge[1]].append([edge[0], edge[2]])
    
    # create a visited array to 
    # keep track of visited nodes
    visited = [False] * n
    
    # create the min heap to store the nodes
    # based on the cost
    pq = []
    
    # push the source node in the min heap
    heappush(pq, [0, src])
    
    # mark the source node as visited
    visited[src] = True
    
    # to store the path   
    path = []
    
    # loop until the min heap is empty
    while pq:
        # get the top element of the min heap
        x = heappop(pq)[1]
        
        # push the current node in the path
        path.append(x)
        
        # if the current node is the target node
        # break the loop
        if x == target:
            break
        
        # loop through the edges of the current node
        for edge in adj[x]:
            if not visited[edge[0]]:
                # mark the node as visited
                visited[edge[0]] = True
                # push the node in the min heap
                heappush(pq, [edge[1], edge[0]])
    
    return path

if __name__ == "__main__":
    n = 14
    edgeList = [
        [0, 1, 3], [0, 2, 6], [0, 3, 5],
        [1, 4, 9], [1, 5, 8], [2, 6, 12],
        [2, 7, 14], [3, 8, 7], [8, 9, 5],
        [8, 10, 6], [9, 11, 1], [9, 12, 10],
        [9, 13, 2]
    ]
    source = 0
    target = 9
    path = bestFirstSearch(edgeList, source, target, n)
    for i in range(len(path)):
        print(path[i], end=" ")

```