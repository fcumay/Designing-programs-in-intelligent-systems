import pygame
import Space_game
import stats


def run():
    """Screen, where user can input his name. User can also pass this step."""
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    font = pygame.font.Font(None, 32)
    input_box = pygame.Rect(100, 100, 140, 32)
    color = (0, 0, 255)
    text = 'NamePlayer'
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # save and continue
                if event.key == pygame.K_RETURN:
                    stats.name = text
                    Space_game.run(text)
                # del char
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                # add char
                else:
                    text += event.unicode
        screen.fill((0, 0, 0))
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()
