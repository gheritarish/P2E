# Pot qui pense - CREPP 2019
# GPL V3.0
# www.crepp.org - yvoz.lg@gmail.com

import machine
import dht

t = dht.DHT22(machine.Pin(12)) 

def test():
	t.measure() 
	print(t.temperature())
	#print(t.humidity())

def get_temp():
	try:
		t.measure()
		tp = str(t.temperature())
		return tp
	except OSError:
		return "-1"

