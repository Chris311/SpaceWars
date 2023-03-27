import random
import constants


class Sterne:
    def __init__(self):
        self.x = random.randint(0, constants.SPIELFELD_BREITE)
        self.y = random.randint(0, constants.SPIELFELD_HOEHE)


sternenspeicher = []
for i in range(constants.STERNE_ANZAHL):
    sternenspeicher.append(Sterne())
