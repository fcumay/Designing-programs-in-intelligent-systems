import pygame


def run():
    """Screen with main information about game"""
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('Space Invaders')
    bg_color = (0, 0, 0)
    screen.fill(bg_color)

    f1 = pygame.font.SysFont('monospace', 42)
    f2 = pygame.font.SysFont('monospace', 36)
    text0 = f1.render('INFORMATION:', 1, (0, 255, 0))
    text1 = f2.render('Use your bullets to defend Earth from waves of SpaceInvaders!''', 1, (255, 255, 0))
    text2 = f1.render('TO MOVE:', 1, (0, 255, 0))
    text3 = f2.render('press [A] == [<-] AND press [D] == [->]', 1, (255, 255, 0))
    text4 = f2.render('press [ __ ] to shoot', 1, (255, 0, 0))

    screen.blit(text0, (50, 50))
    screen.blit(text1, (100, 150))
    screen.blit(text2, (50, 300))
    screen.blit(text3, (100, 400))
    screen.blit(text4, (100, 450))

    pygame.display.flip()
