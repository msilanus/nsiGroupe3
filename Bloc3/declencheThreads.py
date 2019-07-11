from threading import Thread
import time
from random import *


class Declencheur():
    def __init__(self):
        self.declencheur = False

    def active(self):
        self.declencheur = True

    def est_actif(self):
        return  self.declencheur



class MonThread(Thread):
    """La classe MonThread"""
    def __init__(self,d):
        Thread.__init__(self)
        self.declencheur = d
        print(f'Création de MonThread : déclencheur = {self.declencheur.est_actif()}')


    def run(self):
        time.sleep(0.01)
        print("le thread secondaire")
        self.declencheur.active()
        print(f'MonThread a activé le déclencheur : déclencheur = {self.declencheur.est_actif()}')

"""Programme principal"""
#Création d'un déclencheur

leDeclencheur = Declencheur()

#Création d’un thread
monthread = MonThread(leDeclencheur)

#lancement du thread
monthread.start()
print(f'Le thread principal est en attente : déclencheur = {leDeclencheur.est_actif()}')
while not leDeclencheur.est_actif():
    # attendre
    print(f'toujours pas...')

#time.sleep(randint(0,10))
print("le thread principal")
monthread.join()