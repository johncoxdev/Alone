from random import randint, choice, randrange
from models import DefaultCreature, TankCreature, ScreecherCreature, Bullet
from pygame import font, draw, Rect, transform
from math import atan2, degrees

waveNumber = 1
playerHealth = 10
creaturesKilled = 0

def spawn_location_safe(locx, locy):
    if ((locx >= 100 and locx <= 900) and (locy >= 100 and locy <= 650)):
        return False
    return True

def bullet_in_bound(posx, posy, WIDTH, HEIGHT):
    if ((posx <= 0 or posx >= WIDTH) or (posy <= 0 or posy >= HEIGHT)):
        return False
    return True

def spawn_wave(waveNumber, creatureList, ARENA_WIDTH, ARENA_HEIGHT):
    amount_of_creatures = waveNumber * 2 + randrange(1, 3)
    for total_creature_x in range(0, amount_of_creatures):
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

def check_wave_count(counter, creatureList, ARENA_WIDTH, ARENA_HEIGHT):
    global waveNumber
    if (counter > 0 and counter < 15 and len(creatureList) == 0):
        spawn_wave(waveNumber, creatureList, ARENA_WIDTH, ARENA_HEIGHT)
        waveNumber += 1
        counter = 15
        return counter
    if counter == 0:
        spawn_wave(waveNumber, creatureList, ARENA_WIDTH, ARENA_HEIGHT)
        waveNumber += 1
        counter = 15
        return counter
    counter -= 1
    return counter

def is_game_finished():
    if playerHealth <= 0:
        return True
    return False

def rotate_users_gun(win, img, x, y, mx, my):
    correction_angle = 90
    gun_pos = x, y
    gun_rect = img.get_rect(center = gun_pos)
    dx, dy = mx - gun_rect.centerx, my - gun_rect.centery
    angle = degrees(atan2(-dy, dx)) - correction_angle
    
    rot_image = transform.rotate(img, angle)
    rot_image_rect = rot_image.get_rect(center = gun_rect.center)
    win.blit(rot_image, rot_image_rect.topleft)


def game_info_display(win, POSX, POSY, WIDTH, HEIGHT, counter, creaturesLeft):
    if counter == 0:
        counter = "Wave has spawned!"
        
    draw.rect(win, (33, 10, 0), Rect(POSX, POSY, WIDTH, HEIGHT))
    
    styleFont = font.SysFont("comicsans", 20, False)
    
    wave_text = styleFont.render(f"Wave: {waveNumber} | Next wave in: {counter}", True, (255, 255, 255))
    health_text = styleFont.render(f"Health: {playerHealth} | Creatures Left: {creaturesLeft} | Creatures Killed: {creaturesKilled}", True, (255, 255, 255))
    
    win.blit(wave_text, (POSX + 15, POSY + 15))
    win.blit(health_text, (POSX + 15, POSY + 45))
    
    
    
    
        