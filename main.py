import bluetooth
import RPi.GPIO
import thread as th
import time
import os

class bt:
	def __init__(self, port):
		self.server = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
		self.server.bind(("",port))
		self.server.listen(port)
	def connect(self):
		self.client, self.clientAddress = self.server.accept()
	def recvMsg(self):
		return self.client.recv(1024)
	def sendMsg(self,msg):
		self.client.send(msg)
	def close(self):
		self.client.close()
		self.server.close()

class led:
	def __init__(self, pine):
		RPi.GPIO.setmode(RPi.GPIO.BOARD)
		self.pine = pine
		RPi.GPIO.setup(self.pine, RPi.GPIO.OUT)
	def On(self):
		RPi.GPIO.output(self.pine, RPi.GPIO.HIGH)
	def Off(self):
		RPi.GPIO.output(self.pine, RPi.GPIO.LOW)

if __name__ == "__main__":

	def turnOnBt():
		os.system('hciconfig hci0 piscan')
		op = ''
		bth = bt(1)
		bth.connect()
		bth.sendMsg('Conectado!\n')
		while op != '0':
			op = bth.recvMsg()
			print(op)
		else:
			bth.sendMsg('Desconectando..\n'
			bth.close()
	turnOnBt()
