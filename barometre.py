from mpl3115a2 import MPL3115A2
from machine import I2C, Pin

mpl = MPL3115A2(scl=Pin(5), sda=Pin(4), mode=1) # On définit une machine sur le canal 4, un capteur de pression

def baro():
    """On mesure et on imprime la pression, puis la température"""
	pressure = mpl.pressure()
	print (pressure)

	temperature = mpl.temperature()
	print (temperature)
