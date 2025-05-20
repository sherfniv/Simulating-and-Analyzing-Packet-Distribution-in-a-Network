import numpy as np
import math
import random
import functions

lst_packages = functions.lst_packages
const_origin = functions.const_origin
const_dest = functions.const_dest
lst_computers = functions.lst_computers

class Package:
    def __init__(self,number,time = 0,from_add = 0,to_add = 0,size = 0):
        self.time = time  #time of arrival
        self.from_add = from_add #address of origin
        self.to_add = to_add #address of destination
        self.size = size
        self.number = number


    def time_of_package(self,delta):
        if self.number == 1:
            self.time = 0
        else:
            self.time = (self.number-1)*delta



    def origin_address(self):
        v = []
        for i in range(1,1025):
            x = const_origin*(1/i)
            v.append(x)
        self.from_add = random.choices(lst_computers,v)
        self.from_add = self.from_add[0]

    def dest_address(self):
        v = []
        for i in range(1, 1025):
            x = const_dest * (1 /(1025-i))
            v.append(x)
        self.to_add = random.choices(lst_computers, v)
        self.to_add = self.to_add[0]

    def size_gen(self):
        self.size = random.randint(46,1500)
