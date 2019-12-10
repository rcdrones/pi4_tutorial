import sys
import pygame


def run_game():
	pygame.init()
	screen = pygame.display.set_mode((800,600))
	pygame.display.set_caption("Alien Invasion")
	
	bg_color = (230,230,230)
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		
		screen.fill(bg_color)		
		pygame.display.flip()
		
run_game()
		
