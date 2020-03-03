from queue import Queue
def bfs_shortest_path_length(graph,s,e):
    q = Queue()
    q.put(s)
    dist = {}
    if s == e:
        return 0
    dist[s] = 0
    while not q.empty():
        curr = q.get()
        for i in graph[curr]:
            if i not in dist.keys():
                q.put(i)
                dist[i] = dist[curr] + 1
                if i == e:
                    return dist[i]
    return -1

# graph = {
#     's':['a','b'],
#     'a':['s','c'],
#     'b':['s','c','d'],
#     'c':['a','e','b','d'],
#     'd':['b','c','e'],
#     'e':['c','d']
# }
#print (bfs_shortest_path_length(graph,'s','e'))
graph = {
    1:[3,5],
    3:[1,5],
    5:[1,3,7,9],
    7:[5],
    9:[5],
    2:[4],
    4:[2],
    6:[8,10],
    8:[6,10],
    10:[6,8]
}
print (bfs_shortest_path_length(graph,1,10))