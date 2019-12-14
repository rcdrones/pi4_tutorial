

class GameStats():
	
	def __init__(self, ai_settings):
		self.ai_settings = ai_settings
		#游戏开始，为非激活状态
		self.game_active = False
		self.reset_stats()
		self.high_score = 0
		
	def reset_stats(self):
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1
