#імпортуємо файли
from constants import *
from pygame import *
from world import *
from sprites import *
from button import *
from player import *
import sys

#клас сцени гри
class GameScene:
	def __init__(self):
		self.player = player
		self.world = world
		self.btn_play = btn_play
		self.btn_exit = btn_exit
		self.scene = 0
		self.window = window
		self.coins_collected = 0
		self.coins = coins
		self.enemies = enemies
		self.all_sprites = [*self.coins, *self.enemies, player]
	#оновлення сцени гри
	def update(self):
		self.window.blit(background0,(0,0))
		# сцена програшу
		if self.scene == -1:
			self.window.fill((0,0,0))
			for enemy in self.enemies:
				enemy.kill()
			self.player.kill()
			self.world.reset()
			window.blit(lose, (200,400))
		# стартове меню
		if self.scene == 0:
			self.btn_play.draw()
			self.btn_exit.draw()
			# якщо натиснуто
			if btn_play.clicked:
				self.scene = 1
			if btn_exit.clicked:
				self.finish()
		# сцена гри
		elif self.scene == 1:
			self.world.draw()
			self.player.update()
			self.player.reset()
			self.player.bullets.draw(self.window )
			self.enemies.draw(self.window)
			self.coins.draw(self.window)
			coin_text = font1.render("Coin: " + str(self.coins_collected),1, (0,0,0))
			window.blit(coin_text, (1150, 25))
			for enemy in self.enemies:
				enemy.update()
				# перевірка на колізію гравця з ворогом
				if enemy.rect.colliderect(self.player.rect.x, self.player.rect.y, self.player.size_x, self.player.size_y):
					self.scene = -1
			
			for coin in self.coins:
				# перевірка на колізію гравця з монетами
				if coin.rect.colliderect(self.player.rect.x, self.player.rect.y, self.player.size_x, self.player.size_y):
					coin.kill()
					self.coins_collected += 1
					coin_sound.play()
			
			# перевірка чи початок карти не переміщався далі за 0 по х
			if self.world.tile_list[0][1].x >= 0 and self.player.dx < 0 or self.world.tile_list[-1][1].x <= win_width and self.player.dx > 0:
				self.player.rect.x += self.player.dx
			# перевірка чи кінець карти не переміщався далі по х
			elif (win_width - self.player.rect.x > 400 and self.player.dx > 0) or (self.player.rect.x > 400 and self.player.dx < 0):
				self.player.rect.x += self.player.dx
			else:
				# зсув блоків та спрайтів
				for block in self.world.tile_list:
					block[1].x -= self.player.dx
				for sprite in self.all_sprites[:-1]:
					sprite.rect.x -= self.player.dx

			self.player.rect.y += self.player.dy
	# вихід з гри
	def finish(self):
		quit()
		sys.exit()


game = GameScene()