p=[0,1,0,0,0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red','green']
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

def move(p,U):
    q = []
    for i in range(len(p)):
        q.append(p[(i-U) % len(p)])
        #rather than changing the robot to the right, it's more important to
        #know where the robot comes from, and  calculate based on the data.
        #now every increment has to know the previous probabilty
    return q

#for k in range(len(measurements)):
#    p = sense (p,measurements[k])

print move(p,1)