import random
import sys
import pygame
from utili import spawn_wave, create_bullet

pygame.init()
pygame.display.set_caption('Alone v1.0.0')

SIZE = WIDTH, HEIGHT = 1000, 850
ARENA_WIDTH, ARENA_HEIGHT = WIDTH, HEIGHT - 100
SCREEN = pygame.display.set_mode(SIZE)
BACKGROUND = pygame.image.load(".\Images\Terrain\\background.png")
HOUSE = pygame.image.load(".\Images\Terrain\house.png")
clock = pygame.time.Clock()
game_active = True
creatureList = pygame.sprite.Group()
bullets = pygame.sprite.Group()
timer = 5000
dtimer = 0

spawn_wave(creatureList, ARENA_WIDTH, ARENA_HEIGHT)

while game_active:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            game_active = False
            sys.exit()
        """
        // NOTE: This toggles a manual click shooting action
        if (event.type == pygame.MOUSEBUTTONDOWN):
           mousex, mousey = pygame.mouse.get_pos()
           bullet = Bullet(mousex, mousey, 10)
           bullets.add(bullet)
        """
    SCREEN.blit(BACKGROUND, (0,0))
    SCREEN.fill
    
    timer -= dtimer
    if (timer <= 0):
        creatureList = spawn_wave(creatureList, ARENA_WIDTH, ARENA_HEIGHT)
        timer = 5000
    dtimer = clock.tick(60)

    mouse = pygame.mouse.get_pressed()
    
    """
    NOTE: This is a machine gun style of shooting, which 
    will be the default shooting with cooldowns.
    """
    if mouse[0]:
        mousex, mousey = pygame.mouse.get_pos()
        bullets = create_bullet(mousex, mousey, ARENA_WIDTH, ARENA_HEIGHT, bullets)
        
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