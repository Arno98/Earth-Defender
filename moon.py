import pygame

class Moon():
	def __init__(self, sw_settings, screen):
		self.screen = screen
		
		self.image = pygame.image.load('images/moonn.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		self.rect.center = self.screen_rect.center
		self.rect.right = self.screen_rect.right - 200
		self.rect.top = self.screen_rect.top + 250
		
	def show_moon(self):
		self.screen.blit(self.image, self.rect)
