import sys
import pygame
import utili
import tkinter

pygame.init()
pygame.display.set_caption('Alone v1.0.0')

SIZE = WIDTH, HEIGHT = 1000, 850
ARENA_WIDTH, ARENA_HEIGHT = WIDTH, HEIGHT - 100
INFO_DISPLAY_WIDTH, INFO_DISPLAY_HEIGHT, INFO_DISPLAY_X, INFO_DISPLAY_Y = WIDTH, HEIGHT - ARENA_HEIGHT, 0, HEIGHT - (HEIGHT - ARENA_HEIGHT)
SCREEN = pygame.display.set_mode(SIZE)
BACKGROUND = pygame.image.load(".\Images\Terrain\\background.png")
GUN = pygame.image.load(".\Images\Terrain\\gun.png").convert_alpha()
clock = pygame.time.Clock()
game_active = True
creatureList = pygame.sprite.Group()
bullets = pygame.sprite.Group()
gun_cooled = True
counter = 15
WAVENUMBER = 1
pygame.time.set_timer(pygame.USEREVENT + 0, 1000)
pygame.time.set_timer(pygame.USEREVENT + 1, 1000)
utili.spawn_wave(WAVENUMBER, creatureList, ARENA_WIDTH, ARENA_HEIGHT)

while game_active:
    
    mouse = pygame.mouse.get_pressed()
    mousex, mousey = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if (event.type == pygame.USEREVENT + 0):
            counter = utili.check_wave_count(counter, creatureList, ARENA_WIDTH, ARENA_HEIGHT)
        
        if (event.type == pygame.USEREVENT + 1):
            gun_cooled = False
        
        # NOTE: This toggles a manual click shooting action
        if (event.type == pygame.MOUSEBUTTONDOWN):
            bullets = utili.create_bullet(mousex, mousey, ARENA_WIDTH, ARENA_HEIGHT, bullets)
        
        if (event.type == pygame.QUIT):
            game_active = False
            sys.exit()
    
    gun_cooled = True
    
    SCREEN.blit(BACKGROUND, (0,0))
    utili.game_info_display(SCREEN, INFO_DISPLAY_X, INFO_DISPLAY_Y, INFO_DISPLAY_WIDTH, INFO_DISPLAY_HEIGHT, counter, len(creatureList))
    
        
    for bullet in bullets:
        bullet.shoot(SCREEN)
        collision = pygame.sprite.spritecollide(bullet, creatureList, False, pygame.sprite.collide_circle_ratio(2))
        if collision:
            bullet.kill()
            bullet.remove(bullets)
            dead = collision[0].take_damage(creatureList)
            if dead:
                utili.creaturesKilled += 1
            
    
    utili.rotate_users_gun(SCREEN, GUN, ARENA_WIDTH/2.1, ARENA_HEIGHT/2, mousex, mousey)
    
    for default_creature in creatureList:
        default_creature.draw(SCREEN)
        default_creature.show_creature_health(SCREEN)
        crawl_out_complete = default_creature.crawl_out()
        reached_user = default_creature.if_reached_middle()
        if (crawl_out_complete):
            default_creature.walking()
        if (reached_user):
            utili.playerHealth -= 1

    game_finished = utili.is_game_finished()
    if (game_finished):
        game_active = False
        tk_window = tkinter.Tk()
        tk_window.title("Game Over -- Thank you for playing!")
        tk_label = tkinter.Label(text="Game Over", font=("comicsans", 70), bg="BLACK", fg="WHITE")
        tk_label.pack()
        tk_window.eval('tk::PlaceWindow . center')
        tk_window.mainloop()
    
    pygame.display.flip()
    clock.tick(60)