def spawn_location_safe(locx, locy):
    if ((locx >= 300 and locx <= 600) and (locy >= 300 and locy <= 450)):
        return False
    return True