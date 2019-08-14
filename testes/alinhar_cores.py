#!/usr/bin/env python3
from ev3dev.ev3 import *
import time

#deixar mais ou menos apontado pra direção do gasoduto

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
