from pygame import*
import pygame
from random import*

width = height = 500
init()

fenetre = display.set_mode((width,height))
pygame.mixer.music.load('songs\song11.wav')
pygame.mixer.music.play()

display.set_caption("son tests")
fenetre.blit(image.load("buttons\pause2.png"),(0,0))


run = True
while run:
    for events in event.get():
        if events.type == QUIT:
            quit()
    display.flip()
       
