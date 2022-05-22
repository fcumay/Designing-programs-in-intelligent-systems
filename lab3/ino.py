import pygame


class Ino(pygame.sprite.Sprite):
    '''One ino'''

    def __init__(self, screen):
        '''init and start position'''
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/ino.png')
        self.image2= pygame.image.load('images/ino2.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.move=0



    def update(self):
        '''move inos'''

        if self.move==0:
            self.image=pygame.image.load('images/ino.png')
            self.move=1

        else:
            self.image = pygame.image.load('images/ino2.png')
            self.move=0


        self.y += 0.1
        self.rect.y = self.y




