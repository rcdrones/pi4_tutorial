import sys
import pygame

from settings import Settings
from ship import Ship

import game_functions as gf

from pygame.sprite import Group

from alien import Alien

from game_stats import GameStats

from button import Button

from scoreboard import Scoreboard

def run_game():
	pygame.init()

	#建立一个Settings的对象
	ai_settings = Settings()

	#调用对象内的参数
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	play_button = Button(ai_settings, screen, "Play")	
	
	ship = Ship(ai_settings, screen)
	
	bullets = Group()
	aliens = Group()
	
	#产生地人群
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	stats = GameStats(ai_settings)
	
	sb = Scoreboard(ai_settings, screen, stats)
	
	#stats.high_score = 777
	#gf.save_high_score(ai_settings, stats)
	
	gf.read_high_score(ai_settings, stats)
	sb.prep_high_score()
	
	while True:
		#检测退出信号
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

		if stats.game_active:
			ship.update()

			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
		
run_game()
		
