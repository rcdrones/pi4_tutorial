import sys
import pygame

from settings import Settings
from ship import Ship

def run_game():
	pygame.init()
	
	#建立一个Settings的对象
	ai_settings = Settings()
	
	
	#调用对象内的参数
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#bg_color = (230,230,230)
	
	ship = Ship(screen)
	
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		
		#先画背景，然后画前景
		#ship.blitme()
		#screen.fill(bg_color)
		screen.fill(ai_settings.bg_color)	
		
		ship.blitme()
			
		pygame.display.flip()
		
run_game()
		
