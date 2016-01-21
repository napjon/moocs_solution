p=[0.2,0.2,0.2,0.2,0.2]
pHit = 0.6
pMiss = 0.2

p[0] = p[0]*pMiss
p[1] = p[1]*pHit
p[2] = p[2]*pHit
p[3] = p[3]*pMiss
p[4] = p[4]*pMiss

print p
#n=5 wrong code
#for i in range(n):
#sum = sum + p[i]

#as simple as
sum(p)
print sum

