
class Settings():
    
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)
        
        self.score_file = "hs.txt"
        
        #友机左右移动的速度因子（step）
        #self.ship_movingspeed_factor = 2  
        self.ship_limit = 3
        
        #子弹设置
        #self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        
        #外星人设置
        #self.alien_speed_factor = 5
        self.alien_drop_speed = 10
        
        
        #难度增加的系数
        self.speedup_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        
        self.ship_movingspeed_factor = 3 #6
        self.bullet_speed_factor = 6 #12
        self.alien_speed_factor = 2 #4
        
        #设置左右移动的参数。 1 = 右移动   -1 = 向左移动
        self.fleet_direction = 1
        
        self.alien_points = 50
        self.score_scale = 1.5
        
    def increase_speed(self):
        self.ship_movingspeed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        #print(self.alien_points)
        
        
        
        
