import pygame
from config import *
import random
pygame.init()

icon = pygame.image.load("images/2.ico")
pygame.display.set_icon(icon)
pygame.display.set_caption("Umineko Themed Thing")
win = pygame.display.set_mode(size=(1600, 900))
bg = pygame.image.load("images/kanshan.jpg").convert()
shot = pygame.mixer.Sound("sounds/Gunshot.wav")
buleff = pygame.image.load("images/shot.png").convert()
enemy = pygame.image.load("images/furudo.png").convert()
idiotnoise = pygame.mixer.Sound("sounds/Ahaha.wav")
counter = pygame.font.SysFont(name="franklingothicmedium", size=42)



def gunshot(bulxy):
    bulx = bulxy[0]-40
    buly =bulxy[1]-40
    buleff.set_colorkey(0)
    shot.set_volume(volume)
    hitbox = pygame.Rect((bulx, buly), (80, 80))
    pygame.mixer.Channel(0).play(shot)
    win.blit(buleff, (bulx, buly))
    pygame.display.update(hitbox)
    pygame.draw.rect(win, 0, hitbox)
    pygame.time.delay(25)
    pygame.event.clear(pygame.MOUSEBUTTONDOWN)
    return hitbox

def spawnenemy():
    spawnloc = (random.randrange(0, 1521), (random.randrange(0, 821)))
    idiotnoise.set_volume(volume)
    hitbox = pygame.Rect(spawnloc, (80, 80))
    idiotnoise.play()
    win.blit(enemy, spawnloc)
    pygame.display.update()
    pygame.draw.rect(win, 0, hitbox)
    return hitbox


def scoreboard(hitcounter):
    return counter.render(str(hitcounter), True, (255, 0, 0))






















def keypress(keyname):
    return pygame.key.name(keyname.key)
