# Imports go at the top
from microbit import *
from main import Motor, Dir
#"""
class Motor:
    A = 0x1
    B = 0x2

class Dir:
    forward = 0x1
    backward = 0x2
#"""    
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

