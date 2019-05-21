# Pot qui pense - CREPP 2019
# GPL V3.0
# www.crepp.org - yvoz.lg@gmail.com

import machine
from ads1x15 import ADS1115

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4)) # On définit une machine, horloge en 5, données en 4
can = ADS1115(i2c=i2c, address=72, gain=0)

def test():
    """On lit les données du CAN"""
	a0 = can.read(rate=0, channel1=0)
	print(a0)

def get_a0():
    """On essaie de lire les données du channel 0 du CAN que l'on renvoie, sinon on renvoie une erreur"""
	try:
		a0 = can.read(rate=0, channel1=0)
		return a0
	except OSError:
		return -1

def get_a1():
    """On essaie de lire les données du channel 1 du CAN que l'on renvoie, sinon on renvoie une erreur"""
	try:
		a1 = can.read(rate=0, channel1=1)
		return a1
	except OSError:
		return -1

# Gain 0 : 6.144v
# Dividing 6.144 volts by 32767 yields a scale factor of 0.1875 mV per bit.
# Pont diviseur : 4.2 / 3.0 = 1.4

def get_battery():
    """On cherche à savoir le niveau de batterie du CAN à partir des données du channel 1"""
	pts = get_a1()
	if pts > 0:
		vts = round(pts * 0.1875 * 1.4 / 10) / 100 # en Volt
		return vts
	else:
		return -1
