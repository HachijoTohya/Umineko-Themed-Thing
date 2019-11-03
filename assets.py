import pygame
from config import *
pygame.init()

red = (255, 0, 0)
icon = pygame.image.load("images/2.ico")
pygame.display.set_icon(icon)
pygame.display.set_caption("Umineko Themed Thing")
window = pygame.display.set_mode(size=(1600, 900))
bg = pygame.image.load("images/kanshan.jpg").convert()
shot = pygame.mixer.Sound("sounds/Gunshot.wav")

def gunshot(bulx, buly):
    bullet = pygame.Rect((bulx - 40), (buly - 40), 80, 80)
    pygame.draw.rect(window, red, bullet)
    shot.set_volume(volume)
    shot.play()











def keypress(keyname):
    return pygame.key.name(keyname.key)
