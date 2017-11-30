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
        self.TempHistory = [0]*3599         #Used in Web Graphs
        self.TemperatureSetPt = 0           #Set Point in Celcius
        self.RestartPID = True              #Use when changing Set Point
        self.CurVRegSetPt = 0               #What the Voltage Regulator is actually set to (0-100)
        self.NewVRegSetPt = 0               #What the Voltage Regulator should be set to
        self.MaxVRegSetPt = 65              #Highest alowable setpoint for voltage regulator
        self.PidControl = PID(40, 0.2, 1)   #P:100 I:0.2 D:0 for quick heat
        self.PidControl.setPoint(0)

        self.CollectTemp()
        self.ComputeVoltageRegulatorSetpt()

    def CollectTemp(self):
        # Repeat every second
        threading.Timer(1, self.CollectTemp).start()

        # Read temperature sensors
        self.lock.acquire()
        self.TempHistory.insert(0, self.Hardware.read_temp())
        self.TempHistory.pop()
        self.lock.release()

    def ComputeVoltageRegulatorSetpt(self):
        # Repeat every second
        threading.Timer(1, self.ComputeVoltageRegulatorSetpt).start()

        self.lock.acquire()

        # Temperature set point is 0 Celcius (or below). Turn off heating element
        if self.TemperatureSetPt == 0:
            self.NewVRegSetPt = 0

        #Boil Mode (No PID). Manually set voltage regualtor
        elif self.TemperatureSetPt == 100:
            if self.TempHistory[0] < 95 :
                self.NewVRegSetPt = self.MaxVRegSetPt
            else:
                self.NewVRegSetPt = 35

        #Set Point Mode (PID Algorithm)
        else:
            #if the setpoint has changed, restart PID
            if self.RestartPID:
                self.PidControl.setPoint(self.TemperatureSetPt)
            self.NewVRegSetPt = self.PidControl.update(self.TempHistory[0])
            self.NewVRegSetPt = int(self.NewVRegSetPt)

        self.lock.release()


    def run(self):

        # Actualize the voltage regulator setpoint every 1 second.
        # Do not use a timer because this may take longer than
        # 1 second to run.
        while(True):
            self.lock.acquire()
            unlockedNewVRegSetPt = self.NewVRegSetPt
            unlockedCurVRegSetPt = self.CurVRegSetPt
            self.lock.release()
    
            #Set the voltage regulator with the calculated value
            print("NewVRegSetPt: " + str(unlockedNewVRegSetPt))
            while unlockedCurVRegSetPt > unlockedNewVRegSetPt and unlockedCurVRegSetPt > 0 and unlockedCurVRegSetPt < self.MaxVRegSetPt+1:
                self.Hardware.dec_temp()
                unlockedCurVRegSetPt -= 1
            while unlockedCurVRegSetPt < unlockedNewVRegSetPt and unlockedCurVRegSetPt > -1 and unlockedCurVRegSetPt < self.MaxVRegSetPt:
                self.Hardware.inc_temp()
                unlockedCurVRegSetPt +=1
            print("VReg: " + str(unlockedCurVRegSetPt))
    
            self.lock.acquire()
            self.NewVRegSetPt = unlockedNewVRegSetPt
            self.CurVRegSetPt = unlockedCurVRegSetPt 
            self.lock.release()
            time.sleep(1)


    def SetTemperatureSetPt(self, temp):
        self.lock.acquire()
        self.TemperatureSetPt = temp
        self.RestartPID = True
        self.lock.release()
