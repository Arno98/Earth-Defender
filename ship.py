import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	
	def __init__(self, sw_settings, screen):
		super(Ship, self).__init__()
		self.screen = screen
		self.sw_settings = sw_settings
		
		self.image = pygame.image.load('images/starship.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		self.center = float(self.rect.centerx)
		
		self.moving_right = False
		self.moving_left = False
		
		self.shield = False
		self.super_speed = False
		self.super_bullet = False
		
		self.stop_shield = 0
		self.stop_super_speed = 0
		self.stop_super_bullet = 0
		
	def update(self):
		if self.super_speed == False:
			if self.moving_right and self.rect.right < self.screen_rect.right:
				self.center += self.sw_settings.ship_speed_factor
			if self.moving_left and self.rect.left > 0:
				self.center -= self.sw_settings.ship_speed_factor 
		if self.super_speed == True:
			if self.moving_right and self.rect.right < self.screen_rect.right:
				self.center += (self.sw_settings.ship_speed_factor + 1)
			if self.moving_left and self.rect.left > 0:
				self.center -= (self.sw_settings.ship_speed_factor  + 1)
			
		self.rect.centerx = self.center	
		
	def center_ship(self):
		self.center = self.screen_rect.centerx
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)
