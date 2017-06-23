from django.db import models
from django.shortcuts import HttpResponse

# import modules
import math
import matplotlib.pyplot as plt
import numpy as np

# Create your models here.

class HTVector(models.Model):
    """
    HTVector is a model class for Halliday/Tipler vectors
    """
    # vector name
    name = models.CharField(max_length=30, null=True)
    # magnitude (module), m
    m = models.FloatField(default=None, blank=True)
    # anticlockwise angle with east, trigonometric angle theta
    theta = models.FloatField(default=None, blank=True)
    # horizontal component, x
    x = models.FloatField(default=None, blank=True)
    # vertical component, y
    y = models.FloatField(default=None, blank=True)

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
        plt.gca().set_aspect('equal')
        plt.axis(limits)
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        plt.grid(True, linestyle='dashed')
        plt.quiver(0, 0, self.x, self.y, angles='xy', scale_units='xy', scale=1, color='b')
        plt.title(r'Vector {}: m={} | $\theta$={} | x={} | y={}'.format(self.name, self.m, self.theta, self.x, self.y))

        # output picture
        plt.savefig('Physics/static/Physics/vector.png')
        plt.clf()
        # return response

    def vector(self):
        # returns a numpy array
        return np.array([self.x, self.y])


class HTExercise(models.Model):
    """HTExercise will store the Halliday/Tipler exercises"""
    # Tipler (& Mosca) or Halliday (& Resnick)
    book = models.CharField(max_length=1, choices=[('T', 'Tipler'), ('H', 'Halliday')])
    # Volume
    volume = models.IntegerField(blank=True, choices=[(1, 'Volume 1'), (2, 'Volume 2'), (3, 'Volume 3'), (4, 'Volume 4')])
    # Chapter
    chapter = models.IntegerField(default=None, blank=True)
    # page
    page = models.IntegerField(default=None, blank=True)
    # exercise
    exercise = models.CharField(max_length=5, default=None, blank=True)


class HTData(models.Model):
    """The individual data for each exercise"""
    # container: the foreign key relationship to the HTExercise
    container = models.ForeignKey(HTExercise, db_index=True)
    # variable is the measurement given by the exercise (or one to calculate)
    variable = models.CharField(max_length=240, db_index=True)
    # value is the magnitude
    value = models.FloatField(db_index=True)
    # unit is how the value is measured. Preferably in SI
    unit = models.CharField(max_length=20)


