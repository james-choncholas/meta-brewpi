import httplib, urllib
from GlobalVars import GlobalVars
from threading import Thread

class TextAlert(Thread):

	def __init__(self, MyVars):
		Thread.__init__(self)
		self.myVars = MyVars

	def run(self):
		while not self.myVars.getQuit():
			if self.myVars.getCurTemp()[0] > (self.myVars.getSetPT() + 5):
				print("sending text")	
				sendText('The brew kettle has reached a temperature of ' + str(self.myVars.getCurTemp()[0]))
			sleep(10)
			self.myVars.setSetPT(10)


	def sendText(self,message):
		params = urllib.urlencode({'number': 6088866834, 'message': message})
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
		conn = httplib.HTTPConnection("textbelt.com:80")
		conn.request("POST", "/text", params, headers)
		response = conn.getresponse()
		return response.status, response.reason