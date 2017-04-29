#! /usr/bin/python3

#################################################
#                   HTPhysics
# HTPhysics is an implementation of Physics
# based on two books from Halliday and Tipler
#
# v1.013
# Issue #7
#
# Rodrigo Nobrega
# 20170420-20170429
#################################################
__author__ = 'Rodrigo Nobrega'


# import modules
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
