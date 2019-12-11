import pygame.font

class Scoreboard():
	
	def __init__(self, ai_settings, screen, stats):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats
		
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)
		
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		
	def prep_score(self):
		#score_str = str(self.stats.score)
		rounded_score = int(round(self.stats.score, -1))
		score_str = "{0:,}".format(rounded_score)
		#备注：.format()
		#6666   ->    6,666      100000000    -> 100,000,000   
		#"{0:,}"   0 表示后面的truple[0]   :表示转换    ，表示千分位隔离
		#.format(int) 表示要转换的内容。 
		#ref： https://blog.csdn.net/jpch89/article/details/84099277
		
		self.score_image = self.font.render(score_str, True, self.text_color,
											self.ai_settings.bg_color)
		
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20
	
	def prep_high_score(self):
		high_score = int(round(self.stats.high_score, -1))
		high_score_str = "{0:,}".format(high_score)
		
		self.high_score_image = self.font.render(high_score_str, True, 
									self.text_color,self.ai_settings.bg_color)
		
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top
		
	def show_score(self):
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		
	def prep_level(self):
		self.level_image = self.font.render(str(self.stats.level), True,
								self.text_color, self.ai_settings.bg_color)
								
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10
		
		
