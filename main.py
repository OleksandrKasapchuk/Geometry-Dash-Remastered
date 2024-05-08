# імпортуємо файли
from constants import *
from levels import *
from scene import *

# головний цикл гри
while True: 
    for e in event.get(): 
        if e.type == QUIT: 
            game.finish()
    game.update()
    # оновлення малюнку на екрані
    display.update()
    clock.tick(FPS)