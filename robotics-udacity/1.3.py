p=[0.2,0.2,0.2,0.2,0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red','green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i]) #hit return zero if false
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss)) #if hit zero then miss
    s=sum(q)
    for i in range (len(p)):
        q[i] = q[i]/s
        #q[i] = q[i]/sum(q)-->WRONG. The Sum then different everytime it goes to loop
    return q

#def move(p,U)

for k in range(len(measurements)):
    p = sense (p,measurements[k])

print p

print sense(p,Z)