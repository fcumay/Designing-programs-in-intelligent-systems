import pygame
import constants.settings as settings


class Ino(pygame.sprite.Sprite):
    """First type of ino"""

    def __init__(self, screen):
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(settings.INO1)
        self.image2 = pygame.image.load(settings.INO1_2)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.move = 0

    def update(self):
        """Ino move"""
        if self.move == 0:
            self.image = pygame.image.load(settings.INO1)
            self.move = 1
        else:
            self.image = pygame.image.load(settings.INO1_2)
            self.move = 0
        self.y += settings.SPEED_INO1
        self.rect.y = self.y


class Ino2(Ino, pygame.sprite.Sprite):
    """Second type of ino"""

    def update(self):
        """Ino move"""
        if self.move == 0:
            self.image = pygame.image.load(settings.INO2)
            self.move = 1
        else:
            self.image = pygame.image.load(settings.INO2_2)
            self.move = 0
        self.y += settings.SPEED_INO2
        self.rect.y = self.y


class Ino3(Ino, pygame.sprite.Sprite):
    """Third type of ino"""

    def __init__(self, screen):
        '''init and start position'''
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(settings.INO3)
        self.rect = self.image.get_rect()
        self.move = 0

    def update(self):
        """Ino move"""
        if self.move == 0:
            self.image = pygame.image.load(settings.INO3)
            self.move = 1
        else:
            self.image = pygame.image.load(settings.INO3_2)
            self.move = 0
        self.y += settings.SPEED_INO3
        self.rect.y = self.y


class SuperIno(Ino, pygame.sprite.Sprite):
    """Type:Superino"""

    def update(self):
        """Ino move"""
        self.image = pygame.image.load(settings.SUPERINO)
        if self.x < 750:
            self.x += settings.SPEED_SINO
            self.rect.x = self.x
        else:
            self.image = pygame.image.load(settings.SUPERINO2)
