import random
import sys
import pygame
from time import sleep
from models import DefaultCreature, TankCreature, ScreecherCreature, Bullet
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

for total_creature_x in range(0,50):
    random_x = random.randint(10, WIDTH-30)
    random_y = random.randint(10, HEIGHT-30)
    spawn_location = spawn_location_safe(random_x, random_y)
    
    while (spawn_location is False):
        random_x = random.randint(10, WIDTH-30)
        random_y = random.randint(10, HEIGHT-30)
        spawn_location = spawn_location_safe(random_x, random_y)
        
    random_creature = random.choice([DefaultCreature(random_x, random_y), TankCreature(random_x, random_y), ScreecherCreature(random_x, random_y)])
    
    default_creatures.add(random_creature)    

bullets = pygame.sprite.Group()

while game_active:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            game_active = False
            sys.exit()
        if (event.type == pygame.MOUSEBUTTONDOWN):
            mousex, mousey = pygame.mouse.get_pos()
            bullet = Bullet(mousex, mousey)
            bullets.add(bullet)

    SCREEN.blit(BACKGROUND, (0,0))

    mouse = pygame.mouse.get_pressed()
        
    for bullet in bullets:
        bullet.shoot(SCREEN)
    
    for default_creature in default_creatures:
        default_creature.draw(SCREEN)
        crawl_out_complete = default_creature.crawl_out()
        if (crawl_out_complete):
            default_creature.walking()
    pygame.display.flip()
    clock.tick(30)