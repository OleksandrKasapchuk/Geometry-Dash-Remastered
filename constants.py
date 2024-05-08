from pygame import *

game_over = 0
moving_x=False
moving_y=False
tile_size=60

#window
win_width = 1280
win_height = 720
window = display.set_mode((win_width, win_height)) 
display.set_caption("Mario Remastered")

#background
backgrounds = []
current_background = 0

background0 = transform.scale(image.load("assets/images/fone.png"), (win_width, win_height)) 
backgrounds.append(background0)


#sprites
play_button = image.load("assets/images/play_orange.png")
exit_button = image.load("assets/images/exit_orange.png")
#game
FPS = 60
clock = time.Clock() 
cd = 0
game_scene = 0
#music

mixer.init()
# mixer.music.load('Bmusic.ogg') 
# mixer.music.play()
coin_sound = mixer.Sound("assets/sounds/coin.mp3")
kiss_sound = mixer.Sound("assets/sounds/kiss.mp3")
#font
font.init()
font1 = font.Font(None, 50)
font2 = font.Font(None, 125)
lose = font2.render("YOU DIED", True, (255,0,0))
won = font2.render("YOU WIN!", True, (230,230,0))
# групи спрайтів
enemies = sprite.Group()
coins = sprite.Group()