#!/usr/bin/env python3
from ev3dev.ev3 import *
import time
import math
from threading import *

'''

O objetivo dessa programação é fazer com que o lego que está na terra consiga ter uma direção no inicio e
ajustar a sua posição com o mapa, porém ela somente ajusta o angulo com a linha preta por hora.

E está com um problema em que algumas vezes, ele nao acha a linha preta com o outro sensor.

Esse código nao funciona com a diferença por tempo entre um sensor e outro, ele funciona travando o motor do lado
do primeiro sensor que achou o preto e ligando o motor do sensor que ainda nao achou até ele achar

'''

m1 = LargeMotor('outD')
m2 = LargeMotor('outC')
cor = ColorSensor('in2')
cor2 = ColorSensor('in4')
us = UltrasonicSensor('in1')
#us2 = UltrasonicSensor('in3')

cor.mode = 'COL-COLOR'
cor2.mode = 'COL-COLOR'
us.mode = 'US-DIST-CM'
#us2.mode = 'US-DIST-CM'
'''
class vals(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        tempop = time.time()
        while True:
            if (time.time() - tempop) > 0.5:
                print("S1: %d" %cor.value())
                print("S2: %d" %cor2.value())
                tempop = time.time()

oi = vals()
oi.start()
'''

def giraRobo(graus, sentido): #Essa função gira o robo para algum lado
    razaoRobo = (2 * math.pi * 5.5) / (2 * math.pi * 3)
    if sentido:
        m2.run_to_rel_pos(position_sp=(razaoRobo*graus),speed_sp=700,stop_action="brake")
        m1.run_to_rel_pos(position_sp=-(razaoRobo*graus),speed_sp=700,stop_action="brake")
    else:
        m1.run_to_rel_pos(position_sp=(razaoRobo*graus),speed_sp=700,stop_action="brake")
        m2.run_to_rel_pos(position_sp=-(razaoRobo*graus),speed_sp=700,stop_action="brake")
    time.sleep(1)

def alinhar(c): #Essa função alinha o lego a uma cor especifica c.
    time.sleep(0.03)
    if cor.value() == 1 and cor2.value() == 1:
        return 0
    tdetempo = time.time()
    while True:
        if cor.value() == c:
            m1.stop(stop_action="brake")
            m2.stop(stop_action="brake")
            #m1.run_forever(speed_sp=-150)
            m2.run_forever(speed_sp=150)
            while cor2.value() != c:
                if (time.time() - tdetempo) > 0.7:
                    print("S2: %d" %cor2.value())
                    tdetempo = time.time()
                if cor.value() != c:
                    m1.run_forever(speed_sp=100)
                else:
                    m1.stop(stop_action="brake")
            return 0

        if cor2.value() == c:
            m1.stop(stop_action="brake")
            m2.stop(stop_action="brake")
            m1.run_forever(speed_sp=150)
            #m2.run_forever(speed_sp=-150)
            while cor.value() != c:
                if (time.time() - tdetempo) > 0.7:
                    print("S1: %d" %cor.value())
                    tdetempo = time.time()
                if cor2.value() != c:
                    m2.run_forever(speed_sp=100)
                else:
                    m2.stop(stop_action="brake")
            return 0

'''
cont = 0
while us.value() > 500 and cont <= 180:
    m1.run_to_rel_pos(position_sp=5,speed_sp=500,stop_action="brake")
    m2.run_to_rel_pos(position_sp=-5,speed_sp=500,stop_action="brake")
    time.sleep(0.1)
    cont += 1
'''
#Essa função tenta dar um início ao robo, visto que o mesmo inicia em posição aleatoria, porém nao está
#funcionando corretamente

#m1.run_forever(speed_sp=300)
#m2.run_forever(speed_sp=300)
tdetempo = time.time()
while True:
    global tdetempo
    if (time.time() - tdetempo) > 0.6:
        print("US: %d" %us.value())
        tdetempo = time.time()
    '''
    if cor.value() == 1 or cor2.value() == 1:
        alinhar(1)
        print("Achou preto")
        #giraRobo(90,True)
        m1.run_forever(speed_sp=300)
        m2.run_forever(speed_sp=300)
        time.sleep(1.5)
    '''
    '''elif cor.value() != 6 or cor2.value() != 6:
        if cor.value() == 6:
            alinhar(cor2.value())
            print("Achou " + str(cor2.value()))
        else:
            alinhar(cor.value())
            print("Achou " + str(cor.value()))
        giraRobo(180, True)
        time.sleep(100)
    '''
#Esse ultimo elif deveria ajustar o robo a qualquer cor diferente de branco, porém ele nao está identificando o
#branco corretamente

