import os
import glob
import time
import RPi.GPIO as GPIO

#The DS18B20 in the pot thermowell must be attached to GPIO pin XX
potThermoSN = '28-0000075599aa'
tubeThermoSN = '28-000007555514'

class HardwareUtility:

	def __init__(self):
		os.system('modprobe w1-gpio')
		os.system('modprobe w1-therm')

		base_dir = '/sys/bus/w1/devices/'

		pot_device_folder = base_dir + potThermoSN
		tube_device_folder = base_dir + tubeThermoSN

		self.pot_device_file = pot_device_folder + '/w1_slave'
		self.tube_device_file = tube_device_folder + '/w1_slave'
		
		self.inc_pin = 37 #GPIO PIN YOU ATTACHED TO THE INCREMENT BUTTON
		self.dec_pin = 35 #GPIO PIN YOU ATTACHED TO THE DECREMENT BUTTON

		GPIO.setmode(GPIO.BOARD)


###DS18B20 Thermometer#############################################
#Before execution, do the following hardware and software steps
#	Hardware:
#		Attach a 4.7K-10K pull up resistor on the sensor.
#	Software:
#		Add the following lines to /boot/config.txt
#			dtoverlay=w1-gpio
#		Execute the following commands in a terminal
#			sudo modprobe w1-gpio
#			sudo modprobe w1-therm
#			cd /sys/bus/w1/devices
#			ls
#			cd 28-xxxx (change x's to serial number)
#			cat w1_slave

	def read_pot_temp_raw(self):
                try:
		        f = open(self.pot_device_file,'r')
                except:
                        print("Cant read pot temp")
                        return 0

		lines = f.readlines()
		f.close()
		return lines
	
	def read_pot_temp(self):
		lines = self.read_pot_temp_raw()

                # error checking
                if lines == 0:
                        return 0

		while lines[0].strip()[-3] != 'Y':
			time.sleep(0.2)
			lines = self.read_temp_raw()
		equals_pos = lines[1].find('t=')
		if equals_pos != -1:
			temp_string = lines[1][equals_pos+2:]
			temp_c = float(temp_string) / 1000.0
		return float(temp_c)

	def read_tube_temp_raw(self):
                try:
		        f = open(self.tube_device_file,'r')
                except:
                        print("Cant read tube temp")
                        return 0

		lines = f.readlines()
		f.close()
		return lines

	def read_tube_temp(self):
		lines = self.read_tube_temp_raw()

                # error checking
                if lines == 0:
                        return 0

		while lines[0].strip()[-3] != 'Y':
			time.sleep(0.2)
			lines = self.read_temp_raw()
		equals_pos = lines[1].find('t=')
		if equals_pos != -1:
			temp_string = lines[1][equals_pos+2:]
			temp_c = float(temp_string) / 1000.0
		return float(temp_c)


###RioRand Voltage Regulator#######################################
#Before execution do the following hardware and software steps
#	Hardware: Attach the desired pins to the voltage reg
#	Software: Run the following commands in a terminal
#		sudo apt-get install python-dev
#		sudo apt-get install pthon-rpi.gpio

	def inc_temp(self):
		GPIO.setup(self.inc_pin, GPIO.OUT)
		GPIO.output(self.inc_pin, False)
		time.sleep(.1)
		GPIO.output(self.inc_pin, True)
		time.sleep(.1)
		return
	
	
	def dec_temp(self):
		GPIO.setup(self.dec_pin, GPIO.OUT)
		GPIO.output(self.dec_pin, False)
		time.sleep(0.1)
		GPIO.output(self.dec_pin, True)
		time.sleep(0.1)
		return
