from threading import Thread, Lock
import random
import time

mutex = Lock()
produced = []
maxSize = 5
size = 0

class threadProd(Thread):
	def run(self):
		while True:
			#num = random.randint(1, 10)
			global produced
			global size
			if size < maxSize:
				num = random.randint(1, 10)
				mutex.acquire()
				produced.append(num)
				size = size + 1
				mutex.release()
				print "produces", num
				print produced
				time.sleep(0.6)

class threadCons(Thread):
	def run(self):
		while True:
			global produced
			global size
			if not  produced:
				pass
				print "waiting for producer"
				time.sleep(0.5)
			else:
				i = produced[0]
				mutex.acquire()
				aux = produced.remove(i)
				size = size - 1
				mutex.release()
				print "removed", i 
				time.sleep(0.8)

threadProd().start()
threadCons().start()