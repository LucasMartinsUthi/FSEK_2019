#!/usr/bin/env python3
from ev3dev.ev3 import *
from threading import *
import time
import math

#------VARIÁVEIS DO PROGRAMA

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

#alinhado = False
Ativar_Emergencia = True
Estado = 2 #0 = inicio, 1 = ...
Cor_Anterior = 0
Tempo_Cor = 0
dif_temp = 0

#------FIM DAS VARIÁVEIS

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
        global Estado, Cor_Anterior, dif_temp
        while True:
            '''if 42 < ir.value() < 47:
                if Estado == 1:
                    Estado = -1
                    m1.stop(stop_action="brake")
                    m2.stop(stop_action="brake")
                    giraRobo(180, True)
                    Cor_Anterior = cor.value()
                    dif_temp = 0
                    Estado = 1
                else:
                    Emergencia()'''
            #print(str(ir.value()))
            time.sleep(1)

oi = vals()
oi.start()

def Emergencia():
    global Ativar_Emergencia
    if Ativar_Emergencia:
        m1.stop(stop_action="brake")
        m2.stop(stop_action="brake")
        m1.run_to_rel_pos(position_sp=-400,speed_sp=200,stop_action="brake")
        m2.run_to_rel_pos(position_sp=-400,speed_sp=200,stop_action="brake")
        time.sleep(3)
        giraRobo(120, True)
        m1.run_forever(speed_sp=300)
        m2.run_forever(speed_sp=300)

def AchouCano():
    cont = 0
    tempos_media = []
    while cont <= 30:
        m1.stop(stop_action="brake")
        m2.stop(stop_action="brake")

        leitura = ir.value()
        if leitura > 99:
            continue
        while leitura <= 45:
            leitura = ir.value()
            if leitura > 99:
                continue
            m1.run_forever(speed_sp=-70)
            m2.run_forever(speed_sp=70)

        m1.stop(stop_action="brake")
        m2.stop(stop_action="brake")

        tempo_giro = 0

        ss = "LEITURAS:\n"

        while True:
            leitura = ir.value()
            if leitura > 99:
                continue
            ss += "%d\n" %leitura
            m1.run_forever(speed_sp=70)
            m2.run_forever(speed_sp=-70)
            if leitura <= 45 and tempo_giro == 0:
                tempo_giro = time.time()
            else:
                if leitura > 45 and tempo_giro != 0:
                    break
                else:
                    print("ta entrando aqui")
            time.sleep(0.001)

        m1.stop(stop_action="brake")
        m2.stop(stop_action="brake")
        if tempo_giro != -1:
            tempos_media.append(time.time() - tempo_giro)
            print(str(time.time() - tempo_giro))
            cont += 1
        tempo_giro = 0
        giraRobo(40, True)

    '''ss = "LEITURAS:\n"
    for i in range(len(tempos_media)):
        ss += "%f\n" %tempos_media[i]'''
    arq = open("leituras.txt","w")
    arq.write(ss)
    arq.close()
    time.sleep(10)

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
#tdetempo = time.time()

while True:
    if Estado == 0:
        if cor.value() == 1 or cor2.value() == 1: #Preto
            if alinhar(1) == 1:
                Emergencia()
            else:
                m1.stop(stop_action="brake")
                m2.stop(stop_action="brake")
                Estado = 1

    elif Estado == 1:
        pass
        #andar na linha
    elif Estado == 2:
        m1.run_forever(speed_sp=300)
        m2.run_forever(speed_sp=-300)

        while True:
            if 45 < ir.value() < 60:
                m1.run_forever(speed_sp=100)
                m2.run_forever(speed_sp=100)
            elif ir.value() <= 45:
                AchouCano()

    '''
    if cor.value() == 0 or cor2.value() == 0: #Nenhuma cor
        Emergencia()

    elif cor.value() == 3 or cor2.value() == 3: #Verde
        Emergencia()'''



'''
if (time.time() - tdetempo) > 0.5:
    #print("US: %d" %ir.value())
    tdetempo = time.time()
'''

