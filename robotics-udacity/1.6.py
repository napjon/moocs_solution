#Now we want to add motions into parameter that we have. in the senses we include
#measurements as paramater to manipulate the probability for each cell. Now the motions
#will gives commmand, like 1 to move right, and zero to move left.




p=[0.2,0.2,0.2,0.2,0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements =  ['red','red']
motions =[1,1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i]) #hit return zero if false
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss)) #if hit zero then miss
    s=sum(q)
    for i in range (len(p)):
        q[i] = q[i]/s
    return q

def move(p,U):
    q = []
    for i in range(len(p)):
        s= p[(i-U) % len(p)] * pExact
        s=s+p[(i-U-1) % len(p)] *pUndershoot
        s=s+p[(i-U+1) % len(p)] *pOvershoot
        q.append(s)
    return q

for k in range(len(measurements)):
    p= sense(p, measurements[k])
    p = move(p,motions[k])

print p