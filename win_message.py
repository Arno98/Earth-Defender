import pygame.font

class WinMessage():
	
	def __init__(self, sw_settings, screen, msg):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		self.width, self.height = 200, 70
		self.button_color = (34, 139, 34)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont('impact', 48)
		
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.centery = self.screen_rect.centery - 180
		self.rect.centerx = self.screen_rect.centerx
		
		self.prep_msg(msg)
		
	def prep_msg(self, msg):
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
		
	def draw_win_message(self):
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
