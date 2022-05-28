import pygame
import constants.settings as settings


def run(stats):
    """Screen with main information about game"""
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('Space Invaders')
    bg_color = settings.BLACK
    screen.fill(bg_color)

    f1 = pygame.font.SysFont('monospace', settings.HEAD_SIZE)
    f2 = pygame.font.SysFont('monospace', settings.INFO_SIZE)
    text0 = f1.render('Great result!', 1, settings.GREEN)
    text1 = f2.render('NEW HIGHSCORE!!!''', 1, settings.YELLOW)

    screen.blit(text0, (50, 50))
    if stats.new_record:
        screen.blit(text1, (100, 150))

    pygame.display.flip()
