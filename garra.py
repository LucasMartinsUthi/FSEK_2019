#!/usr/bin/env python3
from ev3dev.ev3 import *
import time

m1 = MediumMotor('outA')
t1 = TouchSensor('in1')

b = 0
try:
    with open('backup.txt', 'r') as arq:
        valAr = eval(arq.read())
        if 0 <= valAr <= 1:
            b = valAr
        else:
            b = 0
        arq.close()
except IOError:
    pass

def back(b):
    arq = open('backup.txt', 'w')
    arq.write(str(b))
    arq.close()

print("iniciou")
while True:
    if(t1.value()):
        if b == 0:
            m1.run_to_rel_pos(position_sp=60, speed_sp=200)
            print("fechar")
            time.sleep(1)
            b = 1
            back(b)
        elif b == 1:
            m1.run_to_rel_pos(position_sp=-60, speed_sp=200)
            print("abrir")
            time.sleep(1)
            b = 0
            back(b)
