import time
import machine
import onewire, ds18x20

def test():
	# the device is on GPIO1
	dat = machine.Pin(1)
	# create the onewire object
	ds = ds18x20.DS18X20(onewire.OneWire(dat))
	# scan for devices on the bus
	roms = ds.scan()
	print('capteurs détectés:', roms) # write the devices detected
	ds.convert_temp()
	for rom in roms:
            # On va chercher à connaître la température de chacun des appareils détectés
		DS = ds.read_temp(rom)
		print('température:',DS)
	print()
