from random import randint, choice
from models import DefaultCreature, TankCreature, ScreecherCreature, Bullet

def spawn_location_safe(locx, locy):
    if ((locx >= 100 and locx <= 900) and (locy >= 100 and locy <= 650)):
        return False
    return True

def bullet_in_bound(posx, posy, WIDTH, HEIGHT):
    if ((posx <= 0 or posx >= WIDTH) or (posy <= 0 or posy >= HEIGHT)):
        return False
    return True

def spawn_wave(creatureList, ARENA_WIDTH, ARENA_HEIGHT):
    for total_creature_x in range(0,20):
        random_x = randint(10, ARENA_WIDTH-30)
        random_y = randint(10, ARENA_HEIGHT-30)
        spawn_location = spawn_location_safe(random_x, random_y)
        
        while (spawn_location is False):
            random_x = randint(10, ARENA_WIDTH-30)
            random_y = randint(10, ARENA_HEIGHT-30)
            spawn_location = spawn_location_safe(random_x, random_y)
            
        random_creature = choice([
            DefaultCreature(random_x, random_y, ARENA_WIDTH, ARENA_HEIGHT),
            TankCreature(random_x, random_y, ARENA_WIDTH, ARENA_HEIGHT),
            ScreecherCreature(random_x, random_y, ARENA_WIDTH, ARENA_HEIGHT)
        ])
        creatureList.add(random_creature)
    return creatureList   

def create_bullet(mousex, mousey, ARENA_WIDTH, ARENA_HEIGHT, bullets):
    bullet = Bullet(mousex, mousey, 10, ARENA_WIDTH, ARENA_HEIGHT)
    bullets.add(bullet)
    return bullets
        