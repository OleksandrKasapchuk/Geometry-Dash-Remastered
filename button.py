from pygame import *
from constants import *
# кнопка
class Button():
    def __init__(self, btn_image, x, y, size_x, size_y):
        self.image = btn_image
        self.rect = self.image.get_rect()
        self.size_x, self.size_y = size_x, size_y 
        self.rect.x = x
        self.rect.y = y
        self.index = 0
        self.wait = 5
        self.clicked = False
        self.action = False
        self.image = btn_image

    def draw(self):

        if self.index > 1:
            self.index = 0
        window.blit(self.image, (self.rect.x, self.rect.y))
        #отримуємо позицію кнопки
        pos = mouse.get_pos()
        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.action = True
                self.clicked = True
                
        if mouse.get_pressed()[0] == 0:
            self.clicked = False

btn_play = Button(play_button , 200, 300, 90, 90)
btn_exit = Button(exit_button, 500, 300, 90, 90)