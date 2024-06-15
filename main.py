import pygame
from sys import exit 

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Dark Forest")
clock = pygame.time.Clock()

trees = pygame.image.load('graphics/environment/spooky_trees.png')
landscape = pygame.image.load('graphics/environment/mountain_landscape.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(trees,(200,100))
    screen.blit(landscape, (0,0))
    
    pygame.display.update()
    clock.tick(60)