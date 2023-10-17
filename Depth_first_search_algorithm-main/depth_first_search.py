adj_list = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['B', 'F'],
    'D': [],
    'E': ['F'],
    'F': []
}
color = {}
parent = {}
traverse_time = {}
dfs_traversal_output = []
for node in adj_list.keys():
    color[node] = 'w'
    parent[node] = None
    traverse_time[node] = [-1, -1]

time = 0


def dfs(u):
    global time
    color[u] = 'G'
    traverse_time[u][0] = time
    dfs_traversal_output.append(u)
    for v in adj_list[u]:
        if color[v] == 'w':
            parent[v] = u
            dfs(v)  #rescursive
    color[u] = 'B'
    traverse_time[u][1] = time
    time += 1


dfs('A')
print(dfs_traversal_output)
print(parent)
print(color)
for node in adj_list.keys():
    print(node, "->", traverse_time[node])
