import csv

def make_link(G, node1, node2):#Well it's the same one, as web,
    if node1 not in G:#if not in g1, then make link
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def read_graph(filename):
    # Read an undirected graph in CSV format. Each line is an edge
    tsv = csv.reader(open(filename), delimiter='\t')
    G = {}
    for (node1, node2) in tsv: make_link(G, node1, node2)
    return G

# Read the marvel comics graph
marvelG = read_graph('uniq_edges.tsv')

# distance from start (original)
def distance(G, v1, v2):
    distance_from_start = {}#we first make a empty dict to calculate distance
    open_list = [v1]#and also we make an open list, with v1 as its first nodes
    distance_from_start[v1] = 0#create a dict with v1 as a key and value zero
    while len(open_list) > 0:#while there's a node in open list
        current = open_list[0]#we take 'the first element' in open list
        del open_list[0]#we pop that from open list
        for neighbor in G[current].keys():#and from all neighbor in the graph(within specific key)
            if neighbor not in distance_from_start:#if not in node that's been marked
                distance_from_start[neighbor] = distance_from_start[current] + 1#create a new keys in dict that return current in distance, plus 1
                if neighbor == v2: return distance_from_start[v2]#if the neighbor is indeed the destination that we're looking for,
                                                            #return the values of keys
                open_list.append(neighbor)#Otherwise, we add to the open list(remember, new element add to the end of the list)
    return False

# path from start (after modification on distance())
def path(G, v1, v2):
    #distance_from_start = {}
    path_from_start = {} # modification#
    open_list = [v1]
    #distance_from_start[v1] = 0
    path_from_start[v1] = [v1] # modification
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            #if neighbor not in distance_from_start:
            if neighbor not in path_from_start: # modification
                #distance_from_start[neighbor] = distance_from_start[current] + 1
                path_from_start[neighbor] = path_from_start[current] + [neighbor] # modification
                #if neighbor == v2: return distance_from_start[v2]
                if neighbor == v2: return path_from_start[v2] # modification
                open_list.append(neighbor)
    return False

from_node = "A"
to_node = "ZZZAX"

print distance(marvelG, from_node, to_node)
print path(marvelG, from_node, to_node)