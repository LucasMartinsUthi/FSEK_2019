#!/usr/bin/env python3
# so that script can be run from Brickman

# from ev3dev.ev3 import *
import math
from time import sleep

class Robot:
    def __init__(self, **kwargs):
        self.radius = kwargs.get('radius')
        self.name = kwargs.get('name')
        self.state = kwargs.get('state')

    def debug(self):
        for key, arg in self.__dict__.items(): 
            print key, "-", arg

    def odemetry(self):
        #calcular odometria do robô

    def moveCm(self):
        #calcular odometria do robô

    def rotateDegrees(self):
        #calcular odometria do robô

    def getSensor(self):
        #retornar valores dos sensores já tratados
        #pode chamar outras funções como hsv

    def hsv(self):

    def closeClaw(self):

    def openClaw(self):

    def stop(self):

    def preventNoise(self):

    def learnHolePositions(self):

    def learnTubesPositions(self):

    def funcaoFork(self):
        #teste de fork
        
    def funcaoFork2(self):





