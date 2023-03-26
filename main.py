import pygame
from Classes.tet import Tetris
from constans import *
from helpers import load_img, mouse_in_button


pygame.init()
screen = pygame.display.set_mode(SIZE_SCREEN)
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()
game = Tetris(20, 10)


pressing_down = False


def opening_screen():
    finish = False
    while not finish:
        screen.fill(BLACK)
        load_img(PLAY_PATH, PLAY_WIDTH, PLAY_HEIGHT, X_PLAY, Y_PLAY, screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if mouse_in_button(PLAY_BUTTON, pos):
                    game_screen()

        pygame.display.flip()


def game_screen():
    finish = False
    global pressing_down
    global COUNTER

    while not finish:
        if game.shape is None:
            game.new_figure()
        COUNTER += 1
        if COUNTER > LIMIT:
            COUNTER = 0

        if COUNTER % (FPS // game.level // 2) == 0 or pressing_down:
            if game.state == "start":
                game.go_down()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.rotate()
                if event.key == pygame.K_DOWN:
                    pressing_down = True
                if event.key == pygame.K_LEFT:
                    game.go_side(LEFT)
                if event.key == pygame.K_RIGHT:
                    game.go_side(RIGHT)
                if event.key == pygame.K_SPACE:
                    game.go_space()
                if event.key == pygame.K_ESCAPE:
                    game.__init__(20, 10)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    pressing_down = False

        screen.fill(BLACK)

        for i in range(game.height):
            for j in range(game.width):
                pygame.draw.rect(screen, WHITE, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
                if game.field[i][j] > 0:
                    pygame.draw.rect(screen, COLORS[game.field[i][j]],
                                     [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

        if game.shape is not None:
            for i in range(4):
                for j in range(4):
                    p = i * 4 + j
                    if p in game.shape.image():
                        pygame.draw.rect(screen, COLORS[game.shape.color],
                                         [game.x + game.zoom * (j + game.shape.x) + 1,
                                          game.y + game.zoom * (i + game.shape.y) + 1,
                                          game.zoom - 2, game.zoom - 2])

        font = pygame.font.SysFont(FONT_NAME, SIZE_SCORE, True, False)
        font1 = pygame.font.SysFont(FONT_NAME, SIZE_OVER_ESC, True, False)
        text = font.render("Score: " + str(game.score), True, WHITE)
        text_game_over = font1.render("Game Over", True, GAME_OVER_COLOR)
        text_game_over1 = font1.render("Press ESC", True, PRESS_ESC_COLOR)

        screen.blit(text, (0, 0))
        if game.state == "gameover":
            screen.blit(text_game_over, [20, 200])
            screen.blit(text_game_over1, [25, 265])

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


opening_screen()

