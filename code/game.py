import pygame, random


TITEL = 'Space Wars - 0.0.1'

clock = pygame.time.Clock()
FPS = 60
BLACK = 0, 0, 0
WHITE = 255, 255, 255

SPIELFELD_HOEHE = 700
SPIELFELD_BREITE = 1200

STERNE_DURCHMESSER = 5
STERNE_ANZAHL = 20
STERNE_FARBE = (255, 255, 255)


METEOR_DURCHMESSER = 30
METEOR_ANZAHL = 3
METEOR_FARBE = [230, 60, 100]
METEOR_GESCHWINDICHKEIT_Y = random.randint(0, 10)
METEOR_GESCHWINDICHKEIT_X = random.randint(-10, 10)


pygame.init()

SPIELFELD = pygame.display.set_mode((SPIELFELD_BREITE, SPIELFELD_HOEHE))
pygame.display.set_caption(TITEL)

RAUMSCHIFF_X_POS = 200
RAUMSCHIFF_Y_POS = 200
RAUMSCHIFF_GESCHWINDIGKEIT = 5
RAUMSCHIFF_BREITE = 40
RAUMSCHIFF_HOEHE = 40
tolerance = RAUMSCHIFF_HOEHE


class Sterne:
    def __init__(self):
        self.x = random.randint(0, SPIELFELD_BREITE)
        self.y = random.randint(0, SPIELFELD_HOEHE)
class Meteor:
    def __init__(self):
        self.x = 500
        self. y = 0

Meteorenspeicher = [Meteor()] * METEOR_ANZAHL
Sternenspeicher = [Sterne()] * STERNE_ANZAHL




for i in range(STERNE_ANZAHL):
    Sternenspeicher[i] = Sterne()

for i in range(METEOR_ANZAHL):
    Meteorenspeicher[i] = Meteor()

pygame.display.flip()


running = True

while running:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and RAUMSCHIFF_X_POS > 0:
        RAUMSCHIFF_X_POS -= RAUMSCHIFF_GESCHWINDIGKEIT

    if keys[pygame.K_d] and RAUMSCHIFF_X_POS < SPIELFELD_BREITE - RAUMSCHIFF_BREITE:
        RAUMSCHIFF_X_POS += RAUMSCHIFF_GESCHWINDIGKEIT

    if keys[pygame.K_w] and RAUMSCHIFF_Y_POS > 0:
        RAUMSCHIFF_Y_POS -= RAUMSCHIFF_GESCHWINDIGKEIT

    if keys[pygame.K_s] and RAUMSCHIFF_Y_POS < SPIELFELD_HOEHE - RAUMSCHIFF_HOEHE:
        RAUMSCHIFF_Y_POS += RAUMSCHIFF_GESCHWINDIGKEIT

    # drawing object on screen which is rectangle here
    pygame.draw.rect(SPIELFELD, (255, 0, 0), (RAUMSCHIFF_X_POS, RAUMSCHIFF_Y_POS, RAUMSCHIFF_BREITE, RAUMSCHIFF_HOEHE))

    pygame.display.update()

    SPIELFELD.fill(BLACK)
    for i in Sternenspeicher:
        pygame.draw.rect(SPIELFELD, WHITE, (i.x, i.y, STERNE_DURCHMESSER, STERNE_DURCHMESSER))

    for i in Meteorenspeicher:
        i.y += METEOR_GESCHWINDICHKEIT_Y
        i.x += METEOR_GESCHWINDICHKEIT_X
        pygame.draw.rect(SPIELFELD, 'brown', (i.x, i.y, METEOR_DURCHMESSER, METEOR_DURCHMESSER))
        if abs(RAUMSCHIFF_Y_POS - i.y) < tolerance and abs(RAUMSCHIFF_X_POS - i.x) < tolerance:
            exit()
