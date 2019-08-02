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

alinhado = False

def giraRobo(graus, sentido): #Essa função gira o robo para algum lado
    razaoRobo = (2 * math.pi * 5.5) / (2 * math.pi * 2.71)
    if sentido:
        m2.run_to_rel_pos(position_sp=(razaoRobo*graus),speed_sp=180,stop_action="brake")
        m1.run_to_rel_pos(position_sp=-(razaoRobo*graus),speed_sp=180,stop_action="brake")
    else:
        m1.run_to_rel_pos(position_sp=(razaoRobo*graus),speed_sp=180,stop_action="brake")
        m2.run_to_rel_pos(position_sp=-(razaoRobo*graus),speed_sp=180,stop_action="brake")
    time.sleep(2)

class vals(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        global alinhado
        while True:
            if 42 < ir.value() < 47:
                if alinhado:
                    m1.stop(stop_action="brake")
                    m2.stop(stop_action="brake")
                    m1.run_to_rel_pos(position_sp=-5000,speed_sp=200,stop_action="brake")
                    m2.run_to_rel_pos(position_sp=-5000,speed_sp=200,stop_action="brake")
                    time.sleep(7)
                    m1.stop(stop_action="brake")
                    m2.stop(stop_action="brake")
                    giraRobo(87,False)
                    alinhado = False
                    time.sleep(2)
                else:
                    Emergencia()
                print("infra detectou")

oi = vals()
oi.start()

def Emergencia():
    m1.stop(stop_action="brake")
    m2.stop(stop_action="brake")
    m1.run_to_rel_pos(position_sp=-400,speed_sp=200,stop_action="brake")
    m2.run_to_rel_pos(position_sp=-400,speed_sp=200,stop_action="brake")
    time.sleep(3)
    giraRobo(120, True)
    m1.run_forever(speed_sp=300)
    m2.run_forever(speed_sp=300)

def alinhar(c): #Essa função alinha o lego a uma cor especifica c.
    time.sleep(0.03)
    if cor.value() == 1 and cor2.value() == 1:
        return 0
    while True:
        if cor.value() == c:
            m1.stop(stop_action="brake")
            m2.stop(stop_action="brake")
            while cor.value() == c:
                m1.run_forever(speed_sp=-50)
                m2.run_forever(speed_sp=-50)
            m1.stop(stop_action="brake")
            m2.stop(stop_action="brake")
            #m1.run_forever(speed_sp=-150)
            m2.run_forever(speed_sp=100)
            while cor2.value() != c:
                if cor2.value() == 0:
                    return 1
                if cor.value() != c:
                    m1.run_forever(speed_sp=70)
                else:
                    m1.stop(stop_action="brake")
            return 0

        if cor2.value() == c:
            m1.stop(stop_action="brake")
            m2.stop(stop_action="brake")
            while cor2.value() == c:
                m1.run_forever(speed_sp=-50)
                m2.run_forever(speed_sp=-50)
            m1.stop(stop_action="brake")
            m2.stop(stop_action="brake")
            m1.run_forever(speed_sp=100)
            #m2.run_forever(speed_sp=-150)
            while cor.value() != c:
                if cor.value() == 0:
                    return 1
                if cor2.value() != c:
                    m2.run_forever(speed_sp=70)
                else:
                    m2.stop(stop_action="brake")
            return 0

m1.run_forever(speed_sp=300)
m2.run_forever(speed_sp=300)
tdetempo = time.time()
while True:
    if (time.time() - tdetempo) > 0.5:
        #print("US: %d" %ir.value())
        tdetempo = time.time()

    if cor.value() == 1 or cor2.value() == 1: #Preto
        if alinhar(1) == 1:
            Emergencia()
        else:
            m1.stop(stop_action="brake")
            m2.stop(stop_action="brake")
            m1.run_to_rel_pos(position_sp=-600,speed_sp=300,stop_action="brake")
            m2.run_to_rel_pos(position_sp=-600,speed_sp=300,stop_action="brake")
            time.sleep(2.5)
            giraRobo(87,True)
            m1.run_forever(speed_sp=300)
            m2.run_forever(speed_sp=300)
            alinhado = True

    elif cor.value() == 0 or cor2.value() == 0: #Nenhuma cor
        Emergencia()

    elif cor.value() == 3 or cor2.value() == 3: #Verde
        Emergencia()




