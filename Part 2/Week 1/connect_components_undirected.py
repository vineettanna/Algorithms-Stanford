from queue import Queue
def bfs(graph,s):
    q = Queue()
    q.put(s)
    explored = []
    explored.append(s)
    while not q.empty():
        curr = q.get()
        for i in graph[curr]:
            if i not in explored:
                q.put(i)
                explored.append(i)
    return explored

def connected_components(graph):
    explored_overall = []
    connected = []
    for i in graph.keys():
        if i not in explored_overall:
            explored_curr = bfs(graph,i)
            explored_overall = explored_overall + explored_curr
            connected = connected + [explored_curr]
    return connected

graph = {
    's':['a','b'],
    'a':['s','c'],
    'b':['s','c','d'],
    'c':['a','e','b','d'],
    'd':['b','c','e'],
    'e':['c','d']
}

# graph = {
#     1:[3,5],
#     3:[1,5],
#     5:[1,3,7,9],
#     7:[5],
#     9:[5],
#     2:[4],
#     4:[2],
#     6:[8,10],
#     8:[6,10],
#     10:[6,8]
# }
print (connected_components(graph))