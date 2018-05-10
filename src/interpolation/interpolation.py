import numpy as np
import matplotlib.pyplot as plt
from sympy import *



class interpolate:
    def __init__(self,points):
        self.points = points
        self.points = sorted(self.points,key = lambda point : point['x'])

    def __init__(self,list_of_tupeles):
        p = [{'x': v[0],'y': v[1]} for v in list_of_tupeles]
        self.points = sorted(p,key = lambda point : point['x'])

    def lagrange(self):
        x = symbols('x')
        points_x = [v['x'] for v in self.points]
        points_y = [v['y'] for v in self.points]
        fun = 0
        for i in range(self.points.__len__()):
            l = self.points[i]['y']
            for j in range(self.points.__len__()):
                if(i != j):
                    l = l * (x - self.points[j]['x'])
                    l = l/(self.points[i]['x']-self.points[j]['x'])
            fun = fun + l
        return fun


    def newoten_method(self):
        x = symbols('x')
        points_x = [v['x'] for v in self.points]
        points_y = [v['y'] for v in self.points]
        fun = 0
        coff = []
        coff.append(points_y[0])
        divid_diff = [v for v in points_y]
        next_diff = []
        for i in range(1,self.points.__len__()):

            for j in range(1,divid_diff.__len__()):
                value = divid_diff[j] - divid_diff[j-1]
                value /= (points_x[j+i-1]-points_x[j-1])
                next_diff.append(value)

            divid_diff = [v for v in next_diff]
            coff.append(next_diff[0])
            next_diff.clear()

        fun = 0
        for i in range(points_x.__len__()):
            temp = 1
            for j in range(i):
                temp *= (x - points_x[j])
            fun += temp*coff[i]

        return fun