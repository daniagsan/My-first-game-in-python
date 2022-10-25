from cgi import test
from sys import exit
import pygame

pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('First Videogame')
clock = pygame.time.Clock()
test_font =  pygame.font.Font("Resources_fv/font/Pixeltype.ttf", 50)

sky_surface = pygame.image.load("Resources_fv\graphics\Sky.png").convert()
ground_surface = pygame.image.load("Resources_fv\graphics\ground.png").convert()
text_surface = test_font.render("This is a text", False, "Black")

snail_surface = pygame.image.load("Resources_fv\graphics\snail\snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (850,300))

player_surf = pygame.image.load("Resources_fv\graphics\Player\player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            print(mouse_pos)

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    #player_rect.right -= 1
    screen.blit(player_surf,player_rect)

    snail_rect.x -= 10
    if snail_rect.right < 0: 
        snail_rect.left = 800

    #if print(player_rect.colliderect(snail_rect)):
        #print('Colission')

    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        print("Mouse colliding with player rect")

    screen.blit(snail_surface,snail_rect)

    pygame.display.update()
    clock.tick(30)