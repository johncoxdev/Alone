import random
import sys
import pygame
from models import Zombie

"""
TODO:
.) extend the screen so that there is a scorebaord and counters
"""

pygame.init()
pygame.display.set_caption('Alone v1.0.0')

clock = pygame.time.Clock()
SIZE = WIDTH, HEIGHT = 1000, 750
SCREEN = pygame.display.set_mode(SIZE)
game_active = True
BACKGROUND = pygame.image.load(".\Images\Terrain\\background.png")
HOUSE = pygame.image.load(".\Images\Terrain\house.png")

zombies = pygame.sprite.Group()

for zombie_amount in range(0,100):
    random_x = random.randint(10, WIDTH-30)
    random_y = random.randint(10, HEIGHT-30)
    zombie = Zombie(random_x, random_y)
    zombies.add(zombie)
    
    
while game_active:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            game_active = False
            sys.exit()

    SCREEN.blit(BACKGROUND, (0,0))
    
    
    for zombie in zombies:
        zombie.draw(SCREEN)
        zombie.crawl_out()
        zombie.walking()
    pygame.display.flip()
    clock.tick(30)