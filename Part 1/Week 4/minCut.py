# test_graph = {1: [2,5,6],
# 2: [1,5,6,3],
# 3: [2,7,4,8],
# 4: [3,7,8],
# 5: [1,2,6],
# 6: [1,2,5,7],
# 7: [3,4,6,8],
# 8: [3,4,7]}

# test_graph = {1: [2,3],
# 2: [1,3,4],
# 3: [1,2,4],
# 4: [2,3]}

def findMinCut(test_graph):
    graph = test_graph.copy()
    from random import choice

    while (len(graph.keys()) > 2):
        pivot = choice(list(graph.keys()))
        #print (pivot)
        contract_vertex = choice(graph[pivot])
        #print (contract_vertex)
        for i in graph[contract_vertex]:
            graph[i] = [pivot if j == contract_vertex else j for j in graph[i]]
        graph[pivot] += graph.pop(contract_vertex)
        new_lst = []
        for i in graph[pivot]:
            if i != pivot:
                new_lst = new_lst + [i]
        graph[pivot] = new_lst
        #print(graph)
    return len(graph[pivot])
    
minCuts = []
for i in range(200):
    minCuts.append(findMinCut(test_graph))
    #print ("_________________________________________")

print(min(minCuts))