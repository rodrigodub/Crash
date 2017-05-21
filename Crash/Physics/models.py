from django.db import models

# import modules
import math
import numpy as np

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
        if (self.m != None and self.theta != None):
            self.calculateFromSizeAngle()
        elif (self.x != None and self.y != None):
            self.calculateFromXY()
        else:
            pass
            