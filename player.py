# імпортуємо файли
from pygame import *
from constants import *
from world import *


# клас гравця
class Player(sprite.Sprite): 
    def __init__(self, size_x, size_y, player_x, player_y): 
        super().__init__() 
        self.size_x, self.size_y = size_x, size_y
        # списки медіа гравця
        self.images_right1 = []
        self.images_left1 = []
        self.images_right2 = []
        self.images_left2 = []
        self.index = 0
        # завантажуємо медіа гравця
        for num in range(2):
            img_right = image.load(f'assets/images/player/mario{num}.png')
            img_right = transform.scale(img_right, (self.size_x, self.size_y))
            img_left = transform.flip(img_right, True, False)
            self.images_right1.append(img_right)
            self.images_left1.append(img_left)
        for num in range(0,2):
            img_right = image.load(f'assets/images/player/princess{num}.png')
            img_right = transform.scale(img_right, (self.size_x, self.size_y))
            img_left = transform.flip(img_right, True, False)
            self.images_right2.append(img_right)
            self.images_left2.append(img_left)
        
        self.direction = 0
        self.image = self.images_right1[self.index]
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 
        self.counter = 0
        self.walk_cooldown = 2
        # перевірка чи стрибнув
        self.jumped = False
        self.vel_y = 0
        self.gravity = True
        # рух
        self.dx = 0
        self.dy = 0
        # змінні персонажа
        self.character = 1
        self.changed = 0
        # частота стрільби
        self.last_shot_time = -2000  
        self.shoot_cooldown = 2500
        self.shooting = False

        self.bullets = sprite.Group()
    # метод стрільби
    def fire(self):
        #створення кулі(постріл)
        bullet = Bullet(self.rect.centerx, self.rect.top, 45, 45, self.direction, False)
        self.bullets.add(bullet)
    # метод промальовки гравця
    def reset(self):
        window.blit(self.image, (self.rect.x - self.dx, self.rect.y))
    # метод анімації
    def animate(self, list1, list2):
        if self.counter > self.walk_cooldown:
            self.counter = 0	
            self.index += 1
            if self.index >= len(list1):
                self.index = 0
            if self.direction == 1:
                self.image = list1[self.index]
            if self.direction == -1:
                self.image = list2[self.index]
    # метод оновлення гравця
    def update(self):
        # перевірка на персонажа
        if self.character == 1:
            rights = self.images_right1
            lefts = self.images_left1
        if self.character == 2:
            rights = self.images_right2
            lefts = self.images_left2
        self.dx = 0
        self.dy = 0
        # дістаємо актуальний час
        current_time = time.get_ticks()
        
        keys = key.get_pressed()
        # стрільба 
        if keys[K_LCTRL] and self.character == 2:
            self.fire()
        if keys[K_LSHIFT]:
            if current_time - self.changed > 2500:
                if self.character == 1:
                    self.character = 2
                else:
                    self.character = 1
                self.changed = time.get_ticks()
        # рух направо
        if keys[K_d] or keys[K_RIGHT] and self.rect.x < win_width - self.size_x: 
            self.dx = 5
            self.counter += 1
            self.direction = 1
            self.animate(rights, lefts)
        # рух наліво
        elif keys[K_a] or keys[K_LEFT] and  self.rect.x > 0:
            self.dx = -5
            self.counter += 1
            self.direction = -1
            self.animate(rights, lefts)
        # стрибок
        if keys[K_SPACE] and self.jumped == False:
            self.vel_y = -18
            self.jumped=True
        # якщо стоїть на місці
        if keys[K_LEFT] == False and keys[K_a] == False and keys[K_RIGHT] == False and keys[K_d] == False:
            self.counter = 0
            self.index = 0
            if self.direction == 1:
                self.image = rights[self.index]
            if self.direction == -1:
                self.image = lefts[self.index]
        # гравітація
        self.vel_y += 1
        if self.vel_y > 20:
            self.vel_y = 20
        self.dy += self.vel_y
        if self.rect.bottom > win_height:
            self.rect.bottom = win_height
            self.vel_y = 0
            self.dy = self.vel_y
        # оновлення куль
        for bullet in self.bullets:
            bullet.update()
        #перевіряємо на колізію
        for tile in world.tile_list:
            #колізія по х
            if tile[1].colliderect(self.rect.x + self.dx, self.rect.y - 1, self.size_x, self.size_y):
                self.dx = 0
            #колізія по у
            if tile[1].colliderect(self.rect.x, self.rect.y + self.dy, self.size_x, self.size_y):
                #check if below the ground i.e. jumping
                if self.vel_y < 0:
                    self.dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                #check if above the ground i.e. falling
                elif self.vel_y >= 0:
                    self.dy = tile[1].top - self.rect.bottom
                    self.gravity = False
                    self.jumped=False
                    self.vel_y = 0

# створення гравця
player = Player(40,85, 400, 500)