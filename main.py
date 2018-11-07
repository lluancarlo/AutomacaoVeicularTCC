import bluetooth
import RPi.GPIO
import time
import os
from multiprocessing import Process

class driver:
	def __init__(self, nome, dtanasc, cnh, cnhtip, dtavenc, totalkm, mediakm, mediatemp):
		self.nome = nome
		self.dtanasc = dtanasc
		self.cnh = cnh
		self.cnhtip = cnhtip
		self.dtavenc = dtavenc
		self.totalkm = totalkm
		self.mediakm = mediakm
		self.mediatemp = mediatemp
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
	status = 0
	def __init__(self, pine):
		self.pine = pine
		RPi.GPIO.setup(self.pine, RPi.GPIO.OUT)
	def On(self):
		RPi.GPIO.output(self.pine, RPi.GPIO.HIGH)
		self.status = 1
	def Off(self):
		RPi.GPIO.output(self.pine, RPi.GPIO.LOW)
		self.status = 0
class rgb:
	statusR = 0
	statusG = 0
	statusB = 0
	def __init__(self, pineR, pineG, pineB):
		self.pineR = pineR
		self.pineG = pineG
		self.pineB = pineB
		RPi.GPIO.setup(self.pineR, RPi.GPIO.OUT)
		RPi.GPIO.setup(self.pineG, RPi.GPIO.OUT)
		RPi.GPIO.setup(self.pineB, RPi.GPIO.OUT)
	def Red(self):
		if not self.statusR:
			RPi.GPIO.output(self.pineR, RPi.GPIO.HIGH)
			self.statusR = 1
		else:
			RPi.GPIO.output(self.pineR, RPi.GPIO.LOW)
			self.statusR = 0
	def Green(self):
                if not self.statusG:
                        RPi.GPIO.output(self.pineG, RPi.GPIO.HIGH)
			self.statusG = 1
                else:
                        RPi.GPIO.output(self.pineG, RPi.GPIO.LOW)
			self.statusG = 0
	def Blue(self):
                if not self.statusB:
                        RPi.GPIO.output(self.pineB, RPi.GPIO.HIGH)
			self.statusB = 1
                else:
                        RPi.GPIO.output(self.pineB, RPi.GPIO.LOW)
			self.statusB = 0

class motor:
        status = 0
        def __init__(self, pine):
                self.pine = pine
                RPi.GPIO.setup(self.pine, RPi.GPIO.OUT)
        def On(self):
                RPi.GPIO.output(self.pine, RPi.GPIO.HIGH)
                self.status = 1
        def Off(self):
                RPi.GPIO.output(self.pine, RPi.GPIO.LOW)
                self.status = 0

class buzzer:
	status = 0
	def __init__(self, pine):
		self.pine = pine
		RPi.GPIO.setup(self.pine, RPi.GPIO.OUT)

	def playStarWars(self):
		self.buzz = RPi.GPIO.PWM(self.pine, 1)
		self.buzz.start(1)

		timeNt = [500,500,500,350,150,500,350,150,1000,500,500,500,350,150,500,350,150,1000,500,350,150,500,250,250,125,125,
			  350,  1,250,500,250,250,125,125,250,  1,125,500,375,125,500,375,125,1000,500,250,150,500,250,250,125,125,
			  250,  1,250,500,250,250,125,125,250,  1,250,500,375,125,500,375,125,1000]
		melody = [440,440,440,349,523,440,349,523, 440,659,659,659,698,523,415,349,523, 440,880,440,440,880,830,784,740,698,
			  740,250,455,622,587,554,523,466,523,250,349,415,349,440,523,440,523, 659,880,440,440,880,830,784,740,698,
			  740,250,455,622,587,554,523,466,523,250,349,415,349,523,440,349,261,440]

		for x in range(0,len(melody),1):
			self.buzz.ChangeFrequency(melody[x])
			time.sleep(float(timeNt[x]/1000.000))
		self.buzz.stop()

	def playMario(self):
		self.buzz = RPi.GPIO.PWM(self.pine, 1)
		self.buzz.start(1)

		timeNt = [120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120,
                          120, 120, 120, 120,  90,  90,  90, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120,
                          120, 120, 120, 120, 120, 120, 120,  90,  90,  90, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120]
		melody = [2637, 2637, 250, 2637, 250, 2093, 2637, 250, 3136, 250,  250, 250, 1568, 250, 250, 250, 2093, 250, 250, 1568, 250, 250, 1319, 250, 250,
			  1760, 250, 1976, 250, 1865, 1760, 250, 1568, 2637, 3136, 3520, 250, 2794, 3136, 250, 2637, 250, 2093, 2349, 1976, 250, 250, 2093, 250,
			  250, 1568, 250, 250, 1319, 250, 250, 1760, 250, 1976, 250, 1865,  1760, 250, 1568, 2637, 3136, 3520, 250, 2794, 3136, 250, 2637, 250,
			  2093, 2349, 1976, 250, 250]

		for x in range(0,len(melody),1):
			self.buzz.ChangeFrequency(melody[x])
			time.sleep(float(timeNt[x]/1000.000))
		self.buzz.stop()

	def playPirates(self):
		self.buzz = RPi.GPIO.PWM(self.pine, 1)
		self.buzz.start(1)

		timeNt = [125, 125, 250, 125, 125, 125, 125, 250, 125, 125, 125, 125, 250, 125, 125, 125, 125, 375, 125, 125, 125,
			  250, 125, 125, 125, 125, 250, 125, 125, 125, 125, 250, 125, 125, 125, 125, 375, 125, 125, 125, 250, 125,
			  125, 125, 125, 250, 125, 125, 125, 125, 250, 125, 125, 125, 125, 125, 250, 125, 125, 125, 250, 125, 125,
			  250, 125, 250, 125, 125, 125, 250, 125, 125, 125, 125, 375, 375, 250, 125, 125, 125, 250, 125, 125, 125,
			  125, 250, 125, 125, 125, 125, 375, 125, 125, 125, 250, 125, 125, 125, 125, 250, 125, 125, 125, 125, 250,
			  125, 125, 125, 125, 375, 125, 125, 125, 250, 125, 125, 125, 125, 250, 125, 125, 125, 125, 250, 125, 125,
			  125, 125, 125, 250, 125, 125, 125, 250, 125, 125, 250, 125, 250, 125, 125, 125, 250, 125, 125, 125, 125,
			  375, 375, 250, 125, 375, 250, 125, 375, 125, 125, 125, 125, 125, 125, 125, 125, 375, 250, 125, 375, 250,
			  125, 375, 125, 125, 125, 125, 125, 500, 250, 125, 375, 250, 125, 375, 125, 125, 125, 125, 125, 125, 125,
			  125, 375, 250, 125, 375, 250, 125, 375, 125, 125, 125, 125, 125, 500]
		melody = [330, 392, 440, 440, 250, 440, 494, 523, 523, 250, 523, 587, 494, 494, 250, 440, 392, 440, 250, 330, 392, 440, 440,
                          250, 440, 494, 523, 523, 250, 523, 587, 494, 494, 250, 440, 392, 440, 250, 330, 392, 440, 440, 250, 440, 523, 587,
                          587, 250, 587, 659, 698, 698, 250, 659, 587, 659, 440, 250, 440, 494, 523, 523, 250, 587, 659, 440, 250, 440, 523,
                          494, 494, 250, 523, 440, 494, 250, 440, 440, 440, 494, 523, 523, 250, 523, 587, 494, 494, 250, 440, 392, 440, 250,
                          330, 392, 440, 440, 250, 440, 494, 523, 523, 250, 523, 587, 494, 494, 250, 440, 392, 440, 250, 330, 392, 440, 440,
                          250, 440, 523, 587, 587, 250, 587, 659, 698, 698, 250, 659, 587, 659, 440, 250, 440, 494, 523, 523, 250, 587, 659,
                          440, 250, 440, 523, 494, 494, 250, 523, 440, 494, 250, 659, 250, 250, 698, 250, 250, 659, 659, 250, 784, 250, 659,
			  587, 250, 250, 587, 250, 250, 523, 250, 250, 494, 523, 250, 494, 250, 440, 659, 250, 250, 698, 250, 250, 659, 659,
			  250, 784, 250, 659, 587, 250, 250, 587, 250, 250, 523, 250, 250, 494, 523, 250, 494, 250, 440]

		for x in range(0,len(melody),1):
			self.buzz.ChangeFrequency(melody[x])
			time.sleep(float(timeNt[x]/1000.000))
		self.buzz.stop()

	def playWarning(self):
                self.buzz = RPi.GPIO.PWM(self.pine, 1)
                self.buzz.start(1)

                timeNt = [2000]
                melody = [600]

                for x in range(0,len(melody),1):
		        self.buzz.ChangeFrequency(melody[x])
                        time.sleep(float(timeNt[x]/1000.000))
                self.buzz.stop()

def mod_bt():
	print('[SISTEMA] Modulo Bluetooth Iniciado!')

	#Def Driver
        motoristaA = driver('Luan Carlo', '23/09/1997', '12345678910', 'A', '16/10/2020', '13.876,27','9,6 Km/L', '39M')
        motoristaB = driver('Thiago Almeida', '05/07/19??', '12345678910', 'A, B', '02/03/2021', '6.285,03','8,2 Km/L', '1H 13M')
        motoristaC = driver('Jose Camacho', '01/02/19??', '12345678910', 'A, D', '19/06/2023', '8.189,62','10,2 Km/L', '1H 35M')

        #imports
        farol = led(40)
        bozina = buzzer(36)
        ledrgb = rgb(15,13,11)


	os.system('hciconfig hci0 piscan')
	op = ''
	bth = bt(1)
	bth.connect()


	bth.sendMsg('\n[COMANDO] -> ')

	#Process
	while op != 'z':
		op = bth.recvMsg()
		if (op=='1'):
			if (farol.status == 0):
				farol.On()
			else:
				farol.Off()
		elif (op=='3'):
			if (bozina.status ==0):
				bozina.playStarWars()
			else:
				bozina.Off()
		elif (op=='4'):
			if (bozina.status ==0):
				bozina.playPirates()
			else:
				bozina.off()
		elif(op=='5'):
			if (bozina.status ==0):
				bozina.playMario()
			else:
				bozina.off()
		elif(op=='r'):
			ledrgb.Red()
		elif(op=='g'):
			ledrgb.Green()
		elif(op=='b'):
			ledrgb.Blue()
		elif(op=='m'):
			bth.sendMsg('\n\n[MOTORISTA A] \n[NOME] -> {}\n[NASC] -> {}\n[CNH] -> {}\n[TIPO] -> {}\n[VENC] ->{}\n[TOTAL KM] -> {}\n[MEDIA KM] -> {}\n[MEDIA TEMPO] -> {}'.format(motoristaA.nome, motoristaA.dtanasc, motoristaA.cnh, motoristaA.cnhtip, motoristaA.dtavenc, motoristaA.totalkm, motoristaA.mediakm, motoristaA.mediatemp))
			bth.sendMsg('\n\n[COMANDO] ->  ')
		elif(op=='n'):
			bth.sendMsg('\n\n[MOTORISTA B] \n[NOME] -> {}\n[NASC] -> {}\n[CNH] -> {}\n[TIPO] -> {}\n[VENC] ->{}\n[TOTAL KM] -> {}\n[MEDIA KM] -> {}\n[MEDIA TEMPO] -> {}'.format(motoristaB.nome, motoristaB.dtanasc, motoristaB.cnh, motoristaB.cnhtip, motoristaB.dtavenc, motoristaB.totalkm, motoristaB.mediakm, motoristaB.mediatemp))
			bth.sendMsg('\n\n[COMANDO] ->  ')
		elif(op=='o'):
			bth.sendMsg('\n\n[MOTORISTA C] \n[NOME] -> {}\n[NASC] -> {}\n[CNH] -> {}\n[TIPO] -> {}\n[VENC] ->{}\n[TOTAL KM] -> {}\n[MEDIA KM] -> {}\n[MEDIA TEMPO] -> {}'.format(motoristaC.nome, motoristaC.dtanasc, motoristaC.cnh, motoristaC.cnhtip, motoristaC.dtavenc, motoristaC.totalkm, motoristaC.mediakm, motoristaC.mediatem))
			bth.sendMsg('\n\n[COMANDO] ->  ')
	else:
		l.Off()
		bth.sendMsg('\n\n[DESLIGANDO SISTEMA...]')
		bth.close()
		RPi.GPIO.cleanup()
		os.system('shutdown')

def mod_loop():
	print('[SISTEMA] Modulo Loop Iniciado!')

	RPi.GPIO.setup(18, RPi.GPIO.IN)
	RPi.GPIO.setup(16, RPi.GPIO.OUT)

	bozina = buzzer(36)
	led = rgb(15,13,11)

	while True:
		RPi.GPIO.output(16, False)
		time.sleep(0.5)
		RPi.GPIO.output(16, True)
        	time.sleep(0.00001)
	        RPi.GPIO.output(16, False)
	        tempoInicio = time.time();

        	while RPi.GPIO.input(18)==0:
	                tempoInicio = time.time()
        	while RPi.GPIO.input(18)==1:
                	tempoFinal = time.time()

	        var = tempoFinal-tempoInicio
	        somVolta = var * 17000
	        somvolta = round(somVolta, 2)

		if (somVolta < 20):
			led.Red()
			bozina.playWarning()
			led.Red()

if __name__ == "__main__":
	#Set Global Board Mode
        RPi.GPIO.setmode(RPi.GPIO.BOARD)
        RPi.GPIO.setwarnings(False)
        l = led(12)
        l.On()

        p1 = Process(target=mod_bt, args=())
	p2 = Process(target=mod_loop, args=())

        p1.start()
	p2.start()

	p1.join()
	p2.join()
