#! /usr/bin/python3

#################################################
#                Exercises 02
# Vectors
# based on two books from Halliday and Tipler
#
# Rodrigo Nobrega
# 20170420-20170513
#################################################
__author__ = 'Rodrigo Nobrega'


# import modules
# from HTPhysics import HTVector
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
    
    # # TIPLER p.24 (pdf 32), answers p.703 (pdf 731)
    # # T53a
    # v5 = HTVector(m=10, theta=60)
    # v5.report()
    # # T53b
    # v6 = HTVector(m=25, theta=220)
    # v6.report()
    # # T53c
    # v7 = HTVector(m=40, theta=30)
    # v7.report()
    
    # # T54a
    # v8 = HTVector(x=8.5, y=-5.5)
    # v8.report()
    # # T54b
    # v9 = HTVector(x=-75, y=35)
    # v9.report()
    # # T54c
    # v10 = HTVector(m=50, theta=math.degrees(math.acos(40/50)))
    # v10.report()
    # # T55
    # v11 = HTVector(m=100,theta=math.degrees(math.acos(50/100)))
    # v11.report()
    # # T56
    # v12 = HTVector(x=250, y=-86.603)
    # v12.report()
    # # T57
    # vA = HTVector(x=3.4, y=4.7)
    # vB = HTVector(x=-7.7, y=3.2)
    # vC = HTVector(x=5.4, y=-9.1)
    # vA.report()
    # vB.report()
    # vC.report()
    # print('---')
    # print('Vector A: {}   2*A: {}'.format(vA.vector(), 2*vA.vector()))
    # print('Vector B: {}   4*B: {}'.format(vB.vector(), 4*vB.vector()))
    # print('Vector C: {}   3*C: {}'.format(vC.vector(), 3*vC.vector()))
    # print('---')
    # print('D + 2A - 3C + 4B = 0')
    # print('D = - 2A + 3C - 4B')
    # D = - (2 * vA.vector()) + (3 * vC.vector()) - (4 * vB.vector())
    # print('D = {}'.format(D))
    # print('---')
    # vD = HTVector(x=40.2, y=-49.5)
    # vD.report()
    # # T58
    # vA = HTVector(m=25, theta=330)
    # vB = HTVector(m=42, theta=40)
    # vR = HTVector(m=35, theta=0)
    # print('---')
    # print('2A + C - B = v(m=35, theta=0)')
    # print('Vector A: {}   2*A: {}'.format(vA.vector(), 2*vA.vector()))
    # print('Vector B: {}'.format(vB.vector()))
    # print('Vector result: {}'.format(vR.vector()))
    # print('C = B + v(m=35, theta=0) - 2A')
    # # print('Vector B-2A: {}'.format(vB.vector() - (2 * vA.vector())))
    # C = vB.vector() + vR.vector() - (2 * vA.vector())
    # vC = HTVector(x=C[0], y=C[1])
    # print('Vector C: {}'.format(vC.vector()))
    # vC.report()
    #
    # HALLIDAY p.56 (pdf 70), answers p.334 (pdf 349)
    # H3
    vA = HTVector(x=-25, y=40)
    vA.report()
    



# main, calling main loop
if __name__ == '__main__':
    main()
