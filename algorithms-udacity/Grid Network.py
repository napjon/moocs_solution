import math
def make_link(G,node1, node2):
    if node1 not in G:
        G[node1] = {}
    G[node1][node2] = 1
    if node2 not in G:
        G[node2] = {}
    G[node2][node1] = 1

#make an empty graph
G = {}

n = 256
side = int(math.sqrt(n))

#add in the edges
for i in range(side):
    for j in range(side):
        if i <side-1: make_link(G,(i,j),(i+1,j))
        if j < side-1:make_link(G,(i,j),(i,j+1))
            #make_link(a_ring, i, (i+1)%n)

#How many nodes?
#print len(a_ring)
print len(G)

#how many edges?
#print sum([len(a_ring[node]) for node in a_ring.keys()])/2
print sum([len(G[node]) for node in G.keys()])/2

