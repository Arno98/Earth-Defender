import pygame

class Earth():
	def __init__(self, sw_settings, screen):
		self.screen = screen
		
		self.image = pygame.image.load('images/earthhh.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
	def show_earth(self):
		self.screen.blit(self.image, self.rect)
