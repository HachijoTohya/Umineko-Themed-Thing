import pygame
from assets import *
from config import *
import time
import random
pygame.init()

pygame.mixer.set_num_channels(16)
playing = True
hitcounter = 0


while playing:
    win.blit(bg, (0, 0))
    pygame.display.update()
    ding = spawnenemy()
    while win.get_rect(top=0).contains(ding) and playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            if event.type == pygame.KEYDOWN and keypress(event) == "escape":
                playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ding.colliderect(gunshot(event.pos)):
                    win.blit(bg, (0, 0))
                    hitcounter += 1
                    win.blit(scoreboard(hitcounter), (0, 0))
                    pygame.display.update()
                    ding = spawnenemy()
                    print("Hit!")
                else:
                    win.blit(bg, (0, 0))
                    win.blit(enemy, ding)
                    win.blit(scoreboard(hitcounter), (0, 0))
                    pygame.display.update()
