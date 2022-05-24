import pygame, controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores


def run(name):
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('Space Invaders')
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats(name)
    sc = Scores(screen, stats)
    music = pygame.mixer.Sound('audio/music.wav')
    music.set_volume(0.2)
    music.play(loops=-1)

    while True:
        controls.events(screen, gun, bullets,stats)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, sc, gun, inos, bullets)
            controls.update_bullets(screen, stats, sc, inos, bullets)
            controls.update_inos(stats, screen, sc, gun, inos, bullets)
