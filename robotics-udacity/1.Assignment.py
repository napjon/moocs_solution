#This is the first programming assignment.




p=[0.2,0.2,0.2,0.2,0.2]
colors=[['red','green', 'green','red',  'red'],
       ['red', 'red',   'green','red',  'red'],
       ['red', 'red',   'green','green','red'],
       ['red', 'red',   'red',  'red',  'red']]
measurements =  ['green','green','green','green','green']
motions =[[0,0],[0,1],[1,0],[1,0],[0,1]]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1
sensor_right = 0.8
p_move =1.0

sensor_wrong = 1.0 - sensor_right#compliment of sensor_right
p_stay = 1.0 - p_move

def sense(p, colors, measurements):
    aux = [[0.0 for row in range(len(p[0]))] for col in range(len(p))]
    s=0.0
    for i in range(len(p)):
        for j in range(len(p[i])):
            hit = (measurements == colors[i][j]) #hit return zero if false
            #Non-normalize posterior is prior * big sum over here
            aux[i][j] = p[i][j] * (hit*sensor_right+(1-hit) *sensor_wrong)
            s+=aux[i][j] # s used as normalizer
    for i in range(len(aux)):
        for j in range(len(p[i])):
            aux[i][j]/=s #then all probability required is divided by s
    return aux


def move(p,motion):
    aux = [[0.0 for row in range(len(p[0]))] for col in range(len(p))]
    for i in range(len(p)):
        for j in range(len(p[i])):
            #for each cell, collect the cell the robot might come from                    p_stay required if didn't move
            aux[i][j] = (p_move * p[(i-motion[0]) % len(p)][(j - motion[1]) %len(p[i])]) + (p_stay*p[i][j])
            #remember, motion[0] means go back % time
    return aux# don't have to normalize, because not very useful

def show(p):
    for i in range(len(p)):
        print p[i]#this function better than just print p, because show all of possible p field
if len(measurements) != len(motions):
    raise ValueError, "error in size of measurement/motion vector"
#next we have probability distribution initial value, divided by row and column
pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
p=[[pinit for row in range(len(colors[0]))] for col in range(len(colors[0]))]
for k in range(len(measurements)):
        p = move(p,motions[k])
        p= sense(p, colors, measurements[k])

show(p)