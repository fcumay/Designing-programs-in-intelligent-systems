import pygame
import sys
import info
import input
import high_score
import constants.settings as settings


def run():
    """Main menu window"""
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('Space Invaders')
    bg_color = settings.BLACK
    screen.fill(bg_color)
    image = pygame.image.load(settings.LOGO)
    logo_rect = image.get_rect()
    sign = pygame.image.load(settings.SIGNATURE)
    screen.blit(image, logo_rect)
    screen.blit(sign, (175, 650))

    f1 = pygame.font.SysFont('monospace', 42)
    text0 = f1.render('PRESS:', 1, settings.YELLOW)
    text1 = f1.render('(1)->START', 1, settings.RED)
    text2 = f1.render('(2)->HIGH', 1, settings.YELLOW)
    text3 = f1.render('(3)->INFO', 1, settings.YELLOW)
    text4 = f1.render('(Q)->QUIT', 1, settings.RED)

    screen.blit(text0, settings.MENU_SIZE0)
    screen.blit(text1, settings.MENU_SIZE1)
    screen.blit(text2, settings.MENU_SIZE2)
    screen.blit(text3, settings.MENU_SIZE3)
    screen.blit(text4, settings.MENU_SIZE4)

    pygame.display.flip()

    # choose and change screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_1:
                    input.run()
                elif event.key == pygame.K_2:
                    high_score.run()
                elif event.key == pygame.K_3:
                    info.run()
