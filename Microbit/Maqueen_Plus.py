#(c) 2022 Adrien Aurore
#basé sur Christophe Gueneau

from microbit import *
from time import sleep_ms
from machine import time_pulse_us
import struct

# Canal I2C
I2caddr = 0x10

def initI2C():
    version=0
    while version==0:
        i2c.write(I2caddr, bytearray([0x32]))
        version=(i2c.read(I2caddr, 1))[0]
    print("v", version)

# Fonctions motorisation
def motorSetPower(speedL, speedR): # [L: -255, R: +255]
    dirL   = 1 + (speedL > 0)
    dirR   = 1 + (speedR > 0)
    speedL = abs(speedL)
    speedR = abs(speedR)
    buf = bytearray([0x00, dirL, speedL, dirR, speedR])
    i2c.write(I2caddr, buf)

def motorSetCompensation(moteur, speed): # motor: 1=left / 2=right, speed 0-255
    buf = bytearray([0x07 + moteur, speed])
    i2c.write(I2caddr, buf)

def motorSetPID(switch): # 0 disable / 1 enable
    buf = bytearray([0x0A, switch])
    i2c.write(I2caddr, buf)
        
def motorReadPower():  # [L: -255, R: +255]
    buf = bytearray([0x00])
    i2c.write(I2caddr, buf)
    speeds = struct.unpack('>BBBB', i2c.read(I2caddr, 8))
    speedL = speeds[1] if speeds[0] == 2 else -speeds[1]
    speedR = speeds[3] if speeds[2] == 2 else -speeds[3]
    return [speedL, speedR]

def motorReadEncoders():  # Encoders are + even if maqueen is moving backwards 
    buf = bytearray([0x04])
    i2c.write(I2caddr, buf)
    encoders = struct.unpack('>HH', i2c.read(I2caddr, 8))
    return encoders # 1 tour = 78 ticks

# Fonctions phares
def pharesSetRGB(colourL, colourR):
    buf = bytearray([0x0b, colourL, colourR])
    i2c.write(I2caddr, buf)
    
# Fonctions capteurs sol
def groundReadLogique():
    buf = bytearray([0x1D])
    i2c.write(I2caddr, buf)
    line_d = struct.unpack('b', i2c.read(I2caddr, 1))
    masque = bytearray([0x01, 0x02, 0x04, 0x08, 0x10, 0x20])
    
    line = []
    for i in range(0, 6):
        make = 1 if (line_d[0] & masque[i]) else 0
        line.append(make)
    return line

def groundReadAnalog():
    buf = bytearray([0x1E])
    i2c.write(I2caddr, buf)
    line_d = struct.unpack('>HHHHHH', i2c.read(I2caddr, 12))
    return line_d

# Fonctions servo
def servoSet(number, angle): # number:0-2 , angle 0-180 (170)
    buf = bytearray([0x14 + number, angle])
    i2c.write(I2caddr, buf)
    
def servosSet(angle1, angle2, angle3): # number:0-2 , angle 0-180 (170)
    buf = bytearray([0x14, angle1, angle2, angle3])
    i2c.write(I2caddr, buf)
    
def servosRead(angle1, angle2, angle3): # number:0-2 , angle 0-180 (170)
    buf = bytearray([0x14])
    i2c.write(I2caddr, buf)
    servos = struct.unpack('>BBB', i2c.readfrom(I2caddr, 6))
    return servos

# Tests
if __name__ == '__main__':
    for i in range(1, 8) : # Motors test
        power = 50*(i%3-1)
        motorSetPower(power, power)
        sleep(400)
        print(power, motorReadPower(), motorReadEncoders())
    motorSetPower(0, 0)
    
    for i in range(8) : # RGB color range 0~7
        pharesSetRGB(i, 7-i)
        sleep(400)
    pharesSetRGB(0, 0)
    
    for i in range(8) : # Lecture capteurs ligne
        print(groundReadLogique(), groundReadAnalog())
        sleep(400)
