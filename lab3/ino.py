import pygame


class Ino(pygame.sprite.Sprite):
    '''One ino'''

    def __init__(self, screen):
        '''init and start position'''
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/ino.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        '''Output ino on the screen'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''move inos'''
        self.y += 0.1
        self.rect.y = self.y
