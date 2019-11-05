import pygame
from config import *
import random
pygame.init()

trans = (0, 0, 0)
icon = pygame.image.load("images/2.ico")
pygame.display.set_icon(icon)
pygame.display.set_caption("Umineko Themed Thing")
win = pygame.display.set_mode(size=(1600, 900))
bg = pygame.image.load("images/kanshan.jpg").convert()
shot = pygame.mixer.Sound("sounds/Gunshot.wav")
enemy = pygame.image.load("images/furudo.png").convert()
buleff = pygame.image.load("images/shot.png").convert()
idiotnoise = pygame.mixer.Sound("sounds/Ahaha.wav")


def gunshot(bulxy):
    shot.set_volume(volume)
    pygame.mixer.Channel(0).play(shot)
    win.blit(buleff, (bulxy[0]-40, bulxy[1]-40))
    pygame.display.update()
    pygame.time.delay(25)
    pygame.event.clear(pygame.MOUSEBUTTONDOWN)


def spawnenemy():
    idiotnoise.set_volume(volume)
    spawnloc = (random.randrange(0, 1521), random.randrange(0, 821))
    win.blit(enemy, spawnloc)
    pygame.display.update()
    idiotnoise.play()



















def keypress(keyname):
    return pygame.key.name(keyname.key)
