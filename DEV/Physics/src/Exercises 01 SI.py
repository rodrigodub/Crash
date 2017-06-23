#! /usr/bin/python3

#################################################
#                Exercises 01
# SI: International System of Units
# based on two books from Halliday and Tipler
#
# Rodrigo Nobrega
# 20170420-20170510
#################################################
__author__ = 'Rodrigo Nobrega'


# import modules
from HTPhysics import *


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
