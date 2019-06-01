#!/usr/bin/env python3
from ev3dev.ev3 import *
import time
import math

try:
    m1 = LargeMotor('outA')
    m2 = LargeMotor('outD')
    cor = ColorSensor('in1')
    cor2 = ColorSensor('in4')
    us = UltrasonicSensor('in2')
    us2 = UltrasonicSensor('in3')

    cor.mode = 'COL-COLOR'
    cor2.mode = 'COL-COLOR'
    us.mode = 'US-DIST-CM'
    us2.mode = 'US-DIST-CM'
except:
    print("")

cor_ant = [1, 0]
branco = 6
cores = []

for i in [1,2,3,4,5]:
    ncor = [i, 0]
    cores.append(ncor)

def giraRobo(graus, sentido):
    razaoRobo = (2 * math.pi * 5.5) / (2 * math.pi * 3)
    if sentido:
        m2.run_to_rel_pos(position_sp=(razaoRobo*graus),speed_sp=700,stop_action="brake")
        m1.run_to_rel_pos(position_sp=-(razaoRobo*graus),speed_sp=700,stop_action="brake")
    else:
        m1.run_to_rel_pos(position_sp=(razaoRobo*graus),speed_sp=700,stop_action="brake")
        m2.run_to_rel_pos(position_sp=-(razaoRobo*graus),speed_sp=700,stop_action="brake")
    time.sleep(1)

def ArrumarAngulo(temp_dif, quallado):
    tempinho_novo = temp_dif * 1000
    if quallado:
        m1.run_timed(time_sp=tempinho_novo, speed_sp=600)
    else:
        m2.run_timed(time_sp=tempinho_novo, speed_sp=600)
    time.sleep(temp_dif)
    m1.run_forever(speed_sp=600)
    m2.run_forever(speed_sp=600)

def FoundCor():
    

m1.run_forever(speed_sp=600)
m2.run_forever(speed_sp=600)

iterador, tempinho = 0, 0
umavez = [True, False, False]
while True:
    








