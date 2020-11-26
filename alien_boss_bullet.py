import pygame
from pygame.sprite import Sprite

class AlienBossBullet(Sprite):
	
	def __init__(self, sw_settings, screen, alien_boss, bullet_color):
		super(AlienBossBullet, self).__init__()
		self.screen = screen
		self.sw_settings = sw_settings
		
		self.rect = pygame.Rect(0, 0, self.sw_settings.alien_boss_bullet_width, self.sw_settings.alien_boss_bullet_height)
		self.rect.centerx = alien_boss.rect.centerx
		self.rect.bottom = alien_boss.rect.bottom
		
		self.y = float(self.rect.y)
		
		#self.color = self.sw_settings.alien_boss_bullet_color
		self.color = bullet_color
		
		self.bullet_hit = 0
		
	def update(self):
		self.y += self.sw_settings.alien_boss_bullet_speed_factor
		self.rect.y = self.y
		
	def draw_alien_boss_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)
