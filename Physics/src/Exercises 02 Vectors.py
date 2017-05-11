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
import math


# main loop
def main():
    # # Concept 1: test vectors with opposed angles
    # v1 = HTVector(m=10, theta=60)
    # v2 = HTVector(m=10, theta=120)
    # v1.report()
    # v2.report()
    # v3 = HTVector(m=10, theta=240)
    # v4 = HTVector(m=10, theta=300)
    # v3.report()
    # v4.report()
    # print(v1.vector(), v2.vector(), v3.vector(), v4.vector())
    
    # # p.32, results p.731
    # # 53a
    # v5 = HTVector(m=10, theta=60)
    # v5.report()
    # # 53b
    # v6 = HTVector(m=25, theta=220)
    # v6.report()
    # # 53c
    # v7 = HTVector(m=40, theta=30)
    # v7.report()
    
    # # 54a
    # v8 = HTVector(x=8.5, y=-5.5)
    # v8.report()
    # # 54b
    # v9 = HTVector(x=-75, y=35)
    # v9.report()
    # # 54c
    # v10 = HTVector(m=50, theta=math.degrees(math.acos(40/50)))
    # v10.report()
    # # 55
    # v11 = HTVector(m=100,theta=math.degrees(math.acos(50/100)))
    # v11.report()
    # # 56
    # v12 = HTVector(x=250, y=-86.603)
    # v12.report()
    # 57
    vA = HTVector(x=3.4, y=4.7)
    vB = HTVector(x=-7.7, y=3.2)
    vC = HTVector(x=5.4, y=-9.1)
    vA.report()
    vB.report()
    vC.report()
    print('---')
    print('Vector A: {}   2*A: {}'.format(vA.vector(), 2*vA.vector()))
    print('Vector B: {}   4*B: {}'.format(vB.vector(), 4*vB.vector()))
    print('Vector C: {}   3*C: {}'.format(vC.vector(), 3*vC.vector()))
    print('---')
    print('D + 2A - 3C + 4B = 0')
    print('D = - 2A + 3C - 4B')
    D = - (2 * vA.vector()) + (3 * vC.vector()) - (4 * vB.vector())
    print('D = {}'.format(D))
    print('---')
    vD = HTVector(x=40.2, y=-49.5)
    vD.report()



# main, calling main loop
if __name__ == '__main__':
    main()
