import collections
graph = {
    0:[1,2,3],
    1:[0,2],
    2:[0,1],
    3:[0],
    4:[2]
}

def bfs(graph,node):
    visited = {node}
    queue = collections.deque([node])
    while queue:
        vertex = queue.popleft()
        visited.add(vertex)
        for i in graph[vertex]:
            if i not in visited:
                visited.add(i)
    print(visited)


bfs(graph,0)

# {0, 1, 2, 3}