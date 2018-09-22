import RPi.GPIO as gpio
import time

class farol:
	def __init__(self, pine):
		gpio.setmode(gpio.BOARD)
		self.pine = pine
		gpio.setup(self.pine, gpio.OUT)
	def On(self):
		gpio.output(self.pine, gpio.HIGH)
	def Off(self):
		gpio.output(self.pine, gpio.LOW)
