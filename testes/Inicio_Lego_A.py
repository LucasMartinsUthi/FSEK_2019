#!/usr/bin/env python3
from ev3dev.ev3 import *
import time
import math


'''

O objetivo dessa programação é fazer com que o lego que está na terra consiga ter uma direção no inicio e
ajustar a sua posição com o mapa, porém ela somente ajusta o angulo com a linha preta por hora.

'''

m1 = LargeMotor('outD')
m2 = LargeMotor('outA')
cor = ColorSensor('in4')
cor2 = ColorSensor('in1')
us = UltrasonicSensor('in2')
#us2 = UltrasonicSensor('in3')

cor.mode = 'COL-COLOR'
cor2.mode = 'COL-COLOR'
us.mode = 'US-DIST-CM'
#us2.mode = 'US-DIST-CM'

def giraRobo(graus, sentido): #Função que faz o lego girar
    razaoRobo = (2 * math.pi * 5.5) / (2 * math.pi * 3)
    if sentido:
        m2.run_to_rel_pos(position_sp=(razaoRobo*graus),speed_sp=700,stop_action="brake")
        m1.run_to_rel_pos(position_sp=-(razaoRobo*graus),speed_sp=700,stop_action="brake")
    else:
        m1.run_to_rel_pos(position_sp=(razaoRobo*graus),speed_sp=700,stop_action="brake")
        m2.run_to_rel_pos(position_sp=-(razaoRobo*graus),speed_sp=700,stop_action="brake")
    time.sleep(1)

#Essa função pega a relação de tempo entre os sensores de cor e arruma o angulo. (tem que ajustar os parametros)
def ArrumarAngulo(temp_dif, quallado):
    tempinho_novo = temp_dif * 400
    if quallado:
        m1.run_timed(time_sp=tempinho_novo, speed_sp=300)
        m2.run_timed(time_sp=tempinho_novo, speed_sp=-300)
    else:
        m1.run_timed(time_sp=tempinho_novo, speed_sp=-300)
        m2.run_timed(time_sp=tempinho_novo, speed_sp=300)
    time.sleep(temp_dif+4)

#Essa função é chamada para alinhas o lego com uma certa cor c que o sensor detectar, nesse caso, preto.
def alinhar(c):
    while True:
        if cor.value() == c:
            temp = time.time()
            while cor2.value() != c:
                pass
            ArrumarAngulo(time.time()-temp, False)
            return 0

        if cor2.value() == c:
            temp = time.time()
            while cor.value() != c:
                pass
            ArrumarAngulo(time.time()-temp, True)
            return 0

#Essa função serviria para ele ter alguma direção para ir quando iniciar, visto que o lego iniciará numa posição
#aleatoria a cada partida. Porém nao está funcionando corretamente, tem que ajustar
'''
cont = 0
while us.value() > 500 and cont <= 180:
    m1.run_to_rel_pos(position_sp=5,speed_sp=500,stop_action="brake")
    m2.run_to_rel_pos(position_sp=-5,speed_sp=500,stop_action="brake")
    time.sleep(0.1)
    cont += 1
'''
m1.run_forever(speed_sp=300)
m2.run_forever(speed_sp=300)

while True:
    #Se algum detectar preto, ele chama a função alinhar..
    if cor.value() == 1 or cor2.value() == 1:
        alinhar(1)
        m1.run_forever(speed_sp=300)
        m2.run_forever(speed_sp=300)
        print("Achou preto")

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
#Esse elif serve para caso ache algo diferente de branco, ele chame a funcao alinhar para alinhar o lego
#Porem, o sensor nao está detectando o branco corretamente..












