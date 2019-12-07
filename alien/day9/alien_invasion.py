import sys
import pygame

from settings import Settings
from ship import Ship

import game_functions as gf

from pygame.sprite import Group

from alien import Alien

from game_stats import GameStats

def run_game():
	pygame.init()

	#建立一个Settings的对象
	ai_settings = Settings()

	#调用对象内的参数
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#bg_color = (230,230,230)
	
	ship = Ship(ai_settings, screen)
	#alien = Alien(ai_settings, screen)
	
	bullets = Group()
	aliens = Group()
	
	#产生地人群
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	stats = GameStats(ai_settings)
	
	while True:	
		#检测退出信号
		gf.check_events(ai_settings, screen, ship, bullets)

		if stats.game_active:
			ship.update()

			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
		
		#print(len(bullets))
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)
		
run_game()
		
