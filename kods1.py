import smbus2
import bme280
import time
import RPi.GPIO as GPIO
import random
import math
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#importe bibliotekas

print("Sviecinats saja profesionalaja skripta, kas tev palidzes izmantot BMW280")
intro()
def intro():
    #dod opciju izveleties darbibu
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
    #sagatavo BME280 datu lasisanai
    port = 1
    address = 0x76
    bus = smbus2.SMBus(port)
    calibration_params = bme280.load_calibration_params(bus, address)
    data = bme280.sample(bus, address, calibration_params)
    #Define pogu atrasanas vietu un diozu uz RPI
    GPIO.setup(13,GPIO.OUT) #lilla
    GPIO.setup(19,GPIO.OUT) #Balts
    GPIO.setup(26,GPIO.OUT) #Peleks
    p1 = 16
    p2 = 20
    p3 = 21
    #define pogas, ka pogas
    GPIO.setup(p1, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(p2, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(p3, GPIO.IN, GPIO.PUD_UP)
    try:
        while True:
            if GPIO.input(16) == GPIO.LOW:
                #nospiezot 1. pogu iedegeas 1. dieode un uz ekrana parada iegutos datus
                GPIO.output(13,GPIO.HIGH)
                print("Iegutos datus saglabaju.")
                #parada temperaturu
                print(data.temperature)
                #parada spiedienu
                print(data.pressure)
                #parada identifikaciju
                print(data.id)
                #parada laiku
                print(data.timestamp)
                #saglaba visus ieprieks mineots datus ka mainigos
                id1 = data.id
                id2 = data.timestamp
                id3 = data.temperature
                id4 = data.pressure
                time.sleep(1)
                #diode beidz spidet
                GPIO.output(13,GPIO.LOW)
                
            if GPIO.input(20) == GPIO.LOW:
                #nospiezot 2. pogu iedegas 2. lampina, datus parada bet nesaglaba
                GPIO.output(19,GPIO.HIGH)
                print("Iegutos datus neglabaju")
                print(data.temperature)
                print(data.pressure)
                print(data.id)
                print(data.timestamp)
                time.sleep(1)
                GPIO.output(19,GPIO.LOW)

            if GPIO.input(21) == GPIO.LOW:
                #nospiezot 3. pogu iedegas 3, lampina, parada visus saglabatos datus
                GPIO.output(26,GPIO.HIGH)
                print("Saglabatie dati")
                print(id1)
                print(id2)
                print(id3)
                print(id4)
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

def kalk():
    #sagatavo BME280 datu lasisanai
    port = 1
    address = 0x76
    bus = smbus2.SMBus(port)
    calibration_params = bme280.load_calibration_params(bus, address)
    data = bme280.sample(bus, address, calibration_params)
    #define R ka 8.31 jeb Bolcmana konstante
    R = 8.31
    try:
        while True:
            #dod izveleties gazi
            kv1 = int(input("""
Izvelies gazi:
1 - Gaiss
2 - Oglekla dioksids (Olgskaba gaze)
3 - Viss custom
Darbiba: """))

            if (kv1 == 1):
                #prasa telpas/traila tilpumu
                Vol1 = float(input("Ievadi telpas/trauka tilpumu kubikmetros: "))
                #define molamasu, saja gadijuma gaisam
                Mol1 = 28.97
                mass1 = (Mol1 * data.pressure * Vol1) / (R * (data.temperature + 273))
                #aprekina gazes masu telpa izmantojot darbibu = (gazes molmasa * iegutais spiediesn * tilpums) / (bolcmana konstante * (ieguta temperatura + 273))
                print("Gazes masa telpa = ", mass1, " kg.")
                vv21 = math.sqrt(3 * R * ((data.temperature + 273) / Mol1)
                #aprekina gazes atrumu telpa ar darbibu = kvadratsakne no (3 * bolcmana konstante * (ieguta temperatura + 273) / gazes molmasu)
                print("Gazes atrums telpa ir", vv21, " m/s")
                kalk()

            if (kv1 == 2):
                #tas pats, kas ieprieks, mainas molmasa
                Vol2 = float(input("Ievadi telpas/trauka tilpumu kubikmetros: "))
                Mol2 = 44.01
                mass2 = (Mol2 * data.pressure * Vol2) / (R * (data.temperature + 273))
                print("Gazes masa telpa = ", mass2, " kg.")
                vv222 = math.sqrt(3 * R * (data.temperature + 273) / Mol2)
                print("Gazes atrums telpa ir", vv222, " m/s" )
                kalk()

            if (kv1 == 3):
                #tas pats, kas ieprieks, tacu custom molmasa
                Vol3 = float(input("Ievadi telpas/trauka tilpumu kubikmetros: "))
                Mol3 = float(input("Ievadi gazes molmasu g/mol = "))
                mass3 = (Mol3 * data.pressure *Vol3) / (R * (data.temperature + 273))
                print("Gazes masa telpa = ", mass3, " kg.")
                vv333 = math.sqrt(3 * R * (data.temperature + 273) / Mol3)
                print("Gazes atrums telpa ir", vv333, " m/s" )
                kalk()

            if (kv1 < 1) or (kv1 > 3):
                print("Izvelies 1 vai 2 vai 3")
                kalk()
    
    except(ValueError):
        print("Nesaportu atbildi, megini velreiz!")
        kalk()
    else:
        print("Nesaprotu atbildi, megini velreiz!")
        kalk()

intro()