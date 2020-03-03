curr_label = -1
def dfs(graph,s,top_order):
    global curr_label
    for i in graph[s]:
        if i not in top_order.keys():
            dfs(graph,i,top_order)
    top_order[s] = curr_label
    curr_label = curr_label - 1
    return top_order

def topological_sort(graph):
    global curr_label 
    curr_label = len(graph.keys())
    top_order = {}
    for i in graph.keys():
        if i not in top_order.keys():
            top_order = dfs(graph,i,top_order)
    return top_order

graph = {
    'w':['t'],
    'v':['t'],
    's':['v','w'],
    't':[]
}
print (topological_sort(graph))