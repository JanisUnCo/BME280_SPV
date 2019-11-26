import smbus2
import bme280
import time
import RPi.GPIO as GPIO
import random
import math
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


print("Sviecinats saja profesionalaja skripta, kas tev palidzes izmantot BMW280")
intro()
def intro():
    try:
        kv = int(input("""
    Izvelies darbibu:
    1 - Paspeleties ar pogam
    2 - Aprekinat gazes masu telpa/trauka + gazes atrumu
    Darbiba: """))

        if (kv == 1):
            sensinfo()

        if (kv == 2):
            kalk()

        if (kv < 1) or (kv > 2):
            print("Izvelies 1 vai 2")
            intro()

    except(ValueError):
        print("Nesaportu atbildi, megini velreiz!")
        intro()
    else:
        print("Nesaprotu atbildi, megini velreiz!")
        intro()

def sensinfo():
    port = 1
    address = 0x76
    bus = smbus2.SMBus(port)
    calibration_params = bms280.load_calibration_params(bus, address)
    data = bme280.sample(bus, address, calibration_params)
    GPIO.setup(13,GPIO.OUT) #lilla
    GPIO.setup(19,GPIO.OUT) #Balts
    GPIO.setup(26,GPIO.OUT) #Peleks
    p1 = 4
    p2 = 27
    p3 = 22
    GPIO.setup(p1, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(p2, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(p3, GPIO.IN, GPIO.PUD_UP)
    try:
        while True:
            if GPIO.input(4) == GPIO.LOW:
                GPIO.output(13,GPIO.HIGH)
                time.sleep(1)
                GPIO.output(13,GPIO.LOW)
                
            if GPIO.input(27) == GPIO.LOW:
                GPIO.output(19,GPIO.HIGH)
                time.sleep(1)
                GPIO.output(19,GPIO.LOW)

            if GPIO.input(22) == GPIO.LOW:
                GPIO.output(26,GPIO.HIGH)
                time.sleep(1)
                GPIO.output(26,GPIO.LOW)             

            else:
                GPIO.output(13,GPIO.LOW)
                GPIO.output(19,GPIO.LOW)
                GPIO.output(26,GPIO.LOW)

    except KeyboardInterrupt:
        print('/n')
        GPIO.cleanup()
    finally:
        GPIO.cleanup()

