import pygame
import sys
from bullet import Bullet
from ino import Ino
from ino import Ino2
from ino import Ino3
from ino import SuperIno
import time
import menu
from stats import Stats


def events(screen, gun, bullets):
    '''Computing events'''
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                menu.run()
            # right
            elif event.key == pygame.K_d:
                gun.mright = True
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                laser_sound = pygame.mixer.Sound('audio/laser.wav')
                laser_sound.set_volume(0.5)
                laser_sound.play()
                index=Stats.new_level-1
                new_bullet = Bullet(screen, gun,index)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            # right
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False


def update(bg_color, screen, stats, sc, gun, inos, bullets):
    '''update screen'''
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()


def update_bullets(screen, stats, sc, inos, bullets):
    '''update bullets position'''
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    if collisions:
        for inos in collisions.values():
            stats.score += 10 * len(inos)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_guns()
    if len(inos) == 0:
        if Stats.new_level<5:
            bullets.empty()
            create_army(screen, inos)
            Stats.new_level+=1
        else:
            stats.run_game = False
            menu.run()


def gun_kill(stats, screen, sc, gun, inos, bullets):
    '''Crash gun by army'''
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_guns()
        inos.empty()
        bullets.empty()
        create_army(screen, inos)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        menu.run()


def update_inos(stats, screen, sc, gun, inos, bullets):
    '''update inos position'''
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats, screen, sc, gun, inos, bullets)
    inos_check(stats, screen, sc, gun, inos, bullets)


def inos_check(stats, screen, sc, gun, inos, bullets):
    '''check end of screen'''
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, inos, bullets)
            break


def create_army(screen, inos):
    '''create army of inos'''
    ino = Ino(screen)
    ino_width = ino.rect.width+40
    number_ino_x = int((1550 - 2 * ino_width) / ino_width)
    ino_height = ino.rect.height+40
    number_ino_y=3

    for row_number in range(number_ino_y - 1):
        for ino_number in range(number_ino_x):
            ino = Ino2(screen)
            ino.x = ino_width + (ino_width * ino_number)
            ino.y = ino_height + (ino_height * row_number)
            ino.rect.x=ino.x
            ino.rect.y = ino.rect.height + ino.rect.height * row_number +ino_number*10
            inos.add(ino)

            ino = Ino(screen)
            ino.rect.x = ino_width + (ino_width * ino_number)
            ino.y = 300+ino_height + (ino_height * row_number)
            ino.rect.y = ino.rect.height + ino.rect.height * row_number +ino_number*10
            inos.add(ino)

    for row_number in range(number_ino_y - 2):
        for ino_number in range(number_ino_x):
            ino = Ino3(screen)
            ino.x = ino_width + (ino_width * ino_number)
            ino.y = 75+ino_height + (ino_height * row_number)
            ino.rect.x=ino.x
            ino.rect.y = ino.rect.height + ino.rect.height * row_number +ino_number*10
            inos.add(ino)

    ino=SuperIno(screen)
    ino.x = 50
    ino.y = 50
    ino.rect.x = ino.x
    ino.rect.y = ino.y
    inos.add(ino)






def check_high_score(stats, sc):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('high_score.txt', 'w') as f:
            f.write(str(stats.high_score) + '\n')
            f.write(str(stats.name))
