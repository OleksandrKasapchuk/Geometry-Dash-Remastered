# імпортуємо файли
from pygame import *
from constants import *

# клас звичайних спрайтів
class GameSprite(sprite.Sprite): 
    def __init__(self, player_image, size_x, size_y, player_x, player_y): 
        super().__init__() 
        self.image = transform.scale(image.load(player_image), (size_x, size_y)) 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 
        self.size_x, self.size_y = size_x, size_y 

# клас ворога
class Enemy(sprite.Sprite): 
    def __init__(self, size_x, size_y, player_x, player_y, player_speed, moving_lenth): 
        super().__init__() 
        self.size_x, self.size_y = size_x, size_y 
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        self.direction = 1
        self.move_counter = 0
        self.moving_lenth = moving_lenth
        for num in range(2):
            img_right = image.load(f'assets/images/player/princess{num}.png')
            img_right = transform.scale(img_right, (self.size_x, self.size_y))
            img_left = transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.image = self.images_right[self.index]
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 

    # ходьба та анімація
    def update(self):
        walk_cooldown = 2
        self.rect.x += self.speed
        self.move_counter += 1
        self.counter += 1
        if abs(self.move_counter) > self.moving_lenth:
            self.speed *= -1
            self.direction *= -1
            self.move_counter *= -1
        if self.counter > walk_cooldown:
            self.counter = 0	
            self.index += 1
        if self.index >= len(self.images_right):
            self.index = 0
        if self.direction == 1:
            self.image = self.images_right[self.index]
        if self.direction == -1:
            self.image = self.images_left[self.index]


#клас кулі
class Bullet(sprite.Sprite):
    def __init__(self, player_x, player_y, size_x, size_y, direction, exploded):
        super().__init__()

        self.image = transform.scale(image.load("assets/images/heart.png"),(size_x, size_y))
        self.side_offset = 0
        self.up_down_offset = 0
        self.rotation = 0
        self.explosion_index = 0
        self.explosion_counter = 0
        self.explosion_duration = 10
        self.exploded = exploded
        self.size_x = size_x 
        self.size_y = size_y 
        self.speed = 10
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = direction
        if direction in [1, -1]: 
            self.rotation = 270 if direction == 1 else 90 
            self.image = transform.flip(self.image, True, False) 
        elif direction in [2, -2]: 
            self.rotation = 0 if direction == 2 else 180 
        self.image = transform.rotate(self.image, self.rotation) 

        # якщо направо
        if direction == 1: 
            self.rotation = 180 
            self.image = transform.flip(self.image, True, False) 
            self.side_offset = 3 
            self.up_down_offset = 5 
        # якщо наліво
        elif direction == -1: 
            self.rotation = 0 
            self.side_offset = -43 
            self.up_down_offset = 6 

        self.rect.x += self.side_offset 
        self.rect.y += self.up_down_offset
    # метод оновлення кулі
    def update(self):
        dx, dy = 0, 0
        #пересування
        if self.direction == 1:
            dx += self.speed
        elif self.direction == -1:
            dx -= self.speed
        if self.exploded:
            self.explode()
            # self.show_explosion()
    
    # колізія
        for enemy in enemies:
            if enemy.rect.colliderect(self.rect.x, self.rect.y, self.size_x, self.size_y):
                self.exploded = True
                
        #рух
        self.rect.x += dx
        self.rect.y += dy

    #вибух кулі    
    def explode(self):
        self.kill()
        kiss_sound.play()
        # self.exploded = True
    # #анімацію вибуху
    # def show_explosion(self):
    #     if self.explosion_counter < self.explosion_duration:
    #         window.blit(self.explosion_images[self.explosion_index], (self.rect.x, self.rect.y))
    #         self.explosion_counter += 1
    #     else:
    #         self.explosion_counter = 0
    #         self.explosion_index += 1
    #         if self.explosion_index >= len(self.explosion_images):
    #             self.exploded = False
    #             self.explosion_index = 0 