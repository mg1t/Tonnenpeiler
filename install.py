#Simples Installationsskript fuer die Pakete in Python3
#2020 DD4MG
#

import os
print("Installationsskript für den Tonnenpeiler\n")
print("\033[41mDiese Pythondatei muss in einer Systemkonsole ausgeführt werden!\033[0m")
print("\033[41mIst dies nicht der Fall bitte stoppen und in einer Systemkonsole neustarten!\033[0m")
print("\nInstallation wird mit \"Ja\" gestartet. \"Nein\" beendet das Skript.")
eingabe=input("Ihre Eingabe: ")

if eingabe=="Ja":
    os.system("sudo apt-get update")
    os.system("sudo apt-get upgrade")
    os.system("sudo apt-get install libusb-1.0-0-dev")
    os.system("sudo apt-get install rtl-sdr gr-osmosdr")
    os.system("sudo apt-get install python-gi-cairo")
    os.system("pip3 install pyrtlsdr")
    os.system("pip3 install numpy")
    os.system("pip3 install matplotlib")

    print("\n.\n.\n.\nInstallation der notwendigen Pakete abgeschlossen\n")
    
else:
    print("\n.\n.\n.\nInstallation abgebrochen\n")