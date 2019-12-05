import sys
import time
import threading
from playsound import playsound

class MyTimer:

	global notify_after_every

	def __init__(self):
		self.notify_after_every = 15*60

	def startTimer(self, waitUntilMins):
		waitUntilSecs = waitUntilMins * 60
		timer = threading.Timer(waitUntilSecs, self.playSound)
		timer.start()
		print(f'Timer scheduled for {waitUntilMins} minutes')
		self.printMessage(waitUntilSecs)

	def playSound(self):
		playsound('sample.mp3')
		print('Timer finished.')	

	def printMessage(self, waitTime):
		timeElapsed = waitTime
		while timeElapsed > self.notify_after_every:
			time.sleep(self.notify_after_every)
			timeElapsed = timeElapsed - self.notify_after_every
			print(f'{(waitTime - timeElapsed)/60} minutes over')

myTimer = MyTimer()
myTimer.startTimer(int(sys.argv[1]))