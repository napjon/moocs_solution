from random import choice

def makeG(n, freeNodes):
    if n == 2:#base case, 2 power of 0
        n1 = choice(freeNodes)#value n1 is random for range freeNodes
        freeNodes.remove(n1)#remove value n1 from freeNodes
        n2 = choice(freeNodes)
        freeNodes.remove(n2)
        return [(n1,n2)]#return the tupple of n1,n2
    binList = (0,1)
    G1 = makeG(n/2, freeNodes)#list of first graph
    G2 = makeG(n/2, freeNodes)#list of second graph
    n3 = choice(G1)[choice(binList)]#choose one of tupple, then choose one of its element
    n4 = choice(G1)[choice(binList)]#same as above
    G1.extend(G2)#update G1 with element of G2 that doesn't exist(extend spesifically for list)
    G1.append((n3,n4))#append G1 with the tupple defined earlier that connected 2 graph
    return G1

print makeG(16, range(16))
