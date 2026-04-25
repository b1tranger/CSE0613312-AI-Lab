# function creation

def bfs():
    print("temp function 2")

# bfs()

bfs()

from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):

        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function to print a BFS of graph
    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            # Get all adjacent vertices of the
            # dequeued vertex s.
            # If an adjacent has not been visited,
            # then mark it visited and enqueue it
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

# Driver code
if __name__ == '__main__':

    # Create a graph given in
    # the above diagram
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is Breadth First Traversal"
        " (starting from vertex 2)")
    g.BFS(2)

import collections

def bfs(graph,start):
    # print("this is a function")
    print(f"printing graph: {graph}")


graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
# start = 0
bfs(graph,0) 


# def main():
#     graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
#     # start = 0
#     bfs(graph,0)  

# main()  

# if __name__ == '__main__':
#     graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
#     # start = 0
#     bfs(graph,0)



stack = []
top = -1
data = []
# size = stack.size()

def pop():
    if(top==-1):
        print("underflow")
        return
    
def push(data):
    stack.append(data)
    top=top+1
    if(top>stack.size()):
        print("Overflow")

