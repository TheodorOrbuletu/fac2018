from threading import Thread, Lock
import random
import time

mutex = Lock()
produced = []

class threadProd(Thread):
	def run(self):
		while True:
			mutex.acquire()
			num = random.randint(1, 10)
			global produced
			produced.append(num)
			print "produces", num
			time.sleep(1)
			print produced
			mutex.release()

class threadCons(Thread):
	def run(self):
		while True:
			mutex.acquire()
			global produced
			if not  produced:
				mutex.wait()
				time.sleep(random.random())
			else:
				aux = produced.pop()
				print "removed", aux 
				time.sleep(0.5)
			mutex.release()

threadProd().start()
threadCons().start()
