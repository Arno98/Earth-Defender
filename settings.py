class Settings():
	
	def __init__(self):
		self.screen_width = 1180
		self.screen_height = 690
		self.bg_color = (0, 0, 0)
		
		self.ships_limit = 3
		
		self.bullet_width = 8
		self.bullet_height = 17
		self.bullet_color = 200, 70, 0
		self.bullets_allowed = 3
		
		self.super_bullet_width = 12
		self.super_bullet_height = 23
		
		self.alien_boss_bullet_width = 12
		self.alien_boss_bullet_height = 30
		
		self.alien_bullet_color = 30, 150, 30
		self.fleet_drop_speed = 10
		self.alien_boss_drop_speed = 20
		
		self.speedup_scale = 1.1
		self.score_scale = 1.5
		
		self.level_boss = 5
		self.end_live_boss = 30
		
		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 1.3
		self.alien_speed_factor = 1
		self.alien_bullet_speed_factor = 1.3
		self.alien_boss_bullet_speed_factor = 2
		
		self.asteroid_speed_factor = 2
		
		self.capsule_speed_factor = 2.2
		
		self.fleet_direction = 1
		
		self.alien_boss_speed_factor = 2.0
		self.alien_boss_direction = 1
		
		self.alien_points = 50
		
	def increase_speed(self):
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.asteroid_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)
		
	def increase_boss_speed(self):
		self.alien_boss_speed_factor *= self.speedup_scale
		self.alien_boss_bullet_speed_factor *= self.speedup_scale
		
		
