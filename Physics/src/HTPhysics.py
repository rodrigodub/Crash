#! /usr/bin/python3

#################################################
#                   HTPhysics
# HTPhysics is an implementation of Physics
# based on two books from Halliday and Tipler
#
# v1.016
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


# main loop
def main():
    # create an SI unit instance, with all seven SI units
    theUnit = SIUnit()
    # print(theUnit.baseUnit)
    # tests if a given unit is an SI unit
    testUnit = input('Enter an unit to test: ')
    theUnit.isSIunit(testUnit)
    theUnit.listUnit()
    # creates an SI prefix instance
    thePrefix = SIPrefix()
    # converts a number and unit to a prefixed value
    testNumber = input('Enter a large or small measure (number unit): ')
    result = thePrefix.reduce(testNumber)
    print('{} is equal to {} {}'.format(testNumber, result[2], result[3]))


# main, calling main loop
if __name__ == '__main__':
    main()
