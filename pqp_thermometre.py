# Pot qui pense - CREPP 2019
# GPL V3.0
# www.crepp.org - yvoz.lg@gmail.com

import machine
import dht

t = dht.DHT22(machine.Pin(12)) # On crée une machine sur le canal 12, un capteur de température (dht: température ou humidité)

def test():
    """Pour mesurer et afficher la température"""
	t.measure() 
	print(t.temperature())
	#print(t.humidity())

def get_temp():
    """Pour récupérer la température et l'afficher sous forme de chaîne de caractère"""
	try:
		t.measure()
		tp = str(t.temperature())
		return tp
	except OSError:
		return "-1"

