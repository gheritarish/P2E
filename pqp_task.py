# Pot qui pense - CREPP 2019
# GPL V3.0
# www.crepp.org - yvoz.lg@gmail.com

# On importe les autres programmes du PQP
import machine, time
import pqp_relais as r
import pqp_horloge as h
import pqp_thermometre as t
import pqp_converan as c
import pqp_config as co
import sys

r.off() # On éteint le relais

def start():
	test() # On fait clignoter le relais
	#pump()
	time.sleep_ms(1000) # On fait une pause
	datalog() # On écrit dans les logs


def test():
    """On fait clignoter le relais par périodes de 250ms allumé / 250ms éteint, 3 fois"""
	for i in range(0,3):
		time.sleep_ms(250)
		r.on()
		time.sleep_ms(250)
		r.off()

def pump():
	# irrigation
	r.on()
	time.sleep_ms(co.pumptime)
	r.off()


def datalog():
    """Pour écrire dans les logs"""
	f = open("pqp_datalog.csv", "a")
	data = h.get_datehour() + "; "
	data += t.get_temp() + "; "
	data += str(machine.reset_cause()) + "; "
	data += str(c.get_battery()) + "; " + "\n"
	f.write(data)
	f.close()


