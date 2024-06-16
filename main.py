import pygame
from sys import exit 

pygame.init()

screen = pygame.display.set_mode((800, 550))
pygame.display.set_caption("Dark Forest")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Boxy-Bold.ttf', 50)

character = pygame.image.load('graphics/player/char_test/main_char.png').convert_alpha()
character_rectangle = character.get_rect(center = (400, 250))

grass = pygame.image.load('graphics/environment/map_without_trees.png').convert_alpha()
game_title_text = test_font.render('Dark Forest', False, 'White', 'Black')
night_background = pygame.Surface((800, 550))
night_background.set_alpha(225)


while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        pressed = pygame.key.get_pressed()
        if (pressed[pygame.K_UP] or pressed[pygame.K_w]) and character_rectangle.top >= 0:
            character_rectangle.top -= 2
        if (pressed[pygame.K_DOWN] or pressed[pygame.K_s]) and character_rectangle.bottom <= 550:
            character_rectangle.bottom += 2 
        if (pressed[pygame.K_LEFT] or pressed[pygame.K_a]) and character_rectangle.left >= 0:
            character_rectangle.left -= 2 
        if (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]) and character_rectangle.right <= 800:
            character_rectangle.right += 2
            
  
    screen.blit(grass, (0,0))
    screen.blit(character, character_rectangle)
    screen.blit(night_background, (0,0))
    screen.blit(game_title_text, (200, 30))
    
    pygame.display.update()
    