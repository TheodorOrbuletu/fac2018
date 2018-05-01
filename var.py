from threading import Thread, Lock, Condition
import random
import time

cond = Condition()
produced = []
maxSize = 5
size = 0

class threadCons(Thread):
	def run(self):
		while True:
			global produced
			global size
		
			cond.acquire()

			while len(produced) == 0:
				cond.wait()

			i = produced[0]
			aux = produced.remove(i)
			size = size - 1
			cond.release()
			print "removed", i 
			time.sleep(0.8)

class threadProd(Thread):
	def run(self):
		while True:
			#num = random.randint(1, 10)
			global produced
			global size

			if size < maxSize:
				num = random.randint(1, 10)
				cond.acquire()
				produced.append(num)
				size = size + 1
				cond.notify()
				cond.release()
				print "produces", num
				print produced
				time.sleep(0.6)

threadProd().start()
threadCons().start()
