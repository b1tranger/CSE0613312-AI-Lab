# Sample graph represented as an adjacency list using a Python Dictionary [5, 6]
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs_with_stack(graph, start_node):
    # Initialize the visited set and the stack (frontier) [3, 6]
    visited = set()
    stack = [start_node] # In Python, a list functions as a LIFO stack [1, 7]
    
    print("DFS Traversal Order:")
    while stack:
        # Pop the newest/top node from the stack (LIFO) [3, 7]
        node = stack.pop()
        
        if node not in visited:
            print(node, end=' ')
            # Mark the node as visited to avoid infinite loops [5, 6]
            visited.add(node)
            
            # Generate children: Push unvisited neighbors onto the stack [5]
            # Note: We reverse the list so the first neighbor is visited first
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

# Starting DFS from vertex 'A'
dfs_with_stack(graph, 'A')