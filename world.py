# імпортуємо файли
from pygame import *
from constants import *
from levels import *
from sprites import *
#розташування блоків
class World:
    def __init__(self, data: list):
        self.tile_list = []
        # завантажуємо картинки
        dirt_img1 = image.load('assets/images/blocks/img_dirt1.png')
        grass1 = image.load('assets/images/blocks/grass1.png')
        grass2 = image.load('assets/images/blocks/grass2.png')
        grass3 = image.load('assets/images/blocks/grass3.png')
        grass4 = image.load('assets/images/blocks/grass4.png')
        mystery_box = image.load('assets/images/blocks/mystery_box.png')
        # проходимось по списку блоків(мапа)
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == -1:
                    self.make_block(dirt_img1, col_count, row_count)
                elif tile == 1:
                    self.make_block(grass1, col_count, row_count)
                elif tile == 2:
                    self.make_block(grass2, col_count, row_count)
                elif tile == 3:
                    self.make_block(grass3, col_count, row_count)
                elif tile == 4:
                    self.make_block(grass4, col_count, row_count)
                elif tile == 5:
                    self.make_block(dirt_img1, col_count, row_count)
                elif tile == 6:
                    self.make_block(mystery_box, col_count, row_count)
                
                elif tile == 8:
                    enemy = Enemy(50, 100, tile_size*col_count, tile_size*row_count, 1, 50)
                    enemies.add(enemy)
                elif tile == 9:
                    coin = GameSprite("assets/images/crystal.png",60, 60, tile_size*col_count, tile_size*row_count)
                    coins.add(coin)
                col_count += 1
            row_count += 1
    # створення блоків
    def make_block(self, img, col_count, row_count):
        img = transform.scale(img, (tile_size, tile_size))
        img_rect = img.get_rect()
        img_rect.x = col_count * tile_size
        img_rect.y = row_count * tile_size
        tile = (img, img_rect)
        self.tile_list.append(tile)
    # промальовка ігор
    def draw(self):
        for tile in self.tile_list:
            window.blit(tile[0], (tile[1].x, tile[1].y))
    # перезапуск світу
    def reset(self):
        self.tile_list = []


world = World(level1)