import math
import numpy as np
import matplotlib.pyplot as plt
class Vector:
    def _init_(self):
        self.color = 0
        self.angle = 0

    def direction(self, v_x, v_y):
        self.angle = math.atan(v_y/v_x)*180/math.pi

    '''def expect_colour(self):
        self.color = v_x'''
v_x=10
v_y=10
V1=Vector()
V1.direction(v_x,v_y)
print(V1.angle)
