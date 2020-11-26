import pygame

class Sun():
	def __init__(self, sw_settings, screen):
		self.screen = screen
		
		self.image = pygame.image.load('images/sunn.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		self.rect.center = self.screen_rect.center
		self.rect.left = self.screen_rect.left + 50
		self.rect.top = self.screen_rect.top + 300
		
	def show_sun(self):
		self.screen.blit(self.image, self.rect)
