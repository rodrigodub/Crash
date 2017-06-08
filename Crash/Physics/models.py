from django.db import models
from django.shortcuts import HttpResponse

# import modules
import math
import numpy as np
import matplotlib.pyplot as plt

# Create your models here.

class HTVector(models.Model):
    # vector name
    name = models.CharField(max_length=30, null=True)
    # magnitude, m
    m = models.FloatField(default=None, null=True)
    # anticlockwise angle with east, trigonometric angle theta
    theta = models.FloatField(default=None, null=True)
    # horizontal component, x
    x = models.FloatField(default=None, null=True)
    # vertical component, y
    y = models.FloatField(default=None, null=True)

    def calculateFromSizeAngle(self):
        # Calculates X and Y components when given magnitude and angle.
        self.x = round(self.m * math.cos(math.radians(self.theta)), 3)
        self.y = round(self.m * math.sin(math.radians(self.theta)), 3)

    def calculateFromXY(self):
        # Calculates magnitude and angle when given X and Y components.
        self.m = round(math.sqrt(self.x ** 2 + self.y ** 2), 3)
        self.theta = round(math.degrees(math.atan((self.y / self.x))), 3)

    def calculate(self):
        # depending which pair of attributes exist,
        # it calculates the other two
        if (self.m != None and self.theta != None):
            self.calculateFromSizeAngle()
        elif (self.x != None and self.y != None):
            self.calculateFromXY()
        else:
            pass
    
    def drawVector(self):
        # calculates the chart parameters and draws the vector
        # chart extents (limits):
        if (self.x > 0 and self.y > 0):
            limits = [(-1.1 * self.x), (1.1 * self.x), (-1.1 * self.y), (1.1 * self.y)]
        elif (self.x < 0 and self.y > 0):
            limits = [(1.1 * self.x), (-1.1 * self.x), (-1.1 * self.y), (1.1 * self.y)]
        elif (self.x < 0 and self.y < 0):
            limits = [(1.1 * self.x), (-1.1 * self.x), (1.1 * self.y), (-1.1 * self.y)]
        elif (self.x > 0 and self.y < 0):
            limits = [(-1.1 * self.x), (1.1 * self.x), (1.1 * self.y), (-1.1 * self.y)]
        # draw chart
        plt.axis(limits)
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        plt.grid(True, linestyle='dashed')
        plt.quiver(0, 0, self.x, self.y, angles='xy', scale_units='xy', scale=1, color='b')
        plt.title(r'Vector {}: m={} | $\theta$={} | x={} | y={}'.format(self.name, self.m, self.theta, self.x, self.y))
        # output picture
        # plt.show()
        # response = HttpResponse(content_type="image/png")
        plt.savefig('Physics/static/Physics/vector.png')
        plt.clf()
        # return response

