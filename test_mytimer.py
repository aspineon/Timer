import unittest
from mytimer import MyTimer

class TestMyTimer(unittest.TestCase):

	global myTimer

	@classmethod
	def setUp(self):
		self.myTimer = MyTimer()

	@unittest.skip	
	def test_givenTimeInMinutes__thenTriggerSoundAfterTimeLapse(self):
		wait_until = 1
		self.myTimer.startTimer(wait_until)	
		

	def test_waitTimePrintMessage(self):
		self.myTimer.printMessage(60)	

if __name__ == '__main__':
	unittest.main()
