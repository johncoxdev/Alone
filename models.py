import random
import pygame
import math

class Bullet(pygame.sprite.Sprite):
    def __init__(self, mousex, mousey, speed, ARENA_WIDTH, ARENA_HEIGHT) -> None:
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.ARENA_WIDTH = ARENA_WIDTH
        self.ARENA_HEIGHT = ARENA_HEIGHT
        self.posx, self.posy = self.ARENA_WIDTH/2.1, self.ARENA_HEIGHT/2
        self.distance_x, self.distance_y = 0, 0 
        self.SPEED = speed
        self.in_bound = True
        self.MOUSE_X = mousex 
        self.MOUSE_Y = mousey
        self.previous_x = self.posx
        self.previous_y = self.posy
        self.radians = math.atan2(self.MOUSE_Y - self.previous_y, self.MOUSE_X - self.previous_x)
        self.rect = None
        self.ARENA_WIDTH = ARENA_WIDTH
        self.ARENA_HEIGHT = ARENA_HEIGHT
    
    def bullet_in_bound(self, posx, posy, WIDTH, HEIGHT):
        if ((posx <= 0 or posx >= WIDTH) or (posy <= 0 or posy >= HEIGHT)):
            return False
        return True
    
    def shoot(self, win):
        self.distance_x = math.cos(self.radians)*self.SPEED
        self.distance_y = math.sin(self.radians)*self.SPEED
        
        if (self.in_bound):
            self.posx += self.distance_x
            self.posy += self.distance_y
            self.rect = pygame.draw.circle(win, (179, 61, 55), [self.posx, self.posy], 4, 0)
            self.in_bound = self.bullet_in_bound(self.posx, self.posy, self.ARENA_WIDTH, self.ARENA_HEIGHT)
        
        if(not self.in_bound):
            self.kill()


class CreatureEntity(pygame.sprite.Sprite):
    def __init__(self, x, y, ARENA_WIDTH, ARENA_HEIGHT, creatureType, walking_speed, crawl_out_speed):
        super().__init__()
        self.posx = x
        self.posy = y
        self.is_crawl_animation = True
        self.is_walk_animation = False
        self.sprites_crawl = []
        self.__load_images(creatureType)
        self.current_sprite = 0
        self.image = self.sprites_crawl[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.posx,self.posy]
        self.walk_speed = 1
        self.distance = 0
        self.starting_x, self.starting_y = self.posx, self.posy
        self.SPEED = walking_speed
        self.CRAWL_OUT_SPEED = crawl_out_speed     
        self.ARENA_WIDTH = ARENA_WIDTH
        self.ARENA_HEIGHT = ARENA_HEIGHT
        
        
    def crawl_out(self):
        if (self.is_crawl_animation == True):
            self.current_sprite += random.random() * self.CRAWL_OUT_SPEED
            if (int(self.current_sprite) >= len(self.sprites_crawl)):
                self.current_sprite = len(self.sprites_crawl)-1
                self.current_sprite = 0
                self.is_crawl_animation = False
                self.is_walk_animation = True
                return self.is_walk_animation
        self.image = self.sprites_crawl[int(self.current_sprite)]
        return self.is_walk_animation
    
    def walking(self):
        
        self.previous_x, self.previous_y = self.starting_x, self.starting_y
        self.distance_x, self.distance_y = 0, 0
        
        self.GET_DESPAWNPOINT_X, self.GET_DESPAWNPOINT_Y = self.ARENA_WIDTH/2.1, self.ARENA_HEIGHT/2
        
        self.radians = math.atan2(self.GET_DESPAWNPOINT_Y - self.previous_y, self.GET_DESPAWNPOINT_X - self.previous_x)
        self.distance = math.hypot(self.GET_DESPAWNPOINT_X - self.previous_x, self.GET_DESPAWNPOINT_Y - self.previous_y) / self.SPEED
        self.distance = int(self.distance)    
        
        self.distance_x = math.cos(self.radians)*self.SPEED
        self.distance_y = math.sin(self.radians)*self.SPEED
        
        self.previous_x, self.previous_y = self.GET_DESPAWNPOINT_X, self.GET_DESPAWNPOINT_Y
        if (self.distance != 0):
            self.distance -= 1
            self.starting_x += self.distance_x
            self.starting_y += self.distance_y
        
        if (self.is_walk_animation == True):
            self.current_sprite += random.random() * 0.35
            if (int(self.current_sprite) >= len(self.sprites_walk)):
                self.current_sprite = 0
            self.image = self.sprites_walk[int(self.current_sprite)]   
        
        if (self.distance == 0):
            self.kill()
            self.remove()
            
    def __load_images(self, creatureType):
        """
        load sprite images (crawl/walking) to the class.
        """
        self.sprites_crawl = []
        self.sprites_crawl.append(pygame.image.load(f'.\Images\{creatureType}\crawl0.png'))
        self.sprites_crawl.append(pygame.image.load(f'.\Images\{creatureType}\crawl1.png'))
        self.sprites_crawl.append(pygame.image.load(f'.\Images\{creatureType}\crawl2.png'))
        self.sprites_crawl.append(pygame.image.load(f'.\Images\{creatureType}\crawl3.png'))
        self.sprites_crawl.append(pygame.image.load(f'.\Images\{creatureType}\crawl4.png'))
        self.sprites_crawl.append(pygame.image.load(f'.\Images\{creatureType}\crawl5.png'))
        self.sprites_walk = []
        self.sprites_walk.append(pygame.image.load(f'.\Images\{creatureType}\walk0.png'))
        self.sprites_walk.append(pygame.image.load(f'.\Images\{creatureType}\walk1.png'))
        self.sprites_walk.append(pygame.image.load(f'.\Images\{creatureType}\walk2.png'))
        self.sprites_walk.append(pygame.image.load(f'.\Images\{creatureType}\walk3.png'))       
    
    def draw(self, win):
        if (self.rect.topleft[0] > 500):
            flipped_image = pygame.transform.flip(self.image, True, False)
            return win.blit(flipped_image, (self.starting_x, self.starting_y))
        win.blit(self.image, (self.starting_x, self.starting_y))

class DefaultCreature(CreatureEntity):
    def __init__(self, x, y, ARENA_WIDTH, ARENA_HEIGHT):
        super().__init__(x, y, ARENA_WIDTH, ARENA_HEIGHT, "DefaultCreature", 0.5, 0.2)
        

class TankCreature(CreatureEntity):
    def __init__(self, x, y, ARENA_WIDTH, ARENA_HEIGHT):
        super().__init__(x, y, ARENA_WIDTH, ARENA_HEIGHT, "TankCreature", 0.25, 0.08)
    
class ScreecherCreature(CreatureEntity):
    def __init__(self, x, y, ARENA_WIDTH, ARENA_HEIGHT):
        super().__init__(x, y, ARENA_WIDTH, ARENA_HEIGHT, "ScreecherCreature", 0.75, 0.5)