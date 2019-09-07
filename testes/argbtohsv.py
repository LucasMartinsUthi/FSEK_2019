#!/usr/bin/env python3
from ev3dev.ev3 import *
from threading import *
import time
import math

m1 = LargeMotor('OutD')
m2 = LargeMotor('OutC')
cor = ColorSensor('in2')
cor2 = ColorSensor('in4')
#ir = InfraredSensor('in1')
#us = UltrasonicSensor('in3')

cor.mode = 'COL-COLOR'
cor2.mode = 'COL-COLOR'

def rgbtohsv(r, g, b): #RGB para HSV
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    dif = mx - mn:
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/dif) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/dif) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/dif) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = dif/mx
    v = mx
    return h, s, v

def rgbtohsl(r, g, b)   #RGB para HSL
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    dif = mx - mn:
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/dif) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/dif) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/dif) + 240) % 360
    l = (mx + mn) // 2
    if mx == 0 
        s = 0
    elif mn == 1
        s = 0
    mod = (2*l-1)
    else 
        s = (2*mx - 2*l)//1-(abs(mod))
    return h, s, l

def alinhar(): 
    time.sleep(0.03)
    if cor.value() == 1 and cor2.value() == 1: #ver
        print("esta alinhado")
    while True:
        if cor.value() == 1 and cor2.value() != 1: #ver
            m1.stop(stop_action="brake")
            m2.stop(stop_action="brake")
            while cor.value() == 1: #ver
                m1.run_forever(speed_sp = -50)
                m2.run_forever(speed_sp = -50)
            m1.stop(stop_action="brake")
            m2.stop(stop_action="brake")
            m2.run_forever(speed_sp = 100)    
            while cor2.value != 1: #ver
                if cor2.value() == 0:
                    return 1
                if cor.value() != 1: #ver
                    m1.run_forever(speed_sp = 70)
                else:
                    m1.stop(stop_action="brake")
            return 0
        
        if cor.value() != 1 and cor2.value() == 1: #ver
            m1.stop(stop_action="brake")
            m2.stop(stop_action="brake")
            while cor2.value() == 1: #ver
                m1.run_forever(speed_sp=-50)
                m2.run_forever(speed_sp=-50)
            m1.run_forever(speed_sp = 100)
            while cor.value() != 1: #ver
                if cor.value() == 0
                    return 1
                if cor2.value() !=:
                    m2.run_forever(speed_sp = 70)
                else:
                    m2.stop(stop_action="brake")
            return 0