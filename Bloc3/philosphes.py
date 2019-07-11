from threading import Thread
from threading import Lock
import time
from random import *

class Philosophe(Thread):
    def __init__(self,nom,fourchette_gauche,fourchette_droite):
        Thread.__init__(self)
        self.nom = nom
        self.fourchette_gauche = fourchette_gauche
        self.fourchette_droite = fourchette_droite

    def run(self):
        print(f'Arrivé de {self.nom}')
        time.sleep(randint(0, 5))
        while True:
            self.pense()
            time.sleep(randint(0, 5))
            self.fourchette_droite.acquire()
            self.fourchette_gauche.acquire()

            self.mange()
            time.sleep(randint(0, 5))
            self.fourchette_droite.release()
            self.fourchette_gauche.release()

    def pense(self):
        print(f'{self.nom} pense')

    def mange(self):
        print(f'{self.nom} mange')


"""Programme principal"""

lesPhilosophes = ["Aristote","Pascal","Descarte","Socrate","Volataire"]
fourchette = [Lock() for n in range(5)]

philosophes= []
for i in range(5):
    unPhilosophe = Philosophe(lesPhilosophes[i], fourchette[min(i,(i+1)%5)], fourchette[max(i,(i+1)%5)])
    unPhilosophe.start()