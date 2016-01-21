#By 1.4.py that we have earlier. we give 3 parameter, pexact, pover, and punder
#how to accommodate this 3 parameter into move function that we have

p=[0,1,0,0,0]
world=['green', 'red', 'red', 'green', 'green']
measurements =  ['red','green']
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
        #q[i] = q[i]/sum(q)-->WRONG. The Sum then different everytime it goes to loop
    return q

def move(p,U):
    q = []
    for i in range(len(p)):
        #q.append(p[(i-U) % len(p)] * pExact)
        #q.append(p[(i-1-U) % len(p)] *pUndershoot)
        #q.append(p[(i+1-U) % len(p)] *pOvershoot)
        #the reason why we can't use this method is because it will lead to additional
        #member of the array that isn't nessescary

        s= p[(i-U) % len(p)] * pExact
        s=s+p[(i-1-U) % len(p)] *pUndershoot
        s=s+p[(i+1-U) % len(p)] *pOvershoot
        #what we are trying to do now is more convenient. we knew that each cell
        #will be receive additional probability from neighbourhood cell.
        q.append(s)
    return q
for k in range(1000):
    p=move(p,1)

print p