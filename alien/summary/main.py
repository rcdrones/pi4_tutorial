#basic
import sys
import pygame
import pygame.font #文字

#集群管理
from pygame.sprite import Sprite
from pygame.sprite import Group


class OneImage(Sprite):
	
	def __init__(self, screen):
		super().__init__()
		self.screen = screen
		#这里的rect 和image 不能随便书写。因为调用Group().draw()会用到！
		self.image = pygame.image.load("images/alien.bmp")
		self.rect = self.image.get_rect()

mouse_x = 0
mouse_y = 0
	

def run_game():
	
	
	#print("hello")
	
	global mouse_x,mouse_y
	
	pygame.init()
	#屏幕设置（舞台设置）
	
	screen = pygame.display.set_mode((800,600))
	pygame.display.set_caption("666")
	
	screen_rect = screen.get_rect()
	
	while True:
	
		#消息处理
		for event in pygame.event.get():
			#print("get event!")
			if event.type == pygame.QUIT:#处理右上角的退出叉叉
				sys.exit()
			
			#处理q键
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
				sys.exit()
				
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x,mouse_y = pygame.mouse.get_pos()
			
		#背景颜色
		bg_color = (230,230,230)
		screen.fill(bg_color)
	
		#画文字
		str_temp = "1111"
		
		font = pygame.font.SysFont(None, 48)
		text_color = (30, 30, 30)
		
		text_image = font.render(str(str_temp), True, text_color, bg_color)
								
		text_image_rect = text_image.get_rect()
		text_image_rect.left = screen_rect.left + 10
		text_image_rect.top = screen_rect.top + 10
		
		screen.blit(text_image, text_image_rect)	
		
		
		#画图片（单个）
		
		one_image = pygame.image.load("images/ship.bmp")
		
		one_image_rect = one_image.get_rect()
		one_image_rect.centerx = screen_rect.centerx
		one_image_rect.bottom = screen_rect.top+100
		
		screen.blit(one_image, one_image_rect)

		
		#画图片（集群）
		Myimages = Group()
		
		for num in range(3):
			temp = OneImage(screen)
			temp.rect.y = 150
			temp.rect.x = 100 + num * temp.rect.width
			Myimages.add(temp)
		
		#print(len(Myimages))	
		Myimages.draw(screen)
		

		#画矩形
		rect1_color = (0xcd,0x1a,0xcd) #CD1ACD
		
		#rect1 = pygame.Rect(0,0,ai_settings.bullet_width, ai_settings.bullet_height)
		rect1 = pygame.Rect(0, 0, 50, 100)
		
		rect1.centerx = screen_rect.right-60
		rect1.bottom = screen_rect.top+300
		
		pygame.draw.rect(screen, rect1_color, rect1)
		
		
		#画按钮分2步骤
		
		b_width = 200
		b_height = 50
		b_color = (0, 0, 255)
		b_text_color = (255,255,255)
		b_font = pygame.font.SysFont(None, 48)
		
		b_rect = pygame.Rect(0, 0, b_width, b_height)
		b_rect.center = screen_rect.center
		
		#画矩形背景
		screen.fill(b_color, b_rect)
		
		button_clicked = b_rect.collidepoint(mouse_x, mouse_y)
	
		if button_clicked :	
			#print("111")		
			b_image = b_font.render("clicked", True, b_text_color, b_color)
		else:
			#print("222")
			b_image = b_font.render("Play", True, b_text_color, b_color)	
			
		b_image_rect = b_image.get_rect()
		b_image_rect.center = b_rect.center
		
		
		#画背景之上的图片
		screen.blit(b_image, b_image_rect)
		
	
		#显存刷新到GUI上
		pygame.display.flip()
	
	
run_game()	 

