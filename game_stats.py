class GameStats():
	
	def __init__(self, sw_settings):
		self.sw_settings = sw_settings
		self.reset_stats()
		self.game_active = False
		self.game_pause = True
		
		with open('recordscore.txt') as file_object:
			self.high_score = int(file_object.read())
		
	def reset_stats(self):
		self.ships_left = self.sw_settings.ships_limit
		self.score = 0
		self.level = 1
