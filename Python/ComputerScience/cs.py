#! /usr/bin/python3

#################################################
#               Computer Science
#         CrashCourse Computer Science
#
# v1.115
# Issue #35
#
# Rodrigo Nobrega
# 20170420-20171010
#################################################
__author__ = 'Rodrigo Nobrega'

# import modules
# import os
# import datetime


# CCTransistor()
class CCTransistor(object):
    """Class to define a Transistor with 3 electrodes."""
    def __init__(self, name):
        self.name = name
        # collector = electrode_in. List with [state, charge]
        self.collector = [0, '|']
        # emitter = electrode_out. List with [state, charge]
        self.emitter = [0, '|']
        # base = gate. List with [state, charge]
        self.base = [0, '|']
        # print(self)
    
    def __str__(self):
        st = int((17 - len(self.name)) / 2) * ' ' + self.name + int((17 - len(self.name)) / 2) * ' '
        return '=================\n{}\n================='\
                '\n   C    B    E  \n   {}    {}    {}  \n   {}    {}    {}  \n'\
                .format(st
                , self.collector[0], self.base[0], self.emitter[0]
                , self.collector[1], self.base[1], self.emitter[1])
    

class CCBattery(object):
    """Class to define a Battery."""
    def __init__(self, name):
        self.name = name
        self.positive = [1, '+']
        self.negative = [1, '-']
    
    def __str__(self):
        return '        |\n        |   {}\n  -------------  {}\n    ---------\n        |   {}\n        |\n'\
               .format(self.positive[1], self.name, self.negative[1])
        

# test loop
def test():
    print('------------------------')
    print('Test.')
    print('------------------------')
    a = CCTransistor('T1')
    b = CCBattery('Bat1')
    print(a)
    print(b)


# main loop
def main():
    print('------------------------')
    print('Main.')
    print('------------------------')


# main, calling main loop
if __name__ == '__main__':
    test()
    # main()


