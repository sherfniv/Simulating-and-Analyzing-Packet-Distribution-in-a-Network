import numpy as np
import math
import random

def distribution_delta(dt,lam = 1):
    t = np.arange(0,1010,dt)
    v = [0]
    for i in range(0,len(t)-1):
        v.append(lam*(math.e**((-1*lam)*(t[i+1]))))
    return v


def delta_generate(dist_func):
    delta = random.choices(dist_func,dist_func)
    delta = delta[0]
    return delta


def const_gen(num):
    sum = 0
    for i in range(1,num+1):
        sum = sum + 1/i
    c = 1/sum
    return c




def const_dest_gen(num):
    sum = 0
    for i in range(1,num+1):
        sum = sum + 1/(num+1-i)
    c = 1/sum
    return c


const_origin = const_gen(1024)
const_dest = const_dest_gen(1024)
lst_packages = []
lst_computers = [i for i in range(1,1025)]
