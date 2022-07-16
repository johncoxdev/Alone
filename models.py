import random
import pygame
import math

class default_creature(pygame.sprite.Sprite):
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
        self.STARTING_X, self.STARTING_Y = self.posx, self.posy
        
    def crawl_out(self):
        if (self.is_crawl_animation == True):
            self.current_sprite += random.random() * 0.15
            if (int(self.current_sprite) >= len(self.sprites_crawl)):
                self.current_sprite = len(self.sprites_crawl)-1
                self.current_sprite = 0
                self.is_crawl_animation = False
                self.is_walk_animation = True
                return self.is_walk_animation
        self.image = self.sprites_crawl[int(self.current_sprite)]
        return self.is_walk_animation
    
    """
    NOTE: How we're going to be making the sprites move to a set x,y point in the map
    - 'x' is going to be using cos(radians)
    - 'y' is going to be using sin(radians)
    - 'distance (d)' to find how much longer until we have reached where we need to go
    """
    def walking(self, speed = 1.0):
        """
        Walking animation towards a continous x/y line
        
        Parameters
        ----------
        `speed : float, default 1.0`
            set the speed of the default_creature movement.
        """
        WIDTH, HEIGHT = 1000, 750
        self.SPEED = speed
        self.previous_x, self.previous_y = self.STARTING_X, self.STARTING_Y
        self.distance_x, self.distance_y = 0, 0
        self.distance = 0
        
        self.GET_DESPAWNPOINT_X , self.GET_DESPAWNPOINT_Y = WIDTH/2.1, HEIGHT/2
        
        self.radians = math.atan2(self.GET_DESPAWNPOINT_Y - self.previous_y, self.GET_DESPAWNPOINT_X - self.previous_x)
        self.distance = math.hypot(self.GET_DESPAWNPOINT_X - self.previous_x, self.GET_DESPAWNPOINT_Y - self.previous_y) / self.SPEED
        self.distance = int(self.distance)    
        
        self.distance_x = math.cos(self.radians)*self.SPEED
        self.distance_y = math.sin(self.radians)*self.SPEED
        
        self.previous_x, self.previous_y = self.GET_DESPAWNPOINT_X, self.GET_DESPAWNPOINT_Y
        if (self.distance != 0):
            self.distance -= 1
            self.STARTING_X += self.distance_x
            self.STARTING_Y += self.distance_y
        
        if(self.is_walk_animation == True):
            self.current_sprite += random.random() * 0.35
            if (int(self.current_sprite) >= len(self.sprites_walk)):
                self.current_sprite = 0
            self.image = self.sprites_walk[int(self.current_sprite)]        
            
    def draw(self, win):
        if (self.rect.topleft[0] > 500):
            flipped_image = pygame.transform.flip(self.image, True, False)
            return win.blit(flipped_image, (self.STARTING_X, self.STARTING_Y))
        win.blit(self.image, (self.STARTING_X, self.STARTING_Y))
    
    
    def __load_images(self):
        """
        load sprite images (crawl/walking) to the class.
        """
        self.sprites_crawl = []
        self.sprites_crawl.append(pygame.image.load('.\Images\default_creature\crawl0.png'))
        self.sprites_crawl.append(pygame.image.load('.\Images\default_creature\crawl1.png'))
        self.sprites_crawl.append(pygame.image.load('.\Images\default_creature\crawl2.png'))
        self.sprites_crawl.append(pygame.image.load('.\Images\default_creature\crawl3.png'))
        self.sprites_crawl.append(pygame.image.load('.\Images\default_creature\crawl4.png'))
        self.sprites_crawl.append(pygame.image.load('.\Images\default_creature\crawl5.png'))
        self.sprites_walk = []
        self.sprites_walk.append(pygame.image.load('.\Images\default_creature\walk0.png'))
        self.sprites_walk.append(pygame.image.load('.\Images\default_creature\walk1.png'))
        self.sprites_walk.append(pygame.image.load('.\Images\default_creature\walk2.png'))
        self.sprites_walk.append(pygame.image.load('.\Images\default_creature\walk3.png'))
    