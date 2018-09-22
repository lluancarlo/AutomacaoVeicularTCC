import bluetooth

class bt:
	def __init__(self,port):
		self.server = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
		self.server.bind(("",port))
		self.server.listen(port)
		#self.client, self.clientAddress = self.server.accept()
	def msg(self):
		self.client, self.clientAddress = self.server.accept()
		return self.client.recv(1024)
	def off(self):
		self.client.close()
		self.server.close()

def receptorBluetooth():
	print("Modulo receptor Bluetooth iniciado!\n")

	'''
	server = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
	server.bind(("",1))
	server.listen(1)
	client, clientAdr = server.accept()

	data = ''
	while data != '0':
		data = client.recv(1024)
	else:
		client.close()
		server.close()
	'''
	bth = bt(1)

	data = ''
	while data != '0':
		data = bth.msg();
	else:
		bth.off()

receptorBluetooth()
