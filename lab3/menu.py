import pygame
import sys
import Space_game
import info
import input
import high_score


def run():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('Space Invaders')
    bg_color = (0, 0, 0)
    screen.fill(bg_color)
    image = pygame.image.load('images/logo.png')
    logo_rect = image.get_rect()
    screen.blit(image, logo_rect)

    f1 = pygame.font.SysFont('monospace', 42)
    text0 = f1.render('PRESS:', 1, (255, 255, 0))
    text1 = f1.render('(1)->START', 1, (255, 0, 0))
    text2 = f1.render('(2)->HIGH', 1, (255, 255, 0))
    text3 = f1.render('(3)->INFO', 1, (255, 255, 0))
    text4 = f1.render('(Q)->QUIT', 1, (255, 0, 0))

    screen.blit(text0, (900, 300))
    screen.blit(text1, (990, 380))
    screen.blit(text2, (990, 430))
    screen.blit(text3, (990, 480))
    screen.blit(text4, (990, 530))

    pygame.display.flip()
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
