def func_1(rec):
    print(f"Called function; passed value {rec}")


func_1(1)


### DFS Functions



def inGraph(adj,u,v): # adding values to the graph stack
    adj[u].append(v)
    adj[v].append(u)

### Main Function

v = 5
adj = []

for i in range(v): # creating space for List?
    adj.append([])

inGraph(adj,1,2)
inGraph(adj,1,0)
inGraph(adj,2,0)
inGraph(adj,2,3)
inGraph(adj,2,4)

res = dfs(adj) # calling dfs function to run the graph traversal


###
