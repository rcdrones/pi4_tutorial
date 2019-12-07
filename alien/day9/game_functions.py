import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	if event.key == pygame.K_LEFT:
		ship.moving_left = True 
	
	#按下键盘产生子弹的object
	if event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
	
	if event.key == pygame.K_q:
		sys.exit()

		
def fire_bullet(ai_settings, screen, ship, bullets):
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)


def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		#按下就连续移动
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
			
			
			
def update_screen(ai_settings, screen, ship, aliens, bullets):
	screen.fill(ai_settings.bg_color)
	
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	#bullets.draw(screen)
	
	ship.blitme()
	#alien.blitme()
	
	#for alien in aliens.sprites():
		#alien.blitme()
	aliens.draw(screen)
	
	pygame.display.flip()
	
def update_bullets(ai_settings, screen, ship, aliens, bullets):
	bullets.update()
		
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
			
	check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)
	
	
def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
	#判断2个Groups是否有交集，返回一个字典
	# 最后2个 bool参数表示是否要destory obj
	## Groups1, Groups2, destory for G1 , destory for G2		
	collisions = pygame.sprite.groupcollide(aliens, bullets, True, False)
	
	if len(aliens) == 0:
		bullets.empty()
		create_fleet(ai_settings, screen, ship, aliens)

	
		
def get_number_aliens_x(ai_settings, alien_width):
	#x轴预留后的长度
	available_space_x = ai_settings.screen_width - (2* alien_width)
	
	#计算能存放多少个alien
	number_aliens_x = int( available_space_x/(2*alien_width))
	
	return number_aliens_x

def get_number_aliens_y(ai_settings, ship_height, alien_height):
	#计算y轴的空闲高度
	available_space_y = ai_settings.screen_height - ship_height - 3*alien_height;
	
	#计算能放几行
	number_rows = int( available_space_y / (2* alien_height))
	return number_rows
	
		
#创建单个敌人
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	
	alien.x = alien_width + 2* alien_width * alien_number

	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2*alien.rect.height* row_number
	
	#alien.index = str(alien_number) + str(row_number)
	
	#print("%s " %(alien.index), end = "*")
	aliens.add(alien)
	
def create_fleet(ai_settings, screen, ship, aliens):
	alien = Alien(ai_settings, screen)
	
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_aliens_y(ai_settings, ship.rect.height, alien.rect.height)
	
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number, row_number)
		
def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
	aliens.update() #更新x轴坐标
	check_fleet_edges(ai_settings, aliens)
	
	#检查aliens和ship触碰
	if pygame.sprite.spritecollideany(ship,aliens):
		#print("Ship hit!!!")
		ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
	
	#检查aliens和屏幕底变的触碰
	check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

#最终减命的函数
def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
	if stats.ships_left > 1:
		stats.ships_left -= 1
		
		aliens.empty()
		bullets.empty()
		
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()
		
		sleep(0.5)
	else:
		stats.game_active = False

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
	screen_rect = screen.get_rect()
	
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
			break	

def check_fleet_edges(ai_settings, aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break

#如果碰到了边缘，更新方向，并且Y轴向下移动			
def change_fleet_direction(ai_settings, aliens):
	ai_settings.fleet_direction *= -1
	#Y轴向下移动
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.alien_drop_speed
		

