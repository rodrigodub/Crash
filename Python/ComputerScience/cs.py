#! /usr/bin/python3

#################################################
#               Computer Science
#         CrashCourse Computer Science
#
# v1.114
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
        # collector = electrode_in
        self.collector = 0
        self.collectorcharge = '|'
        # emitter = electrode_out
        self.emitter = 0
        self.emittercharge = '|'
        # base = gate
        self.base = 0
        self.basecharge = '|'
        print(self)
    
    def __str__(self):
        st = int((17 - len(self.name)) / 2) * ' ' + self.name + int((17 - len(self.name)) / 2) * ' '
        return '=================\n{}\n================='\
                '\n   C    B    E  \n   {}    {}    {}  \n   {}    {}    {}  \n'\
                .format(st
                , self.collector, self.base, self.emitter
                , self.collectorcharge, self.basecharge, self.emittercharge)
        

# test loop
def test():
    print('------------------------')
    print('Test.')
    print('------------------------')
    a = CCTransistor('rodrigo')


# main loop
def main():
    print('------------------------')
    print('Main.')
    print('------------------------')


# main, calling main loop
if __name__ == '__main__':
    test()
    # main()


