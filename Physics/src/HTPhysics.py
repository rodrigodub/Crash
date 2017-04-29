#! /usr/bin/python3

#################################################
#                   HTPhysics
# HTPhysics is an implementation of Physics
# based on two books from Halliday and Tipler
#
# v1.015
# Issue #8
#
# Rodrigo Nobrega
# 20170420-20170429
#################################################
__author__ = 'Rodrigo Nobrega'


# import modules
import math


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
        self.prefix = {24: ['Y', 'yotta', 1000000000000000000000000]
        , 21: ['Z', 'zetta', 1000000000000000000000]
        , 18: ['E', 'exa', 1000000000000000000]
        , 15: ['P', 'peta', 1000000000000000]
        , 12: ['T', 'tera', 1000000000000]
        , 9: ['G', 'giga', 1000000000]
        , 6: ['M', 'mega', 1000000]
        , 3: ['k', 'kilo', 1000]}
    
    def reduce(self, number):
        """Calculates the prefixed unit
        arg: number<space>unit
        i.e.: 250000 m"""
        # takes argument ('2500 m') and splits it as value and unit
        try:
            value = int(number.split()[0])
            unit = number.split()[1]
        except:
            value = 0
            unit = 'N/A'
        # output for debug
        print('number: {}\nvalue: {}\nunit: {}'.format(number, value, unit))
        # calculates number length l, remainder r and prefix factor p
        l = len(str(value))
        r = l % 3
        p = l - r
        # output for debug
        print('length: {}\nremainder: {}\nprefix factor: {}'.format(l, r, p))
        # output value
        valueout = value / math.pow(10, p)
        # output unit
        unitout = self.prefix[p][0] + unit
        # output for debug
        print('new value: {}\nnew unit: {}'.format(valueout, unitout))


# main loop
def main():
    # create an SI unit instance, with all seven SI units
    theUnit = SIUnit()
    # print(theUnit.baseUnit)
    # tests if a given unit is an SI unit
    testUnit = input('Enter an unit to test: ')
    theUnit.isSIunit(testUnit)
    theUnit.listUnit()


# main, calling main loop
if __name__ == '__main__':
    main()
