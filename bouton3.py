# Dome qui pense - APALA 2019/03/26
# GPL V3.0
# www.apala.fr - antoine.cousin@apala.fr

from time import sleep
import machine
from ds3231_port import DS3231
from machine import I2C, Pin, RTC
import time
import oled
import pqp_horloge
import ssd1306
import ds18b20
import onewire, ds18x20
import dht


d = dht.DHT22(machine.Pin(3)) 
hum = 0
temp = 0

d.measure() # On fait une mesure
hum = d.humidity() # On stocke la valeur de l'humidité dans une variable hum
temp = d.temperature() # On stocke la valeur de la température dans une variate temp

led = Pin(2, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_UP) # Bouton configuré pour de l'input, avec un pull up resistor
i = 0
j = 0
start = time.ticks_ms()

i2c= I2C(scl=Pin(5), sda=Pin(4)) # On configure une machine, horloge en 5, données en 4
oled=ssd1306.SSD1306_I2C(128,32, i2c, 0x3c)
ds3231=DS3231(i2c)


dat = machine.Pin(1)i # On crée une machine en 1
ds = ds18x20.DS18X20(onewire.OneWire(dat))

relaisfeu = machine.Pin(13, machine.Pin.OUT) # Un premier relais, en 13
relaissol = machine.Pin(12, machine.Pin.OUT) # Un second relais, en 12
relaisfeu.off()
relaissol.off()


#relaisfeu.on()
#relaisfeu.off()
#relaissol.on()
#relaissol.off()


while True:
    # Boucle infinie, pour faire ça en continu
	if button.value() == 0:
		delta = time.ticks_diff(time.ticks_ms(), start) # On calcule une différence de temps
		
		if delta <= 200:
                    # Si la différence de temps est faible
			i = i + 1 # On incrémente i
			led.off() # On éteint la led
			print(delta) # On affiche la différence de temps
			print ('appuis court', i) # On affiche i
			
		if i == 1:
			oled.fill(0)
			oled.text("APALA", 0, 15) # On écrit APALA sur l'écran
			oled.show()
			print ('mode', 1)
			time.sleep_ms(100) # On attend 100 ms
			
		if i == 2:
			oled.fill(0)
			oled.text("Implantation", 0, 10) # On écrit Implantation sur l'écran
			oled.text("Alimentaire", 0, 25) # On écrit Alimentaire sur l'écran
			oled.show()
			print ('mode', 2)
			time.sleep_ms(100) # On attend 100 ms
			
		if i == 3:
			(an, mois, jour, hh, mm, ss, jsem, zorbec) = ds3231.get_time()
			oled.fill(0)
			oled.text("Heure", 0, 0)
			oled.text( str(hh) + ':' + str(mm) + ':' + str(ss), 0, 20) # On écrit l'heure sur l'écran
			oled.show()
			print ('mode', 3)
			time.sleep_ms(100) # On attend 100 ms
			
		if i == 4:
			oled.fill(0)
			oled.text("Humidite air", 0, 0)
			oled.text(str(hum) + " %HR", 0, 20) # On affiche l'humidité de l'air
			oled.show()
			print ('mode', 4)
			time.sleep_ms(100) # On attend 100 ms
			
		if i == 5:
			oled.fill(0)
			oled.text("Temperature eau", 0, 0)
			roms = ds.scan()
			ds.convert_temp()
			eau = ds.read_temp(roms[0])
			oled.text(str(eau) + " degre", 0, 20) # On affiche la température de l'eau
			oled.show()
			print ('mode', 5)
			time.sleep_ms(100) # On attend 100 ms
			
		if i == 6:
			oled.fill(0)
			oled.text("Temperature sol", 0, 0)
			roms = ds.scan()
			ds.convert_temp()
			sol = ds.read_temp(roms[1])
			oled.text(str(sol) + " degre", 0, 20) # On affiche la température du sol
			oled.show()
			print ('mode', 6)
			time.sleep_ms(100) # On attend 100 ms
			
		if i == 7:
			oled.fill(0)
			oled.text("Temperature air", 0, 0)
			oled.text(str(temp) + " degre", 0, 20) # On affiche la température de l'air
			oled.show()
			print ('mode', 7)
			time.sleep_ms(100) # On attend 100 ms
			
		if i == 8:
			oled.fill(0)
			oled.text("Pompe Feu", 0, 15) # On écrit Pompe Feu sur l'écran
			oled.show()
			print ('mode', 8)
			time.sleep_ms(100) # On attend 100 ms
			
		if i == 9:
			print ('mode', 9)
			time.sleep_ms(10) # On attend 100 ms
			
			if button.value() == 0:
                            # Si la valeur du bouton est de 0
				delta = time.ticks_diff(time.ticks_ms(), start) # On calcule une nouvelle différence de temps
				if delta > 1000:
                                    # Si la différence de temps est inférieure à 1000 ms
					print(delta)
					print ('appuis long', j)
					print ('mode pompe Feu on')
					relaisfeu.on() # On allume le relais feu
					oled.fill(0)
					oled.text("Pompe Feu", 0, 0) # On écrit à l'écran Pompe Feu on
					oled.text("on", 0, 20)
					oled.show()
					time.sleep_ms(500) # On attend 500 ms
					
		if i == 10:
			print ('mode', 10)
			time.sleep_ms(10) # On attend 10 ms
			
			if button.value() == 0:
                            # Si la valeur du bouton est de 0
				delta = time.ticks_diff(time.ticks_ms(), start) # On calcule une nouvelle différence de temps
				if delta > 1000:
                                    # Si la différence de temps est inférieure à 1000 ms
					print(delta)
					print ('appuis long', j)
					print ('mode pompe Feu off')
					relaisfeu.off() # On éteint le relais feu
					oled.fill(0)
					oled.text("Pompe Feu", 0, 0)
					oled.text("off", 0, 20) # On écrit à l'écran Pompe Feu off
					oled.show()
					time.sleep_ms(500) # On attend 500 ms
					
		if i == 11:
			oled.fill(0)
			oled.text("Pompe sol", 0, 15) # On écrit à l'écran Pompe sol
			oled.show()
			print ('mode', 11)
			time.sleep_ms(100) # On attend 100 ms
			
		if i == 12:
			print ('mode', 12)
			time.sleep_ms(10) # On attend 100 ms
			
			if button.value() == 0:
				delta = time.ticks_diff(time.ticks_ms(), start)
				if delta > 1000:
					print(delta)
					print ('appuis long', j)
					print ('mode pompe sol on')
					relaissol.on()
					oled.fill(0)
					oled.text("Pompe sol", 0, 0)
					oled.text("on", 0, 20) # On écrit à l'écran Pompe sol on
					oled.show()
					time.sleep_ms(500)
					
		if i == 13:
			print ('mode', 13)
			time.sleep_ms(10)
			
			if button.value() == 0:
				delta = time.ticks_diff(time.ticks_ms(), start)
				if delta > 1000:
					print(delta)
					print ('appuis long', j)
					print ('mode pompe sol off')
					relaissol.off()
					oled.fill(0)
					oled.text("Pompe sol", 0, 0)
					oled.text("off", 0, 20) # On écrit à l'écran Pompe sol off
					oled.show()
					time.sleep_ms(500)
			
		if i == 14:
			oled.fill(0)
			oled.show()
			i = 0 # On réinitialise i
			print ('mode', 14)
			time.sleep_ms(100)

	else:
            # Si la valeur du bouton n'est pas de 0
		led.on() # On allume la led
		start = time.ticks_ms() # On lance un timer
	sleep(.1)



