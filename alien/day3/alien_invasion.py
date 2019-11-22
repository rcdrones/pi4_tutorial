import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	pygame.init()
	
	#建立一个Settings的对象
	ai_settings = Settings()
	
	
	#调用对象内的参数
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#bg_color = (230,230,230)
	
	ship = Ship(ai_settings, screen)
	
	
	while True:
		
		#检测退出信号
		gf.check_events(ship)
		
		#for event in pygame.event.get():
		#	if event.type == pygame.QUIT:
		#		sys.exit()
				
		#画背景、友机、show出来
		gf.update_screen(ai_settings, screen, ship)
		#screen.fill(ai_settings.bg_color)	
		
		ship.update()
		#ship.blitme()
			
		#pygame.display.flip()
		
run_game()
		
