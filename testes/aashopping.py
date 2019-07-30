#!/usr/bin/env python3

import evdev
import ev3dev.auto as ev3
import threading
import time

#teste de pull

garra = ev3.MediumMotor(ev3.OUTPUT_B)
memoria = True

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

def scale(val, src, dst):
    return (float(val - src[0]) / (src[1] - src[0])) * (dst[1] - dst[0]) + dst[0]

def scale_stick(value):
    return scale(value,(0,255),(-1000,1000))

def dc_clamp(value):
    return clamp(value,-1000,1000)

print("Finding ps4 controller...")
devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
ps4dev = devices[0].fn

gamepad = evdev.InputDevice(ps4dev)

forward_speed = 0
side_speed = 0
running = True

class MotorThread(threading.Thread):
    def __init__(self):
        self.right_motor = ev3.LargeMotor(ev3.OUTPUT_A)
        self.left_motor = ev3.LargeMotor(ev3.OUTPUT_D)
        threading.Thread.__init__(self)

    def run(self):
        print("Engine running!")
        while running:
            self.right_motor.run_forever(speed_sp=dc_clamp(forward_speed+side_speed))
            self.left_motor.run_forever(speed_sp=dc_clamp(-forward_speed+side_speed))
        self.right_motor.stop()
        self.left_motor.stop()

motor_thread = MotorThread()
motor_thread.setDaemon(True)
motor_thread.start()

for event in gamepad.read_loop():
    if event.type == 3:
        if event.code == 0:
            forward_speed = -scale_stick(event.value)
        if event.code == 1:
            side_speed = -scale_stick(event.value)
        if side_speed < 100 and side_speed > -100:
            side_speed = 0
        if forward_speed < 100 and forward_speed > -100:
            forward_speed = 0

    if event.type == 1 and event.code == 305 and event.value == 1:
        if memoria:
            garra.run_timed(time_sp=1700, speed_sp=-100)
            time.sleep(1.8)
            garra.stop(stop_action="brake")
            memoria = False
        else:
            garra.run_timed(time_sp=1200, speed_sp=100)
            time.sleep(1.3)
            garra.stop(stop_action="brake")
            memoria = True


