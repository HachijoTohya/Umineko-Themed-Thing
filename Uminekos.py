import pygame
from assets import *
from config import *
import time
import random
pygame.init()



playing = True

while playing:
    win.blit(bg, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           playing = False
        if event.type == pygame.KEYDOWN and keypress(event) == "escape":
            playing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            gunshot(event.pos)
            print(event)
