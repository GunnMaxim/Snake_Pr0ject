import every as every
import pygame
from random import randrange

from pygame import surface

##main code##

RES = 800
size = 50

x,y = randrange(size, RES - size, RES), randrange(size, RES - size, RES)
apple = randrange(size, RES - size, RES), randrange(size, RES - size, RES)
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 30


##controler##
dirs = {'W':True,'S': True,'A': True,'D': True }

score = 0
speed_count, snake_speed = 0, 10

pygame.init()
Surface = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Times New Roman', 26, bold=True)
font_end = pygame.font.SysFont('Times New Roman', 38, bold=True)
img = pygame.image.load('BackGround.png').convert()


#death#
def close_game():
    for event in pygame.event.get():
        if every.type == pygame.QUIT:
            exit()

##game itself##
while True:
    [pygame.draw.rect(surface,pygame.Color('pink'),(i,j, size - 1, size - 1)) for i, j in snake]
    pygame.draw.rect(surface, pygame.Color('green'),(*apple, size, size))


    ##points
    render_score = font_score.render(f'score:{score}',1,pygame.color('orange'))
    surface.blit(render_score, (5, 5))

    ##finally movement
    speed_count += 1
    if not speed_count % snake_speed:
        x += dx * size
        y += dy * size
        snake.append((x, y))
        snake = snake[-length]

    #food 6:27#