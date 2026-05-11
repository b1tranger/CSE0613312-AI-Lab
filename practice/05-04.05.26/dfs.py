graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': ['F'], 'F': []
}
visited = set()

def dfs(graph, vertex):
    if vertex not in visited:
        print(vertex)
        visited.add(vertex)
        for neighbor in graph[vertex]:
            dfs(graph, neighbor) # Recursive Call

# Output: A B D E F C
dfs(graph, 'A')


# A
# B
# D
# E
# F
# C