import RPi.GPIO as io
import time

io.setmode(io.BOARD)

io.setup(11, io.OUT)

while True:
	io.output(11,io.HIGH)
	time.sleep(2)
	io.output(11,io.LOW)
	time.sleep(2)

io.cleanuo()
