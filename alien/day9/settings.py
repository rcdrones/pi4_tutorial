
class Settings():
    
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)
        
        #友机左右移动的速度因子（step）
        self.ship_movingspeed_factor = 2  
        self.ship_limit = 3
        
        #子弹设置
        self.bullet_speed_factor = 5
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        
        #外星人设置
        self.alien_speed_factor = 5
        self.alien_drop_speed = 50
        #设置左右移动的参数。 1 = 右移动   -1 = 向左移动
        self.fleet_direction = 1
        
        
        
        
