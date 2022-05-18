import pygame
import sys

def events():
    '''Computing events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()