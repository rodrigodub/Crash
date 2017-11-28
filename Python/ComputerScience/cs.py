#! /usr/bin/python3

#################################################
#               Computer Science
#         CrashCourse Computer Science
#
# v1.116
# Issue #35
#
# Rodrigo Nobrega
# 20170420-20171128
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
    
    def update(self):
        if self.collector[0] == 1 and self.base[0] == 1:
            if self.collector[1] == '+':
                self.emitter = [1, '-']
            else:
                self.emitter = [1, '+']
        else:
            self.emitter = [0, '|']
    

class CCBattery(object):
    """Class to define a Battery."""
    def __init__(self, name):
        self.name = name
        self.positive = [1, '+']
        self.negative = [1, '-']
    
    def __str__(self):
        return '        |\n        |   {}\n  -------------  {}\n    ---------\n        |   {}\n        |\n'\
               .format(self.positive[1], self.name, self.negative[1])


class CCCircuit(object):
    """Class to define a circuit. 
    Every circuit has components and connections between them.
    A closed circuit does something."""
    def __init__(self, name):
        self.name = name
        self.components = []
    
    def __str__(self):
        return 'Circuit {}'.format(self.name)

    def printcircuit(self):
        [print('{} {} connected to {} {}'.format(i[0][0], i[0][1], i[1][0], i[1][1])) for i in self.components]

    def connect(self, obj1, connection1, obj2, connection2):
        # obj1connection, obj2connection: CCBattery.positive, CCBattery.negative,
        # CCTransistor.collector, CCTransistor.base
        self.components.append([[obj1.name, connection1], [obj2.name, connection2]])
        print('{} {} connected to {} {}'.format(obj1.name, connection1, obj2.name, connection2))
        if obj1.__getattribute__(connection1) == [1, '+']:
            obj2.__setattr__(connection2, [1, '-'])
        elif obj1.__getattribute__(connection1) == [1, '-']:
            obj2.__setattr__(connection2, [1, '+'])
        else:
            obj2.__setattr__(connection2, [0, '|'])


# test loop
def test():
    print('------------------------')
    print('Test.')
    print('------------------------')
    a = CCTransistor('T1')
    b = CCTransistor('T2')
    c = CCBattery('Bat1')
    d = CCCircuit('Circuit1')
    print(a)
    # print(b)
    print(c)
    print(d)
    d.connect(c, 'positive', a, 'collector')
    print(a)


# main loop
def main():
    print('------------------------')
    print('Main.')
    print('------------------------')


# main, calling main loop
if __name__ == '__main__':
    test()
    # main()


