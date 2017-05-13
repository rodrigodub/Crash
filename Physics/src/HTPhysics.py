#! /usr/bin/python3

#################################################
#                   HTPhysics
# HTPhysics is an implementation of Physics
# based on two books from Halliday and Tipler
#
# v1.025
# Issue #10
#
# Rodrigo Nobrega
# 20170420-20170513
#################################################
__author__ = 'Rodrigo Nobrega'


# import modules
import math
import numpy as np


# HTPhysics classes
class SIUnit(object):
    """Defines all base units from the International System of Units."""
    def __init__(self):
        """Constructor"""
        self.baseUnit = {'m':'metre', 'kg':'kilogram', 's':'second'
        , 'A':'ampere', 'K':'kelvin', 'mol':'mole', 'cd':'candela'}
        print('================================================')
        print('SIUnit: A set of base units from SI was created.')
        print('================================================')
    
    def listUnit(self):
        """Lists all base units from SI"""
        [print('{} : {}'.format(k, v)) for k,v in self.baseUnit.items()]
    
    def isSIunit(self, unit):
        """Tests if the unit is an SI base unit"""
        if unit in list(self.baseUnit.keys()):
            print('Unit {} ({}) is a base unit of SI.'.format(unit, self.baseUnit[unit]))
        else:
            print('Unit {} is NOT a base unit of SI.'.format(unit))


class SIPrefix(object):
    """Converts a given number and unit into a SI prefixed one."""
    def __init__(self):
        """Constructor"""
        self.prefix = {24: ['Y', 'yotta', 'y', 'yocto']
        , 21: ['Z', 'zetta', 'z', 'zepto']
        , 18: ['E', 'exa', 'a', 'atto']
        , 15: ['P', 'peta', 'f', 'femto']
        , 12: ['T', 'tera', 'p', 'pico']
        , 9: ['G', 'giga', 'n', 'nano']
        , 6: ['M', 'mega', 'μ', 'micro']
        , 3: ['k', 'kilo', 'm', 'milli']}
        print('================================================')
        print('SIPrefix: A set of SI prefixes was created.')
        print('================================================')
    
    def reduce(self, number):
        """Calculates the prefixed unit
        Argument: number<space>unit      i.e.: 250000 m
        Returns: tuple with (number, unit, new number, new unit)"""
        # takes argument ('2500 m') and splits it as value and unit
        try:
            value = number.split()[0]
            unit = number.split()[1]
        except:
            value = 0
            unit = 'N/A'
        # output for debug
        # print('number: {}\nvalue: {}\nunit: {}'.format(number, value, unit))
        # calculates number length l, remainder r and prefix factor p
        if float(value) >= 1:
            l = len(value)
            r = l % 3
            p = l - r
            # output value
            # rounded to 3 decimal places
            valueout = round(float(value) / math.pow(10, p), 3)
            # output unit
            unitout = self.prefix[p][0] + unit
        else:
            l = len(value.split('.')[1])
            r = l % 3
            p = l - r
            # output value
            # rounded to 3 decimal places
            valueout = round(float(value) * math.pow(10, p), 3)
            # output unit
            unitout = self.prefix[p][2] + unit
        # output for debug
        # print('length: {}\nremainder: {}\nprefix factor: {}'.format(l, r, p))
        # output for debug
        # print('new value: {}\nnew unit: {}'.format(valueout, unitout))
        # return tuple
        # print((value, unit, valueout, unitout))
        return (float(value), unit, valueout, unitout)


class HTVector(object):
    """
    Class to define a numpy vector. There are two ways to create a vector:
    either giving a size and orientation (magnitude m, trigonometric angle theta (in degrees)) 
    OR giving its x, y, z (future) dimensions.
    -
    Usage: 
    v = HTVector(m=5, theta=60)
    w = HTVector(x=6, y=9)
    """
    def __init__(self, m=None, theta=None, x=None, y=None, z=None):
        if (m != None and theta != None):
            self.m = m
            self.theta = theta
            self.calculateFromSizeAngle()
        elif (x != None and y != None):
            self.x = x
            self.y = y
            self.calculateFromXY()
        else:
            print("Vector not defined.")

    def report(self):
        print('-------------Vector-----------------')
        print('Magnitude: {}\nAngle: {}'.format(self.m, self.theta))
        print('X: {}\nY: {}'.format(self.x, self.y))

    def calculateFromSizeAngle(self):
        # Calculates X and Y components when given magnitude and angle.
        self.x = round(self.m * math.cos(math.radians(self.theta)), 3)
        self.y = round(self.m * math.sin(math.radians(self.theta)), 3)

    def calculateFromXY(self):
        # Calculates magnitude and angle when given X and Y components.
        self.m = round(math.sqrt(self.x ** 2 + self.y ** 2), 3)
        self.theta = round(math.degrees(math.atan((self.y / self.x))), 3)

    def vector(self):
        # Returns the numpy vector
        return np.array([self.x, self.y])


# main loop
def main():
    pass


# main, calling main loop
if __name__ == '__main__':
    main()
