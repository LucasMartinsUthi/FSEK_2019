#!/usr/bin/env python3
from ev3dev.ev3 import *
from threading import *
import time
import math

m1 = LargeMotor('outD')
m2 = LargeMotor('outC')
cor = ColorSensor('in2')
cor2 = ColorSensor('in4')
ir = InfraredSensor('in1')
#us2 = UltrasonicSensor('in3')

cor.mode = 'COL-COLOR'
cor2.mode = 'COL-COLOR'
ir.mode = 'IR-PROX'
#us2.mode = 'US-DIST-CM'

x, y, z = -1, -1, -1

while True:
    if cor.value() != 6 and cor.value() != 6:
        m1.run_to_rel_pos(position_sp=360, speed_sp=500)
        m2.run_to_rel_pos(position_sp=360, speed_sp=570)
    else:
        m1.run_to_rel_pos(position_sp=360, speed_sp=570)
        m2.run_to_rel_pos(position_sp=360, speed_sp=500)
    if cor2.value() != 6 and cor2.value() != 1:
        if x == -1:
            x = cor2.value()
            print("cor x: %d" %x)
        elif cor2.value() != x and y == -1:
            y = cor2.value()
            print("cor y: %d" %y)
        elif cor2.value() != y and y != -1 and z == -1:
            z = cor2.value()
            print("cor z: %d" %z)
