from threading import Thread

class Compteur():
    def __init__(self):
        self.compteur = 0

    def valeur(self):
        return self.compteur

    def inc(self):
        delai = 0
        borne = 50000
        v = self.compteur
        for i in range(borne):
            delai = delai + 1
        v = v+1
        self.compteur = v

    def raz(self):
        self.compteur = 0

class Incrementeur(Thread):
    def __init__(self,c):
        Thread.__init__(self)
        self.counter = c

    def run(self):self.counter.inc()

"""Programme principal"""
moncompteur = Compteur()

for i in range(100):
    monthread1 = Incrementeur(moncompteur)
    monthread2 = Incrementeur(moncompteur)
    monthread1.start()
    monthread2.start()
    print(moncompteur.valeur())
    monthread1.join()
    monthread2.join()