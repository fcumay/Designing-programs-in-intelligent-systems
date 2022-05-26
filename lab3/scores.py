import pygame.font
from gun import Gun
from pygame.sprite import Group
import constants.settings as settings


class Scores():

    def __init__(self, screen, stats):
        self.name = ' '
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = settings.L_GREEN
        self.font = pygame.font.SysFont(None, settings.SCORE_SIZE)
        self.image_score()
        self.image_high_score()
        self.image_guns()

    def image_score(self):
        """Conver text from score to image"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, settings.BLACK)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_high_score(self):
        """Conver text from high score to image"""
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, settings.BLACK)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def image_guns(self):
        """Number of lives"""
        self.guns = Group()
        for gun_number in range(self.stats.guns_left):
            gun = Gun(self.screen)
            gun.rect.x = 15 + gun_number * gun.rect.width
            gun.rect.y = 20
            self.guns.add(gun)

    def show_score(self):
        """Draw score"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.guns.draw(self.screen)
