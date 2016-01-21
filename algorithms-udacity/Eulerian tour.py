test_case1 = [(3, 1),(2, 3),(1, 2) ]


test_case2 = [(0, 1), (1, 5), (1, 7), (4, 5),
(4, 8), (1, 6), (3, 7), (5, 9),
(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]

test_case3 = [(1, 13), (1, 6), (6, 11), (3, 13),
(8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9),
(1, 12), (4, 12), (5, 14), (0, 1),  (2, 3), (4, 11), (6, 9),
(7, 14),  (10, 13)]

test_case4 = [(8, 16), (8, 18), (16, 17), (18, 19),
(3, 17), (13, 17), (5, 13),(3, 4), (0, 18), (3, 14), (11, 14),
(1, 8), (1, 9), (4, 12), (2, 19),(1, 10), (7, 9), (13, 15),
(6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)]


def find_eulerian_tour(graph):
    a = max([max(x) for x in graph])#find max value in list of tupples
    d_et = [[] for i in range(a+1)]#make an empty slot for each of value
    for e in graph:#assign the value to the list
        d_et[e[0]].append(e[1])
        d_et[e[1]].append(e[0])
    result = []
    (i,j) = graph[0]
    while len(result) < len(graph):#while result is no more than the length of the graph
        result.append(i)#append i
        j = d_et[i].pop()#pop last element of j in i
        d_et[j].remove(i)#and also remove j in i
        i= j#continue by replacing i with j
    result.append(i)#append last element
    return result#voila


print neo_find_eulerian_tour(test_case4 )
