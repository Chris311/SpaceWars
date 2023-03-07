import pygame
from random import *

TITEL = 'Space Wars - 0.0.1'

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


def zeichne_stern(x_pos_stern, y_pos_stern):
    for x in range(STERNE_DURCHMESSER):
        for y in range(STERNE_DURCHMESSER):
            SPIELFELD.set_at((x_pos_stern + x, y_pos_stern + y), STERNE_FARBE)


for i in range(STERNE_ANZAHL):
    zeichne_stern(randint(0, SPIELFELD_BREITE), randint(0, SPIELFELD_HOEHE))

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
