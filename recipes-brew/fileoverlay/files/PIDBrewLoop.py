import time
import threading
import logging
from HardwareUtility import HardwareUtility
from PID import PID

class PIDBrewLoop(threading.Thread):

    def __init__(self):
        super(PIDBrewLoop, self).__init__()
        self.daemon = True
        self.lock = threading.Lock()

        self.Hardware = HardwareUtility()
        self.TempHistory = [0]*359       #Used in Web Graphs
        self.TemperatureSetPt = 0           #Set Point in Celcius
        self.RestartPID = True              #Use when changing Set Point
        self.VRegSetPt = 0                  #Voltage Regulator Set Point (0-100, capped at 55)
        self.MaxVRegSetPt = 65              #Highest alowable setpoint for voltage regulator
        self.PidControl = PID(60, 0.2, 1)   #P:100 I:0.2 D:0 for quick heat
        self.PidControl.setPoint(0)


    def run(self):
        self.SetVRegTo = 0
        self.lock.acquire()

        while True:

            # Read temperature sensors
            self.TempHistory.insert(0, self.Hardware.read_temp())
            self.TempHistory.pop()

            # Temperature set point is 0 Celcius (or below). Turn off heating element
            if self.TemperatureSetPt == 0:
                self.SetVRegTo = 0

            #Boil Mode (No PID). Manually set voltage regualtor
            elif self.TemperatureSetPt == 100:
                if self.TempHistory[0] < 95 :
                    self.SetVRegTo = self.MaxVRegSetPt;
                else:
                    self.SetVRegTo = 35

            #Set Point Mode (PID Algorithm)
            else:
                #if the setpoint has changed, restart PID
                if self.RestartPID:
                    self.PidControl.setPoint(self.TemperatureSetPt)
                self.SetVRegTo = self.PidControl.update(self.TempHistory[0])
                self.SetVRegTo = int(self.SetVRegTo)

            #Set the voltage regulator with the calculated value
            print("SetVRegTo: " + str(self.SetVRegTo))
            while self.VRegSetPt > self.SetVRegTo and self.VRegSetPt > 0 and self.VRegSetPt < self.MaxVRegSetPt+1:
                self.Hardware.dec_temp()
                self.VRegSetPt -= 1
            while self.VRegSetPt < self.SetVRegTo and self.VRegSetPt > -1 and self.VRegSetPt < self.MaxVRegSetPt:
                self.Hardware.inc_temp()
                self.VRegSetPt +=1
            print("VReg: " + str(self.VRegSetPt))

            self.lock.release()
            
            # Always sleep for 10s between loop iterations
            time.sleep(10)
            
            self.lock.acquire()


    def SetTemperatureSetPt(self, temp):
      	self.lock.acquire()
        self.TemperatureSetPt = temp
        self.RestartPID = True
        self.lock.release()
