WIDTH, HEIGHT = 1000, 750

def spawn_location_safe(locx, locy):
    if ((locx >= 100 and locx <= 900) and (locy >= 100 and locy <= 650)):
        return False
    return True

def bullet_in_bound(posx, posy):
    if ((posx <= 0 or posx >= WIDTH) and (posy <= 0 or posy >= HEIGHT)):
        return False
    return True