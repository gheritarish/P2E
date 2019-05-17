# Pot qui pense - CREPP 2019
# GPL V3.0
# www.crepp.org - yvoz.lg@gmail.com

import machine
import bh1750

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4)) # On définit une machine à deux canaux, horloge en 5, données en 4
lum = bh1750.BH1750(i2c)

def test():
    """Mesure la luminosité et l'affiche"""
	print(lum.lecture_lumiere(bh1750.MODE_CONTINU_HAUTE_RESOLUTION))

