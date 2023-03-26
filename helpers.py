import pygame

def mouse_in_button(button, mouse_pos):
    if button.x_pos + button.width > mouse_pos[0] > button.x_pos and \
            button.y_pos < mouse_pos[1] < button.y_pos + button.height:
        return True

def load_img(path, width, height, x, y, screen):
    img = pygame.image.load(path)
    img = pygame.transform.scale(img, (width, height))
    screen.blit(img, (x, y))

