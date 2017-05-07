class GlobalVars():
	
	def __init__(self):
		self.potTemp = [0]*359		#Used in Web Graphs
		self.tubeTemp = [0]*359		#Used in Web Graphs
		self.setPT = 0			#Set Point in Celcius
		self.newSetPT = False		#a boolean to notify brew loop of a change in set point
		self.heating = False		#heating is a boolean if heating element is on
		self.boil = False		#boolean if boilin
		self.vRegSetPt = 0

	def getSetPT(self):
		return self.setPT

	def setSetPT(self, SetPT):
		self.setPT = SetPT

	def getPotTemp(self):
		return self.potTemp

	def addPotTemp(self, PotTemp):
		self.potTemp.insert(0, PotTemp)
		self.potTemp.pop()

	def getTubeTemp(self):
		return self.tubeTemp

	def addTubeTemp(self, TubeTemp):
		self.tubeTemp.insert(0, TubeTemp)
		self.tubeTemp.pop()

	#Only call from PIDBrewLoop!
	def getSetPTChanged(self):
		self.temp = self.newSetPT
		self.newSetPT = False
		return temp

	def setSetPTChanged(self, NewSetPT):
		self.heating = True
		self.newSetPT = NewSetPT

	def getHeating(self):
		return self.heating

	def setHeating(self, Heating):
		self.heating = Heating

	def getBoil(self):
		return self.boil

	def setBoil(self, Boiling):
		self.boil = Boiling

	def getVRegSetPt(self):
		return self.vRegSetPt

	def setVRegSetPt(self, VRegSetPt):
		self.vRegSetPt = VRegSetPt