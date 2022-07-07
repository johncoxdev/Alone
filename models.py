import random
import pygame

class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.posx = x
        self.posy = y
        self.is_crawl_animation = True
        self.is_walk_animation = False
        self.sprites_crawl = []
        self.__load_images()
        self.current_sprite = 0
        self.image = self.sprites_crawl[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.posx,self.posy]
        self.walk_speed = 1
        
    def crawl_out(self):
        if (self.is_crawl_animation == True):
            self.current_sprite += random.random() * 0.15
            if (int(self.current_sprite) >= len(self.sprites_crawl)):
                self.current_sprite = len(self.sprites_crawl)-1
                self.current_sprite = 0
                self.is_crawl_animation = False
                self.is_walk_animation = True
        self.image = self.sprites_crawl[int(self.current_sprite)]
    
    
    """
    NOTE: We are going to find the angle and distance from the point
    of the zombie and moving it towards the middle of the screen. Once
    the zombie has went to the middle of the screen we will then destroy
    the class/sprite and have it remove -x health from the lives.
    """
    def walking(self):
        """
        Walking animation towards a continous x/y line
        
        Parameters
        ----------
        `speed : float, default 0.1`
            set the speed of the zombie movement.
        """
        if(self.is_walk_animation == True):
            self.current_sprite += random.random() * 0.35
            if (int(self.current_sprite) >= len(self.sprites_walk)):
                self.current_sprite = 0
            self.image = self.sprites_walk[int(self.current_sprite)]        
            
    def draw(self, win):
        if (self.rect.topleft[0] > 500):
            flipped_image = pygame.transform.flip(self.image, True, False)
            return win.blit(flipped_image, (self.posx, self.posy))
        win.blit(self.image, (self.posx, self.posy))
    
    
    def __load_images(self):
        """
        load sprite images (crawl/walking) to the class.
        """
        self.sprites_crawl = []
        self.sprites_crawl.append(pygame.image.load('.\Images\Zombie\crawl0.png'))
        self.sprites_crawl.append(pygame.image.load('.\Images\Zombie\crawl1.png'))
        self.sprites_crawl.append(pygame.image.load('.\Images\Zombie\crawl2.png'))
        self.sprites_crawl.append(pygame.image.load('.\Images\Zombie\crawl3.png'))
        self.sprites_crawl.append(pygame.image.load('.\Images\Zombie\crawl4.png'))
        self.sprites_crawl.append(pygame.image.load('.\Images\Zombie\crawl5.png'))
        self.sprites_walk = []
        self.sprites_walk.append(pygame.image.load('.\Images\Zombie\walk0.png'))
        self.sprites_walk.append(pygame.image.load('.\Images\Zombie\walk1.png'))
        self.sprites_walk.append(pygame.image.load('.\Images\Zombie\walk2.png'))
        self.sprites_walk.append(pygame.image.load('.\Images\Zombie\walk3.png'))
    