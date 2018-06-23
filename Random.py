#Random
import random
import operator
from functools import reduce

class RandomPosition:
                def __init__(self, x, y, n):
                                self.x = x # x is the number of total positions 
                                self.y = y # y is the number of selected positions
                                self.n = n # n is the number of models

                def c(self): # combination
                               return reduce(operator.mul, range(self.x - self.y + 1, self.x + 1)) /reduce(operator.mul, range(1, self.y + 1))
                                
                def buildpostion(self): # main function
                                a = list() # original position list
                                for i in range(1, self.x + 1):
                                                a.append(i) 

                                c = list() # main matrix
                                for j in range(self.n): # random function
                                                b = random.sample(a, self.y)
                                                print("#", j+1, ":", b)
                                                c.append(b)

                                print("\n") # separation line
                                print("*"*12, "Statistics", "*"*12)
                                
                                for k in range(1, self.x + 1): # count the frequence of each number
                                                d = 0 # counting variables
                                                for i in range(self.n):
                                                                for j in range(self.y):
                                                                                if c[i][j] == k:
                                                                                                d += 1
                                                f = d/(self.y * self.n)
                                                print("position", k, ":", d, " "*3, "f:", '%.4f'%f)#round(, 4))
                                mean = 1/self.x
                                print("mean:", "%.4f"%mean, '\n')
                                
                                                                                                
