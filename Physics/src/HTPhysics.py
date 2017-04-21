#! /usr/bin/python3

#################################################
#                   HTPhysics
# HTPhysics is an implementation of Physics
# based on two books from Halliday and Tipler
#
# v1.012
# Issue #7
#
# Rodrigo Nobrega
# 20170420-
#################################################
__author__ = 'Rodrigo Nobrega'


# import modules
class SIUnit(object):
    """Defines all base units from the International System of Units."""
    def __init__(self):
        """Constructor"""
        self.baseUnit = {'m':'metre', 'kg':'kilogram', 's':'second'
        , 'A':'ampere', 'K':'kelvin', 'mol':'mole', 'cd':'candela'}
    
    def isSIunit(self, unit):
        """Tests if the unit is an SI base unit"""
        if unit in list(self.baseUnit.keys()):
            print('OK')
        else:
            print('Not OK')


# main loop
def main():
    theUnit = SIUnit()
    print(theUnit.baseUnit)
    theUnit.isSIunit('t')


# main, calling main loop
if __name__ == '__main__':
    main()
