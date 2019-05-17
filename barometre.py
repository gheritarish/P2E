from mpl3115a2 import MPL3115A2
from machine import I2C, Pin

mpl = MPL3115A2(scl=Pin(5), sda=Pin(4), mode=1)

def baro():
	pressure = mpl.pressure()
	print (pressure)

	temperature = mpl.temperature()
	print (temperature)
