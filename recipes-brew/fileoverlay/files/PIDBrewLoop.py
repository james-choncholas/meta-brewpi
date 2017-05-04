import time
import threading
import logging
from HardwareUtility import HardwareUtility
from PID import PID

class PIDBrewLoop(threading.Thread):
#class PIDBrewLoop(object):

	def __init__(self, MyVars):
		super(PIDBrewLoop, self).__init__()
		self.daemon = True
		self.myVars = MyVars
		self.hardware = HardwareUtility()
		self.pidControl = PID(80, 0.2, 0)	#P:100 I:0.2 D:0 for quick heat
		self.pidControl.setPoint(self.myVars.getSetPT())
		self.VRegSetpt = 0
		self.PIDSetpt = 0


	def run(self):
		while True:

			self.myVars.addPotTemp(self.hardware.read_pot_temp())
			self.myVars.addTubeTemp(self.hardware.read_tube_temp())
			self.myVars.setVRegSetPt(self.VRegSetpt)
			time.sleep(10)

			while self.myVars.getHeating() == True:

				self.myVars.addPotTemp(self.hardware.read_pot_temp())
				self.myVars.addTubeTemp(self.hardware.read_tube_temp())
				self.myVars.setVRegSetPt(self.VRegSetpt)

				#Boil Mode (No PID)
				if self.myVars.getBoil():
					#Do this to get up to temp
					if self.myVars.getPotTemp()[0] < 95 :
						self.PIDSetpt = 65

					#At this point the user should cover the pot to maintain temp
					else:
						self.PIDSetpt = 35

				#Set Point Mode (PID Algorithm)
				else:
					#if the setpoint has changed restart PID
					if self.myVars.getSetPTChanged():
						self.pidControl.setPoint(self.myVars.getSetPT())
						self.myVars.setSetPTChanged(False)

					self.PIDSetpt = self.pidControl.update(self.myVars.getTubeTemp()[0])
					self.PIDSetpt = int(self.PIDSetpt)

					print("PIDSetpt: " +str(self.PIDSetpt))
				
				#Set the voltage regulator
				while self.VRegSetpt > self.PIDSetpt and self.VRegSetpt > 0 and self.VRegSetpt < 56:
					self.hardware.dec_temp()
					self.VRegSetpt -= 1
				while self.VRegSetpt < self.PIDSetpt and self.VRegSetpt > -1 and self.VRegSetpt < 55:
					self.hardware.inc_temp()
					self.VRegSetpt +=1

				self.myVars.setVRegSetPt(self.VRegSetpt)
				print("VReg: " + str(self.VRegSetpt))
				time.sleep(10)

			if self.myVars.getHeating() == False:
				for i in range(0, self.VRegSetpt):
					self.hardware.dec_temp()
					self.VRegSetpt -= 1
