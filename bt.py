\import bluetooth

class bt:
	def __init__(self,port):
		self.server = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
		self.server.bind(("",port))
		self.server.listen(port)
		self.client, self.clientAddress = self.server.accept()
	def msg(self):
		return self.client.recv(1024)
	def off(self):
		self.client.close()
		self.server.close()

def receptorBluetooth():
	data = ""
	b = bt(1)
	while data != '0':
		data = b.msg()
	else:
		b.off()
