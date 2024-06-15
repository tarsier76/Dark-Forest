import pygame
from sys import exit 

pygame.init()

screen = pygame.display.set_mode((800, 550))
pygame.display.set_caption("Dark Forest")
clock = pygame.time.Clock()

character = pygame.image.load('graphics/player/char_test/character.png')
grass = pygame.image.load('graphics/environment/map_grass.png')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
  
    screen.blit(grass, (0,0))
    screen.blit(character, (0,0))
    
    pygame.display.update()
    clock.tick(60)