#!/usr/bin/env python3
from ev3dev.ev3 import *
from threading import *
import time
import math

#Motors
m1 = LargeMotor('OutD') #Left_Motor
m2 = LargeMotor('OutC') #Right_Motor
m3 = MediumMotor('OutA') #Claw_Motor

#ColorSensors
cor = ColorSensor('in2') #Left_ColorSensor
cor.mode = 'COL-COLOR'
cor2 = ColorSensor('in4') #Right_ColorSensor
cor2.mode = 'COL-COLOR'

#Sensors 
ir = InfraredSensor('in1') #Infrared_Sensor
ir.mode = 'IR-PROX'
us = UltrasonicSensor('in3') #Ultrasonic_Sensor
us.mode = 'US-DIST-CM'



def rgbtohsv(rgb): #RGB to HSV
    r = float(rgb[0]/255.0)
    g = float(rgb[1]/255.0)
    b = float(rgb[2]/255.0)

    mx = max(r, g, b)
    mn = min(r, g, b)
    dif = float(mx - mn)
    if mx == mn:
        h = 0
    elif mx == r:
        h = float(60 * ((g-b)/dif) + 360) % 360
    elif mx == g:
        h = float(60 * ((b-r)/dif) + 120) % 360
    elif mx == b:
        h = float(60 * ((r-g)/dif) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = float(100*dif/mx)
    v = float(100*mx)
    
    h = round(h, 2)
    s = round(s, 2)
    v = round(v, 2)

    return [hsv]

def hsvtorgb(hsv): #HSV to RGB
    h = float(hsv[0])
    s = float(hsv[1]/100)
    v = float(hsv[2]/100)

    hi = h/60
    c = float(v*s)
    x = float(c*(1 - abs(((hi)%2)-1)))
    m = float(v-c)

    if 0 <= hi <= 1:
        ri, gi, bi = c, x, 0
    if 1 < hi <= 2:
        ri, gi, bi = x, c, 0
    if 2 < hi <= 3:
        ri, gi, bi = 0, c, x
    if 3 < hi <= 4:
        ri, gi, bi = 0, x, c 
    if 4 < hi <= 5:
        ri, gi, bi = x, 0, c  
    if 5 < hi <= 6:
        ri, gi, bi = c, 0, x  
    
    r = round((ri+m))
    g = round((gi+m))
    b = round((bi+m))

    return [rgb]

def rgbtohsl(rgb):  #RGB to HSL
    r = float(rgb[0]/255.0)
    g = float(rgb[1]/255.0)
    b = float(rgb[2]/255.0)

    mx = max(r, g, b)
    mn = min(r, g, b)
    dif = mx - mn:
    if mx == mn:
        h = 0
    elif mx == r:
        h = float(60 * ((g-b)/dif) + 360) % 360
    elif mx == g:
        h = float(60 * ((b-r)/dif) + 120) % 360
    elif mx == b:
        h = float(60 * ((r-g)/dif) + 240) % 360
    l = float(100*((mx + mn) / 2))
    if mx == 0 
        s = 0
    elif mn == 1
        s = 0
    else
        mod = (2*l-1)
        s = float(100*((2*mx - 2*l)/1-(abs(mod))))
    
    h = round(h,2)
    s = round(s,2)
    l = round(s,2)

    return [hsl]

def hsltorgb(hsl): #HSL to RGB
    h = float(hsl[0])
    s = float(hsl[1]/100)
    l = float(hsl[2]/100)

    c = float((1 - abs(2*l -1))*s)
    hi = float(h/60)
    x = float(c*(1 - abs((hi)%2)-1))
    m = float(l - c/2)

    if 0 <= hi <= 1:
        ri, gi, bi = c, x, 0
    if 1 < hi <= 2:
        ri, gi, bi = x, c, 0
    if 2 < hi <= 3:
        ri, gi, bi = 0, c, x
    if 3 < hi <= 4:
        ri, gi, bi = 0, x, c 
    if 4 < hi <= 5:
        ri, gi, bi = x, 0, c  
    if 5 < hi <= 6:
        ri, gi, bi = c, 0, x  
    
    r = round((ri+m))
    g = round((gi+m))
    b = round((bi+m))
    
    return [rgb]

def blakeLine(self): #Walk the black line to learning colors.
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
                print("color x: %d" %x)
            elif cor2.value() != x and y == -1:
                y = cor2.value()
                print("color y: %d" %y)
            elif cor2.value() != y and y != -1 and z == -1:
                z = cor2.value()
                print("color z: %d" %z)
    return [xyz]

def odometry(self)
    R = 7.5
    r = 2.85
    C = 2*math.pi*R #Robot
    c = 2*math.pi*r #Wheel
    rate = C/c
    return rate 

def odometrySensor(self)
    R = 12.5
    r = 2.85
    C = 2*math.pi*R #Robot
    c = 2*math.pi*r #Wheel
    rate = C/c
    return rate

def rotateRobot(degrees,way): #Rotate the robot with degree change.
    odometry()
    if way:
        m1.run_to_rel_pos(position_sp=-(rate*degrees),speed_sp=180,stop_action="brake")
        m2.run_to_rel_pos(position_sp=(rate*degrees),speed_sp=180,stop_action="brake")
    else:
        m1.run_to_rel_pos(position_sp=(rate*degrees),speed_sp=180,stop_action="brake")
        m2.run_to_rel_pos(position_sp=-(rate*degrees),speed_sp=180,stop_action="brake")
    time.sleep(2)

def rotateSensor(degrees,way): #Rotate the robot with degree sensor.
    odometrySensor()
    if way:
        m1.run_to_rel_pos(position_sp=-(rate*degrees),speed_sp=180,stop_action="brake")
        m2.run_to_rel_pos(position_sp=(rate*degrees),speed_sp=180,stop_action="brake")
    else:
        m1.run_to_rel_pos(position_sp=(rate*degrees),speed_sp=180,stop_action="brake")
        m2.run_to_rel_pos(position_sp=-(rate*degrees),speed_sp=180,stop_action="brake")
    time.sleep(2)