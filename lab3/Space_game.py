import pygame, controls
from gun import Gun


def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 780))
    pygame.display.set_caption('Space Invaders')
    bg_color = (0, 0, 0)
    gun = Gun(screen)

    while True:
        controls.events()
        screen.fill(bg_color)
        gun.output()
        pygame.display.flip()


run()
