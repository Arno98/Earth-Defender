import pygame

from pygame.sprite import Sprite

from random import randint

class Capsule(Sprite):
	
	def __init__(self, sw_settings, screen, image):
		super(Capsule, self).__init__()
		self.sw_settings = sw_settings
		self.screen = screen
		
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		self.rect.bottom = self.screen_rect.top
		self.rect.x = self.screen_rect.left + randint(0, self.sw_settings.screen_width - self.rect.width)
		
		self.y = float(self.rect.y)
		
	def update(self):
		self.y += self.sw_settings.capsule_speed_factor
		self.rect.y = self.y
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)

