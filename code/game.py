import pygame
import random
import constants

clock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption(constants.TITEL)

spielfeld = pygame.display.set_mode((constants.SPIELFELD_BREITE, constants.SPIELFELD_HOEHE))

raumschiff_x_pos = 200
raumschiff_y_pos = 200


class Sterne:
    def __init__(self):
        self.x = random.randint(0, constants.SPIELFELD_BREITE)
        self.y = random.randint(0, constants.SPIELFELD_HOEHE)


Sternenspeicher = [Sterne()] * constants.STERNE_ANZAHL

for i in range(constants.STERNE_ANZAHL):
    Sternenspeicher[i] = Sterne()

pygame.display.flip()

running = True
spaceship = pygame.image.load('../png/spaceship.png')
spaceship = pygame.transform.scale(spaceship, (30, 30))


def zeichne_raumschiff(x, y):
    spielfeld.blit(spaceship, (x, y))


while running:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and raumschiff_x_pos > 0:
        raumschiff_x_pos -= constants.RAUMSCHIFF_GESCHWINDIGKEIT

    if keys[pygame.K_d] and raumschiff_x_pos < constants.SPIELFELD_BREITE - constants.RAUMSCHIFF_BREITE:
        raumschiff_x_pos += constants.RAUMSCHIFF_GESCHWINDIGKEIT

    if keys[pygame.K_w] and raumschiff_y_pos > 0:
        raumschiff_y_pos -= constants.RAUMSCHIFF_GESCHWINDIGKEIT

    if keys[pygame.K_s] and raumschiff_y_pos < constants.SPIELFELD_HOEHE - constants.RAUMSCHIFF_HOEHE:
        raumschiff_y_pos += constants.RAUMSCHIFF_GESCHWINDIGKEIT

    zeichne_raumschiff(raumschiff_x_pos, raumschiff_y_pos)

    pygame.display.update()

    spielfeld.fill(constants.BLACK)
    for i in Sternenspeicher:
        pygame.draw.rect(spielfeld, constants.WHITE, (i.x, i.y, constants.STERNE_DURCHMESSER,
                                                      constants.STERNE_DURCHMESSER))
