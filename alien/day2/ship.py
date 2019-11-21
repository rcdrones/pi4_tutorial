import pygame

class Ship():
    
    def __init__(self,screen):
        self.screen = screen
        
        self.image = pygame.image.load("images/ship.bmp")
        #建立2个对象，一个是飞船的对象，一个是窗口对象
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #把飞船的位置，确定下来。（底部中间！）
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    def blitme(self):
        # 把飞船画出来！
        self.screen.blit(self.image, self.rect)
        
    

