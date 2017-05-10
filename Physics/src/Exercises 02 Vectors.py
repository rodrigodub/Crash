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
    #
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
    #
    # 54a
    v8 = HTVector(x=8.5, y=-5.5)
    v8.report()
    # 54b
    v9 = HTVector(x=-75, y=35)
    v9.report()
    # 54c
    v10 = HTVector(x=8.5, y=-5.5)
    v10.report()



# main, calling main loop
if __name__ == '__main__':
    main()
