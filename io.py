import RPi.GPIO as io
import time

class farol:
	def __init__(self, pine):
		self.pine = pine
		io.setup(self.pine, io.OUT)
	def On(self):
		io.output(self.pine, io.HIGH)
	def Off(self):
		io.output(self.pine, io.LOW)

def initBoard():
	print("Modulo de Hardware iniciado!\n")
	io.setmode(io.BOARD)
	led01 = farol(11)

	while True:
		led01.On()
		time.sleep(2)
		led01.Off()
		time.sleep(2)
	else:
		io.cleanup()
