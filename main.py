import threading as th
import time
import bt
import io

if __name__ == "__main__":
	receptor = th.Thread(target = bt.receptorBluetooth, args = ())
	receptor.start()
	#hardware = th.Thread(target = io.initBoard, args = ())
        #hardware.start()

