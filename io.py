import RPi.GPIO as io
import time

class farol:
	def __init__(pine):
		self.pine = pine
		io.setup(self.pine, io.OUT)
	def On():
		io.output(self.pine, io.HIGH)
	def Off():
		io.output(self.pine, io.LOW)

def initBoard():
	io.setmode(io.BOARD)

	while True:
		io.output(11,io.HIGH)
		time.sleep(2)
		io.output(11,io.LOW)
		time.sleep(2)

	io.cleanup()
