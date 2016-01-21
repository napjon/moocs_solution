#So we would program a function to make a gaussian formula
from math import *

def f(x,miu,sigma_square):
    e = exp((((x-miu)**2)/sigma_square)*-0.5)
    k = 1/sqrt(2*pi*sigma_square)
    f = k*e
    return f

print f(8.,10.,4.)

#what x value to maximize gaussian? the answer is x has to be equal to miu,
#which we have learned earlier
