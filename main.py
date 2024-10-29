# Imports go at the top
from microbit import *
import sys
import math
import time
import log # type: ignore

# +++ SBC MotorDriver +++
class Motor:
    A = 0x1
    B = 0x2

class Dir:
    forward = 0x1
    backward = 0x2

class Servo:
    S0 = 0x1
    S1 = 0x2
    S2 = 0x3

PWMA = pin8
AIN1 = pin13
AIN2 = pin12
PWMB = pin16
BIN1 = pin14
BIN2 = pin15
S0_PIN = pin0
S1_PIN = pin1
S2_PIN = pin2

class MotorDriver:
    @staticmethod
    def MotorRun(m, index, speed: int) -> None:
        speed = speed * 64 - 1  # map 0 to 1023

        if m == Motor.A:
            #pins.analogWritePin(PWMA, speed)
            PWMA.write_analog(speed)
            if index == Dir.forward:
                #pins.digitalWritePin(AIN1, 0)
                #pins.digitalWritePin(AIN2, 1)
                AIN1.write_digital(0)
                AIN2.write_digital(1)
            else:
                #pins.digitalWritePin(AIN1, 1)
                #pins.digitalWritePin(AIN2, 0)
                AIN1.write_digital(1)
                AIN2.write_digital(0)
        else:
            #pins.analogWritePin(PWMB, speed)
            if index == Dir.forward:
                #pins.digitalWritePin(BIN1, 0)
                #pins.digitalWritePin(BIN2, 1)
                BIN1.write_digital(0)
            else:
                #pins.digitalWritePin(BIN1, 1)
                #pins.digitalWritePin(BIN2, 0)
                BIN1.write_digital(1)
                BIN2.write_digital(0)

    @staticmethod
    def MotorStop(m) -> None:
        if m == Motor.A:
            #pins.analogWritePin(PWMA, 0)
            PWMA.write_digital(0)
        else:
            #pins.analogWritePin(PWMB, 0)
            PWMB.write_digital(0)

    @staticmethod
    def ServosTurnZero(s: Servo) -> None:
        if s == Servo.S0:
            #pins.servoWritePin(S0_PIN, 0)
            S0_PIN.write_analog(0)
        elif s == Servo.S1:
            #pins.servoWritePin(S1_PIN, 0)
            S1_PIN.write_analog(0)
        else:
            #pins.servoWritePin(S2_PIN, 0)
            S2_PIN.write_analog(0)
            
    @staticmethod        
    def servo_write( servo, angle):
        pulse_width = (angle * 1800 // 180) + 600
        servo.write_analog(pulse_width)
    
    @staticmethod
    def ServosTurnFull(s: Servo) -> None:
        if s == Servo.S0:
            #pins.servoWritePin(S0_PIN, 180)
            S0_PIN.write_analog(180)
        elif s == Servo.S1:
            #pins.servoWritePin(S1_PIN, 180)
            S1_PIN.write_analog(180)
        else:
            #pins.servoWritePin(S2_PIN, 180)
            S2_PIN.write_analog(180)

    @staticmethod
    def ServoStop(s: Servo) -> None:
        if s == Servo.S0:
            #pins.servoSetPulse(S0_PIN, 0)
            S0_PIN.write_analog(0)
        elif s == Servo.S1:
            #pins.servoSetPulse(S1_PIN, 0)
            S1_PIN.write_analog(0)
        else:
           #pins.servoSetPulse(S2_PIN, 0)
            S2_PIN.write_analog(0)

    @staticmethod
    def ServoTurnAngle(s: Servo, angle: int) -> None:
        temp = angle * 10 + 500  # 0.5ms - 2.5ms
        if s == Servo.S0:
            #pins.servoSetPulse(S0_PIN, temp)
            MotorDriver.servo_write(Servo.S0 , temp)
        elif s == Servo.S1:
            #pins.servoSetPulse(S1_PIN, temp)
            MotorDriver.servo_write(Servo.S1 , temp)
        else:
            #pins.servoSetPulse(S2_PIN, temp)
            MotorDriver.servo_write(Servo.S2 , temp)

# --- SBC MotorDriver ---

# +++ mPy-POC-2 +++
prev_angle = 0
prev_time = 0
prev_head = 0

def get_angle():
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    angle = math.atan2(y, x) * 180 / math.pi
    return angle

def get_angular_velocity():
    current_angle = get_angle()
    current_time = time.ticks_ms()
    delta_angle = current_angle - prev_angle
    delta_time = (current_time - prev_time) / 1000  # Convert ms to seconds
    return delta_angle / delta_time

def getAVH():
    return 0
def turnStart():
    MotorDriver.MotorRun(Motor.A, Dir.forward, 8)
    MotorDriver.MotorRun(Motor.B, Dir.backward, 8)
def turnStop():
    MotorDriver.MotorStop(Motor.B)
    MotorDriver.MotorStop(Motor.B)
def getDeltaH():
    return 0

def getCompH():
    return 0
def getAV():
    return 0
    
el = 0
display.show(Image.HEART)

compass.calibrate()
ch = compass.heading()
log.set_mirroring(True)


def on_forever():
    if pin_logo.is_touched():
        display.show(Image.HAPPY)
        sys.exit()
        
    turnStart()
    av = get_angular_velocity()
    ch = compass.heading()
    turnStop()
    
    log.set_labels('av', 'ch', timestamp=log.MILLISECONDS)
    log.add({'av':av, 'ch':ch})
# +++ mPy-POC-2 +++

while True:
    on_forever()

