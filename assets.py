import pygame
from config import *
pygame.init()


icon = pygame.image.load("images/2.ico")
pygame.display.set_icon(icon)
pygame.display.set_caption("Umineko Themed Thing")
window = pygame.display.set_mode(size=(1600, 900))
bg = pygame.image.load("images/kanshan.jpg").convert()
shot = pygame.mixer.Sound("sounds/Gunshot.wav")



def gunshot():
    shot.set_volume(volume)
    shot.play()










def keypress(keyname):
    return pygame.key.name(keyname.key)
