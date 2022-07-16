import random
import sys
import pygame
from models import default_creature
from utili import spawn_location_safe

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

default_creatures = pygame.sprite.Group()


for total_creature_x in range(0,100):
    random_x = random.randint(10, WIDTH-30)
    random_y = random.randint(10, HEIGHT-30)
    spawnLocation = spawn_location_safe(random_x, random_y)
    while (spawnLocation is False):
        random_x = random.randint(10, WIDTH-30)
        random_y = random.randint(10, HEIGHT-30)
        spawnLocation = spawn_location_safe(random_x, random_y)
    creature = default_creature(random_x, random_y)
    default_creatures.add(creature)
    
    
while game_active:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            game_active = False
            sys.exit()

    SCREEN.blit(BACKGROUND, (0,0))
    
    
    for default_creature in default_creatures:
        default_creature.draw(SCREEN)
        crawl_out_complete = default_creature.crawl_out()
        if (crawl_out_complete):
            default_creature.walking(3)
    pygame.display.flip()
    clock.tick(30)