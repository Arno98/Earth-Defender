import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
	
	def __init__(self, sw_settings, screen, ship):
		super(Bullet, self).__init__()
		self.screen = screen
		self.sw_settings = sw_settings
		
		self.ship_super_bullet = ship.super_bullet
		
		if self.ship_super_bullet == False:
			self.rect = pygame.Rect(0, 0, self.sw_settings.bullet_width, self.sw_settings.bullet_height)
			self.sw_settings.bullets_allowed = 3
		if self.ship_super_bullet == True:
			self.rect = pygame.Rect(0, 0, self.sw_settings.super_bullet_width, self.sw_settings.super_bullet_height)
			self.sw_settings.bullets_allowed = 10
	
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		self.y = float(self.rect.y)
		
		self.color = self.sw_settings.bullet_color
	
	def update(self):
		if self.ship_super_bullet == False:
			self.y -= self.sw_settings.bullet_speed_factor
			self.rect.y = self.y
		if self.ship_super_bullet == True:
			self.y -= self.sw_settings.bullet_speed_factor + 1
			self.rect.y = self.y
		
	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)
