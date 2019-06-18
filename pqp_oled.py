# Pot qui pense - CREPP 2019
# GPL V3.0
# www.crepp.org - patrick.pastor56@gmail.com

# intialisation du bus i2c
# scl=Pin5=GPIO5=d1 sda=Pin4=GPIO4=d2
#del  sys.modules['pqp_oled']

from machine import I2C, Pin
i2c= I2C(scl=Pin(5), sda=Pin(4)) # On crée une machine, piste horloge en 5 et piste données en 4

import ssd1306

# adresse Oled 0x3c ?
print(i2c.scan())

#initialisation de l'écran 128x64 à 0x3c
# oled=ssd1306.SSD1306_I2C(128,64, i2c, 0x3c)
oled=ssd1306.SSD1306_I2C(128,32, i2c, 0x3c)


# timer
import time
# time.sleep_ms(5000)

def affiche(Quoi):
    """Pour afficher quelque chose, représenté par Quoi"""
  oled.fill(0)
  oled.text(Quoi, 0, 10)
  oled.show()
  
def afficheXY(Quoi,x,y):
    """Pour afficher quelque chose à une position choisie par l'utilisateur"""
  oled.fill(0)	
  oled.text(Quoi, int(x), int(y))
  oled.show()
  
def surafficheXY(Quoi,x,y):
    """Pour afficher quelque chose par-dessus ce qui a déjà été affiché"""
  #oled.fill(0)
  oled.text(Quoi, int(x), int(y))
  oled.show()
  
def efface():
    """Pour effacer ce qui est affiché"""
  oled.fill(0)
  oled.show()
  
def  inverse(p):
    """Pour inverser selon p : si p = 1, on passe en fond blanc, si p = 0, on passe en fond noir"""
  oled.invert(p)
  
def test():
    """Pour afficher le texte "Bonjour il fait beau" """
  oled.fill(0)
  oled.text("Bonjour", 0, 0)
  oled.text("il fait beau", 0, 20)
  oled.show()
 
def machine(): 
 efface() # On efface ce qu'il aurait pu y avoir
 import machine, sys
 oled.text('version ' + sys.version, 0,10) # On écrit la version du système
 oled.text('CPU: ' + str(machine.freq()/1000000) + 'MHz', 0,20) # On écrit la fréquence de la CPU
 oled.show() 
 time.sleep_ms(2500) # On fait une pause
 # inversion fond blanc=1 / fond noir=0 
 oled.invert(1) # On inverse les couleurs
 time.sleep_ms(2000) # On fait une nouvelle pause
 # écran blanc=1 / noir=0 
 oled.fill(0) # On inverse à nouveau les couleurs
 oled.show() 
 





