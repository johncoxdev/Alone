import random
import sys
import pygame
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

creatureList = pygame.sprite.Group()
bullets = pygame.sprite.Group()

def spawn_wave():
    for total_creature_x in range(0,10):
        random_x = random.randint(10, WIDTH-30)
        random_y = random.randint(10, HEIGHT-30)
        spawn_location = spawn_location_safe(random_x, random_y)
        
        while (spawn_location is False):
            random_x = random.randint(10, WIDTH-30)
            random_y = random.randint(10, HEIGHT-30)
            spawn_location = spawn_location_safe(random_x, random_y)
            
        random_creature = random.choice([DefaultCreature(random_x, random_y), TankCreature(random_x, random_y), ScreecherCreature(random_x, random_y)])
        
        creatureList.add(random_creature)    

timer = 5000
dtimer = 0

spawn_wave()

while game_active:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            game_active = False
            sys.exit()
        # if (event.type == pygame.MOUSEBUTTONDOWN):
        #     mousex, mousey = pygame.mouse.get_pos()
        #     bullet = Bullet(mousex, mousey, 10)
        #     bullets.add(bullet)

    SCREEN.blit(BACKGROUND, (0,0))
    
    timer -= dtimer
    if (timer <= 0):
        spawn_wave()
        timer = 5000
    dtimer = clock.tick(60)

    mouse = pygame.mouse.get_pressed()
    
    if mouse[0]:
        mousex, mousey = pygame.mouse.get_pos()
        bullet = Bullet(mousex, mousey, 10)
        bullets.add(bullet)
        
    for bullet in bullets:
        bullet.shoot(SCREEN)
        collision = pygame.sprite.spritecollide(bullet, creatureList, True)
        if collision:
            bullet.kill()
            bullet.remove(bullets)
        
    
    for default_creature in creatureList:
        default_creature.draw(SCREEN)
        crawl_out_complete = default_creature.crawl_out()
        if (crawl_out_complete):
            default_creature.walking()
    pygame.display.flip()
    clock.tick(60)