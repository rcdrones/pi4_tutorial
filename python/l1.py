import sys
import pygame


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.dispaly.set_caption("Alien Invasion 666")
    
    bg_color = ((110,230,230))
    
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    screen.fill(bg_color)
            
    pygame.display.flip()
    

run_game()
