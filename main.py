import pygame
from sys import exit 

pygame.init()

screen = pygame.display.set_mode((800, 550))
pygame.display.set_caption("Dark Forest")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font\Boxy-Bold.ttf', 50)

character = pygame.image.load('graphics/player/char_test/character.png')
character_x_pos = 400
character_y_pos = 250

grass = pygame.image.load('graphics/environment/map_grass.png')
game_title_text = test_font.render('Dark Forest', False, 'White', 'Black')
night_background = pygame.Surface((800, 550))
night_background.set_alpha(210)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] or pressed[pygame.K_w]:
            character_y_pos -= 2
        if pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
            character_y_pos += 2 
        if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
            character_x_pos -= 2 
        if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
            character_x_pos += 2

  
    screen.blit(grass, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    
    screen.blit(night_background, (0,0))
    screen.blit(game_title_text
, (200, 30))
    
    pygame.display.update()
    clock.tick(60)