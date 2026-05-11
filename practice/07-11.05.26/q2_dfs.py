graph = {
    "A" : ["B", "C"],
    "B" : ["D", "E"],
    "C" : ["F", "G"],
    "D" : [ "H"],
    "E" : [],
    "F" : [],
    "G" : [],
    "H" : ["I"],
    "I" : []
}

start = "A"
dest = "I"

def dfs(graph,node,visited=None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    print(node)
    # 1. Base Case: Return True if this is the destination
    if node == dest:
        print("\ndestination found\n")
        return True

    for i in graph[node]:
        if i not in visited:
            # 2. Propagation: Check if the child call found the goal
            if dfs(graph, i, visited):
                return True # Stop and return up the stack
    
    # 3. If the goal wasn't found in any neighbor, return False
    return False


dfs(graph,start)


# A
# B
# D
# H
# I

# destination found
