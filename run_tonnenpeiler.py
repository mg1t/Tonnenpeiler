# -*- coding: utf-8 -*-
#
#Tonnenpeiler V1.3 DD4MG 2021
#Software für RaspberryPi
#
#Hardware:
#RaspberryPi3 V2.0
#Nema Stepper 12V
#Stepper-Driver A4988
#SDR-Stic: Nooelec
#
#
#
#eventuell benötigte Software mit install.py installieren
#
#
#Gewünschte Mittenfrequenz kann hier eingestellt werden.
#Werte müssen in Hz angegeben sein
_center_frequency_ =91.7e6
#
#Zusätzlich kann der PraAmp im SDR eingestellt werden.
# "auto" für Automatik, 1 bis 10 für manuell.
_sdr_gain_="auto"
#
#Der SDR Stick muss wiessen wie viele Samples er Messen soll.
#Je mehr Samples, desto genauer das Ergebnis der Messung
# !!!! Achtung !!!!
# _Minimum_ 129 Samples eintagen, sonst geht der RaspberryPi
#in Kernelpanik und muss hardwaremäßig resettet werden
_sdr_samples_ = 1*512
#


#Libary für plotten
from pylab import *
#Libary für RTL-SDR-Stick
from rtlsdr import *
#Achtung! Minimum 129 Samples aufnehmen lassen
#Sonst Kernelprobleme auf Raspi!!!!!
#
#Matheumgebung
import numpy as np
#Libary 2 zum Plotten
import matplotlib.pyplot as plt
#Libary für Zeiten
import time


#debug = True lässt die aktuellen Schritte auf der Konsole ausgeben
debug=False



#definieren der Stepper-Winkel
_STEP_ANGLE_=1.8

#Einstellen der GPIOs
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD) #Boardpins
GPIO.setwarnings(False) #meine Hardware, meine Regeln

_STEP_PIN_=16
_DIRECTION_PIN_=18

GPIO.setup(_STEP_PIN_, GPIO.OUT)
GPIO.setup(_DIRECTION_PIN_, GPIO.OUT)

GPIO.output(_STEP_PIN_, GPIO.LOW)
GPIO.output(_DIRECTION_PIN_, GPIO.LOW)

#liste mit Schritten erzeugen
schritte = np.arange(0, (2 * np.pi - _STEP_ANGLE_/57.29578), _STEP_ANGLE_/57.29578) 

#sdr call

sdr = RtlSdr()
if debug: print("sdr called");

# sdr einstellen
sdr.sample_rate = 2.4e6 #nicht verändern
sdr.center_freq = _center_frequency_
sdr.gain = _sdr_gain_

print("[R82XX] Warte auf PLL-Lock...")

#Begin der Dauermessung

while(True):
    
    messungen=[] #leere Liste fuer neue Werte
    
    for position in schritte:
        if debug: print(position,end="")
        #sampling
        samples = sdr.read_samples(_sdr_samples_) #minimum 129!!!!!!
        #Achtung Kernelpanik!!!!!!!!
        if debug: print(",sampling done",end="")
        #fft der daten
        fft_samples=np.fft.fft(samples)
        if debug: print(",fft done",end="")
        avg=mean(abs(fft_samples))
        if debug: print(",meaning done",end="")
        messungen.append(avg)
        if debug: print(",append done",end="")
        plt.polar(position,avg,"g.")
        
        GPIO.output(_STEP_PIN_, GPIO.HIGH)
        #Step Pin für 2ms "high" lassen
        time.sleep(0.002)
        GPIO.output(_STEP_PIN_, GPIO.LOW)
        if debug: print(",rotating done")

    maximum=max(messungen)
    if debug: print("Maximum: ",maximum)
    maximum_pos=messungen.index(maximum)
    if debug: print("Position: ",maximum_pos)
    maximum_angle=schritte[maximum_pos]

    print("Maximum bei ",maximum_angle*57.29578," °")
    plt.pause(0.0001)
    plt.clf()
    
#wird nie erreicht aufgrund while(True)
#wird aber vom Raspi verkraftet
sdr.close()
if debug: print("sdr closed");


