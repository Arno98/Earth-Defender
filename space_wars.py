import pygame

from pygame.sprite import Group

from settings import Settings

from game_stats import GameStats

from earth import Earth

from moon import Moon

from sun import Sun

from scoreboard import Scoreboard

from button import Button

from pause_message import PauseMessage

from win_message import WinMessage

from game_over_message import LoseMessage

from ship import Ship

import game_functions as gf

def run_game():
	pygame.init()
	pygame.mixer.music.load('music/Phantom from Space.mp3')
	pygame.mixer.music.play(-1)
	pygame.mixer.music.set_volume(0.5)
	sw_settings = Settings()
	screen = pygame.display.set_mode((sw_settings.screen_width, sw_settings.screen_height))
	pygame.display.set_caption("Earth's Defender")
	earth = Earth(sw_settings, screen)
	moon = Moon(sw_settings, screen)
	sun = Sun(sw_settings, screen) 
	play_button = Button(sw_settings, screen, "Play")
	pause_message = PauseMessage(sw_settings, screen, "Pause")
	win_message = WinMessage(sw_settings, screen, "You win!")
	lose_message = LoseMessage(sw_settings, screen, "You lose!")
	game_stats = GameStats(sw_settings)
	scoreboard = Scoreboard(sw_settings, screen, game_stats)
	ship = Ship(sw_settings, screen)
	bullets = Group()
	aliens = Group()
	aliens_bullets = Group()
	alien_boss_bullets = Group()
	asteroids = Group()
	capsules_shield = Group()    
	capsules_bullet = Group()
	capsules_speed = Group()
	aliens_bosses = pygame.sprite.GroupSingle()
	gf.create_fleet(sw_settings, screen, ship, aliens)
	#gf.create_alien_boss(sw_settings, screen, aliens_bosses)
	
	while True:
		gf.check_events(sw_settings, screen, game_stats, scoreboard, play_button, pause_message, ship, aliens, bullets, aliens_bullets, asteroids, aliens_bosses, alien_boss_bullets, capsules_shield, capsules_speed, capsules_bullet)
		if game_stats.game_active and game_stats.game_pause:
			ship.update()
			gf.update_bullets(sw_settings, screen, game_stats, scoreboard, ship, aliens, bullets, aliens_bullets, asteroids, aliens_bosses, alien_boss_bullets, capsules_shield, capsules_speed, capsules_bullet)
			gf.update_aliens(sw_settings, game_stats, scoreboard, screen, ship, aliens, bullets, aliens_bullets, asteroids, alien_boss_bullets, aliens_bosses, capsules_shield, capsules_speed, capsules_bullet)
			gf.check_alien_fires(sw_settings, screen, aliens, aliens_bullets)
			gf.update_aliens_bullets(sw_settings, game_stats, scoreboard, screen, ship, aliens, bullets, aliens_bullets, asteroids, alien_boss_bullets, aliens_bosses, capsules_shield, capsules_speed, capsules_bullet)
			gf.check_asteroid_fall(sw_settings, screen, asteroids)
			gf.update_asteroids(sw_settings, game_stats, scoreboard, screen, ship, aliens, bullets, aliens_bullets, asteroids, aliens_bosses, alien_boss_bullets, capsules_shield, capsules_speed, capsules_bullet)
			gf.check_capsule_fall(sw_settings, screen, capsules_shield, capsules_bullet, capsules_speed)
			gf.update_capsules(sw_settings, screen, capsules_shield, capsules_bullet, capsules_speed, ship, aliens_bullets)
			gf.update_alien_boss(sw_settings, screen, game_stats, aliens_bosses, aliens, aliens_bullets, bullets, asteroids)
			gf.check_alien_boss_fires(sw_settings, screen, aliens_bosses, alien_boss_bullets, game_stats, aliens)
			gf.update_alien_boss_bullet(sw_settings, game_stats, scoreboard, screen, ship, aliens, bullets, aliens_bullets, asteroids, alien_boss_bullets, aliens_bosses, capsules_shield, capsules_speed, capsules_bullet)
		gf.update_screen(sw_settings, screen, earth, moon, sun, game_stats, scoreboard, ship, aliens, bullets, aliens_bullets, asteroids, capsules_shield, capsules_bullet, capsules_speed, play_button, pause_message, win_message, lose_message, aliens_bosses, alien_boss_bullets)
run_game()
