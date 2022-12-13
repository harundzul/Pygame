import pygame
import os

WIDTH, HEIGHT = 900,500
WHITE = (255,255,255)
BLACK = (0,0,0)

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 30,30
FPS = 60
VEL = 5
BORDER = pygame.Rect(WIDTH/2 -5, 0, 10, HEIGHT)

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','yellow spaceship.png'))
BLUE_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','blue spaceship.png'))
GAME_ICON = pygame.image.load(os.path.join('Assets','ARRIW.png'))

YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),-90)
BLUE_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(BLUE_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),90)

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('GREST GAME')
pygame.display.set_icon(GAME_ICON)

def draw_window(yellow,blue):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x,yellow.y))
    WIN.blit(BLUE_SPACESHIP, (blue.x,blue.y))
    pygame.display.update()

def yellow_movement(key_pressed,yellow):
    if key_pressed[pygame.K_a] and yellow.x - VEL > 0: #LEFT
            yellow.x -= VEL
    if key_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: #RIGHT
            yellow.x += VEL
    if key_pressed[pygame.K_w] and yellow.y - VEL > 0: #UP
            yellow.y -= VEL
    if key_pressed[pygame.K_s] and yellow.y + VEL + yellow.width < HEIGHT: #DOWN
            yellow.y += VEL

def blue_movement(key_pressed,blue):
    if key_pressed[pygame.K_LEFT] and blue.x - VEL > BORDER.x + BORDER.width: #LEFT
            blue.x -= VEL
    if key_pressed[pygame.K_RIGHT] and blue.x + VEL +blue.width < WIDTH: #RIGHT
            blue.x += VEL
    if key_pressed[pygame.K_UP] and blue.y - VEL > 0: #UP
            blue.y -= VEL
    if key_pressed[pygame.K_DOWN] and blue.y + VEL + blue.height < HEIGHT: #DOWN
            blue.y += VEL

def main():
    yellow = pygame.Rect(200, 250, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    blue = pygame.Rect(700, 250, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        key_pressed = pygame.key.get_pressed()
        yellow_movement(key_pressed, yellow)
        blue_movement(key_pressed, blue)
        draw_window(yellow,blue)

    pygame.quit()

if __name__ == '__main__':
    main()