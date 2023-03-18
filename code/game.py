import pygame
import random

TITEL = 'Space Wars - 0.0.1'

clock = pygame.time.Clock()
FPS = 60
BLACK = 0, 0, 0
WHITE = 255, 255, 255
ROT = (255, 0, 0)

SPIELFELD_HOEHE = 700
SPIELFELD_BREITE = 1200

STERNE_DURCHMESSER = 5
STERNE_ANZAHL = 20
STERNE_FARBE = (255, 255, 255)

pygame.init()

SPIELFELD = pygame.display.set_mode((SPIELFELD_BREITE, SPIELFELD_HOEHE))
pygame.display.set_caption(TITEL)

RAUMSCHIFF_X_POS = 200
RAUMSCHIFF_Y_POS = 200
RAUMSCHIFF_GESCHWINDIGKEIT = 10
RAUMSCHIFF_BREITE = 20
RAUMSCHIFF_HOEHE = 20


class Sterne:
    def __init__(self):
        self.x = random.randint(0, SPIELFELD_BREITE)
        self.y = random.randint(0, SPIELFELD_HOEHE)


Sternenspeicher = [Sterne()] * STERNE_ANZAHL

for i in range(STERNE_ANZAHL):
    Sternenspeicher[i] = Sterne()

pygame.display.flip()

running = True
spaceship = pygame.image.load('../png/spaceship.png')
spaceship = pygame.transform.scale(spaceship, (30, 30))


def zeichneRaumschiff(x, y):
    SPIELFELD.blit(spaceship, (x, y))


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

    zeichneRaumschiff(RAUMSCHIFF_X_POS, RAUMSCHIFF_Y_POS)

    pygame.display.update()

    SPIELFELD.fill(BLACK)
    for i in Sternenspeicher:
        pygame.draw.rect(SPIELFELD, WHITE, (i.x, i.y, STERNE_DURCHMESSER, STERNE_DURCHMESSER))
