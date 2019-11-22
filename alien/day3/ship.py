import pygame

class Ship():
    
    def __init__(self, ai_settings, screen):
        self.screen = screen
        
        self.ai_settings = ai_settings
        
        self.moving_right = False
        self.moving_left = False
        
        self.image = pygame.image.load("images/ship.bmp")
        #建立2个对象，一个是飞船的对象，一个是窗口对象
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #把飞船的位置，确定下来。（底部中间！）
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        self.centerx = float(self.rect.centerx)
        
    def blitme(self):
        # 把飞船画出来！
        self.screen.blit(self.image, self.rect)
    
    def update(self):
            
        #比较简单的方式    
        #if self.moving_right == True:
        #    self.rect.centerx += 1    
        #if self.moving_left == True:
        #    self.rect.centerx -= 1
    
        #加入速度因子的方式
        if self.moving_right == True:
            self.centerx += self.ai_settings.ship_movingspeed_factor
        if self.moving_left == True:
            self.centerx -= self.ai_settings.ship_movingspeed_factor
        
        self.rect.centerx = self.centerx

