from math import *
import random

landmarks = [[20.0, 20.0],
             [80.0, 80.0],
             [20.0, 80.0],
             [80.0, 20.0]]

world_size = 100.0

class robot:
    def __init__(self):
        #random position at world size
        #random.random() takes value between 0 and 1
        self.x = random.random()*world_size
        self.y = random.random()*world_size
        self.orientation = random.random() * 2.0 * pi
        #add a noise to our gaussian
        self.forward_noise = 0.0;
        self.turn_noise = 0.0;
        self.sense_noise = 0.0;

    def set(self, new_x, new_y, new_orientation):
        """takes x, y and radian heading"""
        #This function want to set position and heading
        #program defensively! we don't want the value to be negative or out of world_size
        if new_x < 0 or new_x >= world_size:
            raise ValueError, 'X coordinate out of bound'
        if new_x < 0 or new_x >= world_size:
            raise ValueError, 'X coordinate out of bound'
        if new_orientation < 0 or new_orientation >= 2*pi:
            raise ValueError, 'X coordinate out of bound'
        #If all three satisfied, then insert new value
        self.x = float(new_x)
        self.y = float(new_y)
        self.orientation = float(new_orientation)

    def set_noise(self, new_f_noise, new_t_noise, new_s_noise):
        """makes it possible to change the noise parameters"""
        #this is often useful in particle filters self.forward_noise = float(new_f_noise)
        #it's an easy function just to set noise, there are 3 kind of noise
        self.forward_noise = float(new_f_noise);
        self.turn_noise = float(new_t_noise);
        self.sense_noise = float(new_s_noise);

    def sense(self):
        """senses the possibility in each possible area"""
        Z = []
        for i in range(len(landmarks)):
            dist = sqrt((self.x - landmarks[i][0] ) **2 +(self.y - landmarks[i][1]) **2 )
            dist += random.gauss(0.0, self.sense_noise)
            Z.append(dist)
        return Z

    def move(self, turn, forward):
        if forward < 0:
            raise ValueError, 'Robot can not move backwards'
        #turn positive is counter-clockwise
        #turn and add randomness to the turning command
        #turning/orientation also have a noise, a turn-noise
        orientation = self.orientation + float(turn) + random.gauss(0.0, self.turn_noise)
        orientation %= 2* pi#recalculated so it doesn't exceed  360 degree

        #What move does, is actually recreate the robot, with change existing parameter
        dist = float(forward) + random.gauss(0.0, self.forward_noise)
        #forward of course depend on the orientation, and the noise it makes when forward
        x = self.x + (cos(orientation) * dist)
        y = self.y + (sin(orientation) * dist)
        x %= world_size         #cyclic x,y, make it doesn't exceed world_size
        y %= world_size

        #recreate the robot with updated parameter
        res = robot()
        res.set(x,y, orientation)
        #When init of course, noise return zero, so set with prior noise
        res.set_noise(self.forward_noise, self.turn_noise, self.sense_noise)
        return res

    def Gaussian(self, mu, sigma, x):
        """calculates the probability of x for 1-dim Gaussian with mean mu and var. sigma"""
        return exp(- ((mu - x) ** 2) / (sigma**2) / 2.0) / sqrt(2.0 * pi * (sigma**2))

    def measurement_prob(self, measurement):
        """calculates how likely a measurement should be which is an essential step"""
        prob = 1.0;
        for i in range(len(landmarks)):
            dist = sqrt((self.x - landmarks[i][0] ) **2 +(self.x - landmarks[i][0]) **2 )
            prob *= self.Gaussian(dist,self.sense_noise, measurement[i] )
        return prob

    def __repr__(self):
        """reinitialized print function for this class"""
        return '[x = %.6s y = %.6s orient = %.6s]' % (str(self.x), str(self.y), str(self.orientation))

myrobot = robot()
myrobot = myrobot.move(0.1, 5.0)
Z = myrobot.sense()

N = 1000
p = []
#This is how we init particles in 1000 particles, a random by init, and fixed noise
for i in range(N):
    x = robot()
    x.set_noise(0.05, 0.05, 5.0)
    p.append(x)

#p2 is to make robot moves like correct robot moves(in myrobot)
p2 = []
for i in range(N):
    p2.append(p[i].move(0.1, 5.0))
p = p2

w = []
#insert code here!
#This code here to calculate the weight of all particles,
#Based on comparing Z, senses of the correct robot's position
#9.912421262869467e-55 ==> e-55, more weight, more likely, the longer it's survive
#8.345334102281845e-169 ==> e-169, lower weight, less likely, the shorter it's survive
for i in range(N):
    w.append(p[i].measurement_prob(Z))
print w #Please print w for grading purposes.

p3 = []
index = int(random.random() * N)
print index
beta = 0.0
mw = max(w)
for i in range(N):
    beta += random.random() * 2.0 * mw
    #print beta
    while beta > w[index]:
      #print w[index]
      beta -= w[index]
      index = (index + 1) % N
    p3.append(p[index])
p = p3
#print p