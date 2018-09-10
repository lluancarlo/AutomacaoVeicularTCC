import bluetooth
import os

class btClass:
	def __init__(self, port):
		self.server = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
		self.server.bind(("",port))
		self.server.listen(1)
		self.client, self.clientAddress = self.server.accept()
	def accept(self):
		data = self.client.recv(1024)
		return data
	def closeClient(self):
		self.client.close()
	def closeServer(self):
		self.server.close()
	def getClientAdress():
		return self.clientAdress

if __name__ == "__main__":
	data = ''
	bt = btClass(1)

	while(data != '0'):
		data = bt.accept()
		print(data)
	else:
		bt.closeClient()
		bt.closeServer()

