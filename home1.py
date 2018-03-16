from threading import Thread, Lock
import random
import time

mutex = Lock()
produced = []
maxSize = 2
size = 0

class threadProd(Thread):
	def run(self):
		while True:
			num = random.randint(1, 10)
			global produced
			global size
			if size != maxSize:
				mutex.acquire()
				produced.append(num)
				size =+ 1
				mutex.release()
				print "produces", num
				time.sleep(0.5)
			print produced

class threadCons(Thread):
	def run(self):
		while True:
			global produced
			global size
			if not  produced:
				size =- 1
				pass
				time.sleep(random.random())
			else:
				mutex.acquire()
				aux = produced.pop()
				mutex.release()
				print "removed", aux 
				time.sleep(1)

threadProd().start()
threadCons().start()