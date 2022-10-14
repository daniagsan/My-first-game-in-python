from cgi import test
import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('First Videogame')
clock = pygame.time.Clock()
test_font =  pygame.font.Font(None, 50)

sky_surface = pygame.image.load("Resources\graphics\Sky.png").convert()
ground_surface = pygame.image.load("Resources\graphics\ground.png").convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))

    pygame.display.update()
    clock.tick(30)