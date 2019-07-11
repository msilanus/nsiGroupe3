from threading import Thread
import time
from random import *

class MonThread(Thread):
    """La classe MonThread"""
    def run(self):
        time.sleep(randint(0,10))
        print("le thread secondaire")

"""Programme principal"""
#Création d’un thread
monthread = MonThread()

#lancement du thread
monthread.start()

time.sleep(randint(0,10))
print("le thread principal")
monthread.join()