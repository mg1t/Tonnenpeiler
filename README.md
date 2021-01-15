# Tonnenpeiler
Software für den Tonnenpeiler der HS-Koblenz 
geschrieben von Michael Gräf DD4MG


Verwendete Hardware:

RaspberryPi3 V2.0
Nema Stepper 12V
Stepper-Driver A4988
SDR-Stic: Nooelec

Aktueller Stand: 15.01.2020

Die Tonne dreht, Messungen werden ausgeführt.
Der Plot funktioniert, müsste jedoch um 90° gedreht werden.
Die Antenne tut ihren dienst, die Dämpfung ist aber nicht ausreichend. Feldversuche mit
zusätzlicher Erdung an der Hardware stehen aus.

Benutzung der Software:

Vor der ersten Ausführung müssen die eventuell fehlenden Python3 Pakete mit der Datei
"instal.py" nachinstalliert werden. dies geschieht mit dem Kommando: "python3 install.py"

Der Raspberry muss neu gestartet werden, damit die RTL-SDR-Treiber richtig geladen werden.
Wird dies nicht getan, kann sich der Raspberry aufhängen. (Hardwarereset)

Danach kann die Dataei "run_tonnenpeiler.py" ausgeführt werden. Diese läuft in einer
Endlosschleife. Wenn sie aus der Konsole mit "python3 run_tonnenpeiler.py" gestartet wurde,
kann sie mit "CMD+C" gestoppt werden.

Grafische Umsetzung kann mit PysimpleGUI umgesetzt werden
