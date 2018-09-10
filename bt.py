import bluetooth

server_socket = bluetooth.BluetoothSocket( bluetooth.RFCOMM )

server_socket.bind(("",1))
server_socket.listen(1)

client_socket, address = server_socket.accept()
print ("Conectado ao dispositivo ",address)

while 1:
	data = client_socket.recv(1024)
	print("Mensagem: ",data)

	if data == '0':
		client_socket.send(" Turn Off! ")
	elif data == '1':
		client_socket.send(" Turn On! ")
	elif data == '2':
		client_socket.send(" It's a Number Two boy. ")

client_socket.close()
server_socket.close()
