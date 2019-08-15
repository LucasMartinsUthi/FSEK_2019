#!/usr/bin/env python3
from ev3dev.ev3 import *
import time, math

m1 = LargeMotor('outD')
m2 = LargeMotor('outC')
cor = ColorSensor('in2')
cor2 = ColorSensor('in4')

#deixar mais ou menos apontado pra direção do gasoduto

def alinhar(c): #Essa função alinha o lego a uma cor especifica c.
    m1.run_forever(speed_sp=-50)
    m2.run_forever(speed_sp=-50)
    time.sleep(2)
    m1.stop(stop_action="brake")
    m2.stop(stop_action="brake")
    m1.run_forever(speed_sp=50)
    m2.run_forever(speed_sp=50)
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

if cor.value() == cor2.value():
    cor_anterior = cor.value()

while True: #enquanto nao chegar, ajustar para parar quando chegar
    m1.run_forever(speed_sp=300)
    m2.run_forever(speed_sp=300)

    if cor.value() != cor_anterior:
        alinhar(cor.value())
        cor_anterior = cor.value()
    elif cor2.value() != cor_anterior:
        alinhar(cor2.value())
        cor_anterior = cor2.value()

#teoricamente ele vai tentar ficar alinhado com cada cor, pode ter algum erro, da uma olhada

