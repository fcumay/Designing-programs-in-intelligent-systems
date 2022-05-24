import pygame
import json


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun, index):
        """Create bullet using gun position"""
        super(Bullet, self).__init__()
        self.screen = screen
        with open("gun_options.json", "r") as jf:
            self.option = json.load(jf)
        self.rect = pygame.Rect(0, 0, self.option["size"][index], 12)
        self.color = self.option["color"][index][0], self.option["color"][index][1], self.option["color"][index][2]
        self.speed = self.option["speed"][index]
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """Shoot"""
        self.y -= self.option["speed"][0]
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
