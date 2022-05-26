import pygame
from pygame.sprite import Sprite
import constants.settings as settings


class Gun(Sprite):

    def __init__(self, screen):
        """Initialize gun"""
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(settings.GUN)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        """Draw gun"""
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """Update gun position"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += settings.SPEED_GUN
        if self.mleft and self.rect.left > 0:
            self.center -= settings.SPEED_GUN
        self.rect.centerx = self.center

    def create_gun(self):
        """Create gun again"""
        self.center = self.screen_rect.centerx
