from threading import Thread
from threading import Lock

class Compteur():
    def __init__(self,ver):
        self.compteur = 0
        self.leVerrou = ver

    def valeur(self):
        return self.compteur

    def inc(self):
        delai = 0
        borne = 5000
        self.leVerrou.acquire()
        try:
            v = self.compteur
            for i in range(borne):
                delai = delai + 1
            v = v+1
            self.compteur = v
        finally:
            self.leVerrou.release()

    def raz(self):
        self.compteur = 0

class Incrementeur(Thread):
    def __init__(self,n,c):
        Thread.__init__(self)
        self.objet = n
        self.counter = c

    def run(self):
        self.counter.inc()
        print(f'{self.objet} : {self.counter.valeur()}')

"""Programme principal"""
monVerrou = Lock()
moncompteur = Compteur(monVerrou)


for i in range(100):
    monthread1 = Incrementeur("monthread1",moncompteur)
    monthread2 = Incrementeur("monthread2",moncompteur)
    monthread1.start()
    monthread2.start()
    print(moncompteur.valeur())
    monthread1.join()
    monthread2.join()