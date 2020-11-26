import sys

import pygame

from time import sleep

import random

from bullet import Bullet

from alien import Alien

from alien_bullet import AlienBullet

from alien_boss_bullet import AlienBossBullet

from asteroid import Asteroid

from capsule import Capsule

from alien_boss import AlienBoss

def check_keydown_events(event, sw_settings, screen, game_stats, scoreboard, play_button, pause_message, ship, aliens, bullets, aliens_bullets, asteroids, aliens_bosses, alien_boss_bullets, capsules_shield, capsules_speed, capsules_bullet):
	if event.key == pygame.K_RIGHT:
	    ship.moving_right = True
	if event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(sw_settings, screen, ship, bullets)
	elif event.key == pygame.K_PAUSE:
		game_stats.game_pause = False
		pygame.mixer.music.set_volume(0.5)
		while game_stats.game_pause:
			sleep(1)
			check_events(sw_settings, screen, game_stats, scoreboard, play_button, ship, aliens, bullets, aliens_bullets, asteroids, aliens_bosses, alien_boss_bullets, capsules_shield, capsules_speed, capsules_bullet)
	elif event.key == pygame.K_ESCAPE:
		game_stats.game_pause = True
		pygame.mixer.music.set_volume(1)
	elif event.key == pygame.K_q:
		with open('recordscore.txt', 'w') as file_object:
			file_object.write(str(game_stats.high_score))
		sys.exit()
	elif event.key == pygame.K_p and not game_stats.game_active:
		start_game(sw_settings, screen, game_stats, scoreboard, play_button, ship, aliens, bullets, aliens_bullets, asteroids, capsules_shield, capsules_speed, capsules_bullet)
		
def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(sw_settings, screen, game_stats, scoreboard, play_button, pause_message, ship, aliens, bullets, aliens_bullets, asteroids, aliens_bosses, alien_boss_bullets, capsules_shield, capsules_speed, capsules_bullet):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(sw_settings, screen, game_stats, scoreboard, play_button, ship, aliens, bullets, aliens_bullets, asteroids, mouse_x, mouse_y, aliens_bosses, alien_boss_bullets, capsules_shield, capsules_speed, capsules_bullet)
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, sw_settings, screen, game_stats, scoreboard, play_button, pause_message, ship, aliens, bullets, aliens_bullets, asteroids, aliens_bosses, alien_boss_bullets, capsules_shield, capsules_speed, capsules_bullet)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
			
def check_play_button(sw_settings, screen, game_stats, scoreboard, play_button, ship, aliens, bullets, aliens_bullets, asteroids, mouse_x, mouse_y, aliens_bosses, alien_boss_bullets, capsules_shield, capsules_speed, capsules_bullet):
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not game_stats.game_active:
		start_game(sw_settings, screen, game_stats, scoreboard, play_button, ship, aliens, bullets, aliens_bullets, asteroids, aliens_bosses, alien_boss_bullets, capsules_shield, capsules_speed, capsules_bullet)
		
def start_game(sw_settings, screen, game_stats, scoreboard, play_button, ship, aliens, bullets, aliens_bullets, asteroids, aliens_bosses, alien_boss_bullets, capsules_shield, capsules_speed, capsules_bullet):
	sw_settings.initialize_dynamic_settings()
	pygame.mixer.music.set_volume(1)
	pygame.mouse.set_visible(False)
	game_stats.reset_stats()
	game_stats.game_active = True
		
	scoreboard.prep_images()
		
	aliens.empty()
	bullets.empty()
	aliens_bullets.empty()
	asteroids.empty()
	aliens_bosses.empty()
	alien_boss_bullets.empty()
	capsules_shield.empty()
	capsules_bullet.empty()
	capsules_speed.empty()
		
	create_fleet(sw_settings, screen, ship, aliens)
	
	ship.center_ship()
	
def check_asteroid_fall(sw_settings, screen, asteroids):
	random_fall = random.randint(0, 10000)
	if random_fall < 3:
		asteroid_fall(sw_settings, screen, asteroids)
		
def asteroid_fall(sw_settings, screen, asteroids):
	asteroid = Asteroid(sw_settings, screen)
	asteroids.add(asteroid)
	
def update_asteroids(sw_settings, game_stats, scoreboard, screen, ship, aliens, bullets, aliens_bullets, asteroids, aliens_bosses, alien_boss_bullets, capsules_shield, capsules_speed, capsules_bullet):
	asteroids.update()
	screen_rect = screen.get_rect()
	for asteroid in asteroids.copy():
		if asteroid.rect.top == screen_rect.bottom:
			asteroids.remove(asteroid)
	check_asteroid_ship_collision(sw_settings, game_stats, scoreboard, screen, ship, aliens, bullets, aliens_bullets, asteroids, alien_boss_bullets, aliens_bosses, capsules_shield, capsules_speed, capsules_bullet)
	check_asteroid_alien_collision(sw_settings, screen, asteroids, aliens, capsules_shield, capsules_speed, capsules_bullet)
	check_asteroid_bullets_collision(sw_settings, screen, asteroids, bullets, aliens_bullets)
	check_asteroid_boss_collision(sw_settings, screen, asteroids, aliens_bosses, game_stats, scoreboard, ship, aliens, bullets, aliens_bullets, alien_boss_bullets, capsules_shield, capsules_speed, capsules_bullet)
	
def check_capsule_fall(sw_settings, screen, capsules_shield, capsules_bullet, capsules_speed):
	random_fall_s = random.randint(0, 5000)
	random_fall_b = random.randint(0, 6000)
	random_fall_c = random.randint(0, 7000)
	if random_fall_s < 3:
		capsule_fall_s(sw_settings, screen, capsules_shield)
	if random_fall_b < 3:
		capsule_fall_b(sw_settings, screen, capsules_bullet)
	if random_fall_c < 3:
		capsule_fall_c(sw_settings, screen, capsules_speed)
				
def capsule_fall_s(sw_settings, screen, capsules_shield):
	capsule_s = Capsule(sw_settings, screen, 'images/capsule_shield.png')
	capsules_shield.add(capsule_s)

def capsule_fall_b(sw_settings, screen, capsules_bullet):
	capsule_b = Capsule(sw_settings, screen, 'images/capsule_bullet.png')
	capsules_bullet.add(capsule_b)
	
def capsule_fall_c(sw_settings, screen, capsules_speed):
	capsule_c = Capsule(sw_settings, screen, 'images/capsule_speed.png')
	capsules_speed.add(capsule_c)
	
def update_capsules(sw_settings, screen, capsules_shield, capsules_bullet, capsules_speed, ship, aliens_bullets):
	for capsule in capsules_shield, capsules_bullet, capsules_speed:
		capsule.update()

	screen_rect = screen.get_rect()
	
	for capsule_s in capsules_shield.copy():
		if capsule_s.rect.top == screen_rect.bottom:
			capsules_shield.remove(capsule_s)	
			
	for capsule_b in capsules_bullet.copy():
		if capsule_b.rect.top == screen_rect.bottom:
			capsules_bullet.remove(capsule_b) 
			
	for capsule_c in capsules_speed.copy():
		if capsule_c.rect.top == screen_rect.bottom:
			capsules_speed.remove(capsule_c)
			
	check_capsule_shield_ship_collision(sw_settings, screen, capsules_shield, ship, aliens_bullets)
	check_capsule_bullet_ship_collision(sw_settings, screen, capsules_bullet, ship)
	check_capsule_speed_ship_collision(sw_settings, screen, capsules_speed, ship)


def check_capsule_shield_ship_collision(sw_settings, screen, capsules_shield, ship, aliens_bullets):
	if pygame.sprite.spritecollide(ship, capsules_shield, True):
		ship.image = pygame.image.load('images/starship_shieldd.png')
		ship.shield = True
	
		ship.stop_shield = int(pygame.time.get_ticks() / 1000) + 10
	
	check_timer(sw_settings, screen, ship)
		
def check_capsule_bullet_ship_collision(sw_settings, screen, capsules_bullet, ship):	
	if pygame.sprite.spritecollide(ship, capsules_bullet, True):
		ship.super_bullet = True
		ship.stop_super_bullet = int(pygame.time.get_ticks() / 1000) + 10
		
	check_timer(sw_settings, screen, ship)
		
def check_capsule_speed_ship_collision(sw_settings, screen, capsules_speed, ship):
	if pygame.sprite.spritecollide(ship, capsules_speed, True):
		ship.super_speed = True
		ship.stop_super_speed = int(pygame.time.get_ticks() / 1000) + 10
		
	check_timer(sw_settings, screen, ship)
		
def check_timer(sw_settings, screen, ship):
	timer = int(pygame.time.get_ticks() / 1000)
	
	if timer >= ship.stop_shield:
		ship.image = pygame.image.load('images/starship.png')
		ship.shield = False
		
	if timer >= ship.stop_super_speed:
		ship.super_speed = False
		
	if timer >= ship.stop_super_bullet:
		ship.super_bullet = False

def check_asteroid_ship_collision(sw_settings, game_stats, scoreboard, screen, ship, aliens, bullets, aliens_bullets, asteroids, alien_boss_bullets, aliens_bosses, capsules_shield, capsules_speed, capsules_bullet):
	if pygame.sprite.spritecollideany(ship, asteroids):
		ship_hit(sw_settings, game_stats, scoreboard, screen, ship, aliens, bullets, aliens_bullets, asteroids, alien_boss_bullets, aliens_bosses, capsules_shield, capsules_speed, capsules_bullet)
		
def check_asteroid_alien_collision(sw_settings, screen, aliens, asteroids, capsules_shield, capsules_speed, capsules_bullet):
	asteroid_alien_collsion = pygame.sprite.groupcollide(asteroids, aliens, True, False)
	
def check_asteroid_bullets_collision(sw_settings, screen, asteroids, bullets, aliens_bullets):
	asteroid_bullet_collsion = pygame.sprite.groupcollide(asteroids, bullets, False, True)
	asteroid_alien_bullet_collision = pygame.sprite.groupcollide(asteroids, aliens_bullets, False, True)
	
def check_asteroid_boss_collision(sw_settings, screen, asteroids, aliens_bosses, game_stats, scoreboard, ship, aliens, bullets, aliens_bullets, alien_boss_bullets, capsules_shield, capsules_speed, capsules_bullet):
	asteroid_boss_collison = pygame.sprite.groupcollide(asteroids, aliens_bosses, True, False)
	if asteroid_boss_collison:
		for alien_boss in aliens_bosses:
			alien_boss.boss_hit += 1
			if alien_boss.boss_hit == sw_settings.end_live_boss:
				start_new_boss_level(sw_settings, screen, bullets, aliens_bosses, game_stats, scoreboard, ship, aliens, aliens_bullets, asteroids, alien_boss_bullets, capsules_shield, capsules_speed, capsules_bullet)

def fire_bullet(sw_settings, screen, ship, bullets):
	if len(bullets) < sw_settings.bullets_allowed:
		new_bullet = Bullet(sw_settings, screen, ship)
		bullets.add(new_bullet)
			
def update_bullets(sw_settings, screen, game_stats, scoreboard, ship, aliens, bullets, aliens_bullets, asteroids, aliens_bosses, alien_boss_bullets, capsules_shield, capsules_speed, capsules_bullet):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	check_bullet_alien_collisions(sw_settings, screen, game_stats, scoreboard, ship, aliens, bullets, asteroids, aliens_bullets, aliens_bosses, alien_boss_bullets, capsules_shield, capsules_speed, capsules_bullet)
	check_bullets_bullets_collision(sw_settings, screen, bullets, aliens_bullets)
	if game_stats.level == sw_settings.level_boss:
		if len(aliens) == 0:
			check_bullets_alien_boss_collision(sw_settings, screen, bullets, aliens_bosses, game_stats, scoreboard, ship, aliens, aliens_bullets, asteroids, alien_boss_bullets, capsules_shield, capsules_speed, capsules_bullet)
			check_alien_boss_bullet_ship_bullet_collision(sw_settings, game_stats, scoreboard, screen, ship, aliens, bullets, aliens_bullets, asteroids, alien_boss_bullets, aliens_bosses)
			
def check_alien_boss_fires(sw_settings, screen, aliens_bosses, alien_boss_bullets, game_stats, aliens):
	alien_boss_fires = random.randint(0, 300)
	if game_stats.level == sw_settings.level_boss:
		if len(aliens) == 0:
			if alien_boss_fires < 2:
				fire_alien_boss_bullet(sw_settings, screen, aliens_bosses, alien_boss_bullets, game_stats, aliens)
			
def fire_alien_boss_bullet(sw_settings, screen, aliens_bosses, alien_boss_bullets, game_stats, aliens):
	for alien_boss in aliens_bosses:
		bullet_boss_colors = [None, (100, 50, 100), (215, 215, 0), (0, 100, 0), (128, 128, 128)]
		alien_boss_bullet = AlienBossBullet(sw_settings, screen, alien_boss, bullet_boss_colors[game_stats.level // 5])
		alien_boss_bullets.add(alien_boss_bullet)
		
def update_alien_boss_bullet(sw_settings, game_stats, scoreboard, screen, ship, aliens, bullets, aliens_bullets, asteroids, alien_boss_bullets, aliens_bosses, capsules_shield, capsules_speed, capsules_bullet):
	alien_boss_bullets.update()
	screen_rect = screen.get_rect()
	for alien_boss_bullet in alien_boss_bullets.copy():
		if alien_boss_bullet.rect.top == screen_rect.bottom:
			alien_boss_bullets.remove(alien_boss_bullet)
	check_alien_boss_bullet_ship_collision(sw_settings, game_stats, scoreboard, screen, ship, aliens, bullets, aliens_bullets, asteroids, alien_boss_bullets, aliens_bosses, capsules_shield, capsules_speed, capsules_bullet)
	check_alien_boss_bullet_ship_bullet_collision(sw_settings, game_stats, scoreboard, screen, ship, aliens, bullets, aliens_bullets, asteroids, alien_boss_bullets, aliens_bosses)
	
def check_alien_boss_bullet_ship_collision(sw_settings, game_stats, scoreboard, screen, ship, aliens, bullets, aliens_bullets, asteroids, alien_boss_bullets, aliens_bosses, capsules_shield, capsules_speed, capsules_bullet):
	if pygame.sprite.spritecollideany(ship, alien_boss_bullets):
		ship_hit(sw_settings, game_stats, scoreboard, screen, ship, aliens, bullets, aliens_bullets, asteroids, alien_boss_bullets, aliens_bosses, capsules_shield, capsules_speed, capsules_bullet)

def check_alien_boss_bullet_ship_bullet_collision(sw_settings, game_stats, scoreboard, screen, ship, aliens, bullets, aliens_bullets, asteroids, alien_boss_bullets, aliens_bosses):
	ship_bullets_alien_boss_bullets_collisions = pygame.sprite.groupcollide(alien_boss_bullets, bullets, True, True)

def check_alien_fires(sw_settings, screen, aliens, aliens_bullets):
	aliens_fires = random.randint(0, 400)
	if len(aliens) != 0:
		if aliens_fires < 2:
			fire_alien_bullet(sw_settings, screen, aliens, aliens_bullets)
	
def fire_alien_bullet(sw_settings, screen, aliens, aliens_bullets):
	alien_y_values = [alien.rect.y for alien in aliens.sprites()]
	max_alien_y = max(alien_y_values)
	bottom_aliens = []
	for alien in aliens.sprites():
		if alien.rect.y == max_alien_y:
			bottom_aliens.append(alien)
	for alien in bottom_aliens:
		new_alien_bullet = AlienBullet(sw_settings, screen, alien)
		aliens_bullets.add(new_alien_bullet)
	
def update_aliens_bullets(sw_settings, game_stats, scoreboard, screen, ship, aliens, bullets, aliens_bullets, asteroids, alien_boss_bullets, aliens_bosses, capsules_shield, capsules_speed, capsules_bullet):
	aliens_bullets.update()
	screen_rect = screen.get_rect()
	for alien_bullet in aliens_bullets.copy():
		if alien_bullet.rect.top == screen_rect.bottom:
			aliens_bullets.remove(alien_bullet)
	check_bullet_ship_collisions(sw_settings, game_stats, scoreboard, screen, ship, aliens, bullets, aliens_bullets, asteroids, alien_boss_bullets, aliens_bosses, capsules_shield, capsules_speed, capsules_bullet)
	check_bullets_bullets_collision(sw_settings, screen, bullets, aliens_bullets)
	
def check_bullet_ship_collisions(sw_settings, game_stats, scoreboard, screen, ship, aliens, bullets, aliens_bullets, asteroids, alien_boss_bullets, aliens_bosses, capsules_shield, capsules_speed, capsules_bullet):
	if ship.shield == False:
		if pygame.sprite.spritecollideany(ship, aliens_bullets):
			ship_hit(sw_settings, game_stats, scoreboard, screen, ship, aliens, bullets, aliens_bullets, asteroids, alien_boss_bullets, aliens_bosses, capsules_shield, capsules_speed, capsules_bullet)
	else:
		pygame.sprite.spritecollide(ship, aliens_bullets, True)
		
def check_bullets_bullets_collision(sw_settings, screen, bullets, aliens_bullets):
	bullets_bullets_collision = pygame.sprite.groupcollide(bullets, aliens_bullets, True, True)
	
def check_bullets_alien_boss_collision(sw_settings, screen, bullets, aliens_bosses, game_stats, scoreboard, ship, aliens, aliens_bullets, asteroids, alien_boss_bullets, capsules_shield, capsules_speed, capsules_bullet):
	bullets_alien_boss_collisions = pygame.sprite.groupcollide(aliens_bosses, bullets, False, True)
	if bullets_alien_boss_collisions:
		for alien_boss in aliens_bosses:
			alien_boss.boss_hit += 1
			if alien_boss.boss_hit == sw_settings.end_live_boss:
				bullets_alien_boss_collisions = pygame.sprite.groupcollide(aliens_bosses, bullets, True, True)
				if game_stats.level == 20:
					end_game(sw_settings, screen, bullets, aliens_bosses, game_stats, scoreboard, ship, aliens, aliens_bullets, asteroids, alien_boss_bullets, capsules_shield, capsules_speed, capsules_bullet)
				else:
					start_new_boss_level(sw_settings, screen, bullets, aliens_bosses, game_stats, scoreboard, ship, aliens, aliens_bullets, asteroids, alien_boss_bullets, capsules_shield, capsules_speed, capsules_bullet)
					
def end_game(sw_settings, screen, bullets, aliens_bosses, game_stats, scoreboard, ship, aliens, aliens_bullets, asteroids, alien_boss_bullets, capsules_shield, capsules_speed, capsules_bullet):
	aliens_bosses.empty()
	bullets.empty()
	alien_boss_bullets.empty()
	capsules_shield.empty()
	capsules_speed.empty()
	capsules_bullet.empty()
	game_stats.game_active = False
	pygame.mouse.set_visible(True)
	pygame.mixer.music.set_volume(0.5)
	
def start_new_boss_level(sw_settings, screen, bullets, aliens_bosses, game_stats, scoreboard, ship, aliens, aliens_bullets, asteroids, alien_boss_bullets, capsules_shield, capsules_speed, capsules_bullet):
	sleep(0.5)
	start_new_level(sw_settings, screen, game_stats, scoreboard, ship, aliens, bullets, aliens_bullets, asteroids, aliens_bosses, alien_boss_bullets, capsules_shield, capsules_speed, capsules_bullet)	
	aliens_bosses.empty()
	sw_settings.increase_boss_speed()
	sw_settings.level_boss += 5
	sw_settings.end_live_boss += 15
								
def check_bullet_alien_collisions(sw_settings, screen, game_stats, scoreboard, ship, aliens, bullets, aliens_bullets, asteroids, aliens_bosses, alien_boss_bullets, capsules_shield, capsules_speed, capsules_bullet):
	colisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if colisions:
		for aliens in colisions.values():
			game_stats.score += sw_settings.alien_points * len(aliens)
		scoreboard.prep_score()
		check_high_score(game_stats, scoreboard)
	if game_stats.level != sw_settings.level_boss:
		if len(aliens) == 0:
			start_new_level(sw_settings, screen, game_stats, scoreboard, ship, aliens, bullets, aliens_bullets, asteroids, aliens_bosses, alien_boss_bullets, capsules_shield, capsules_speed, capsules_bullet)
		
def start_new_level(sw_settings, screen, game_stats, scoreboard, ship, aliens, bullets, aliens_bullets, asteroids, aliens_bosses, alien_boss_bullets, capsules_shield, capsules_speed, capsules_bullet):
	bullets.empty()
	aliens_bullets.empty()
	asteroids.empty()
	alien_boss_bullets.empty()
	capsules_shield.empty()
	capsules_speed.empty()
	capsules_bullet.empty()
	sw_settings.increase_speed()
	game_stats.level += 1
	
	if game_stats.level == sw_settings.level_boss:
		if len(aliens) == 0:
			create_alien_boss(sw_settings, screen, aliens_bosses, game_stats)
		
	scoreboard.prep_level()
	create_fleet(sw_settings, screen, ship, aliens)
	sleep(0.5)
			
def create_alien_boss(sw_settings, screen, aliens_bosses, game_stats):
	image_list = [None, "images/first_boss.png", "images/second_boss.png", "images/third_boss.png", "images/fourth_boss.png"]
	alien_boss = AlienBoss(sw_settings, screen, game_stats, image_list[game_stats.level // 5])
	aliens_bosses.add(alien_boss)
	
def update_alien_boss(sw_settings, screen, game_stats, aliens_bosses, aliens, aliens_bullets, bullets, asteroids):
	if game_stats.level == sw_settings.level_boss:
		if len(aliens) == 0:
			check_alien_boss_edges(sw_settings, aliens_bosses)
			for alien_boss in aliens_bosses.sprites():
				alien_boss.update()
	
def check_alien_boss_edges(sw_settings, aliens_bosses):
	for alien_boss in aliens_bosses.sprites():
		if alien_boss.alien_boss_check_edges():
			change_alien_boss_direction(sw_settings, aliens_bosses)
		
def change_alien_boss_direction(sw_settings, aliens_bosses):
	for alien_boss in aliens_bosses.sprites():
		alien_boss.rect.y += sw_settings.alien_boss_drop_speed
	sw_settings.alien_boss_direction *= -1
	
def check_high_score(game_stats, scoreboard):
	if game_stats.score > game_stats.high_score:
		game_stats.high_score = game_stats.score
		scoreboard.prep_high_score()

def get_number_aliens_x(sw_settings, alien_width):
	avialable_space_x = sw_settings.screen_width - 2 * alien_width
	number_aliens_x = int(avialable_space_x / (2 * alien_width))
	return number_aliens_x
	
def get_number_rows(sw_settings, ship_height, alien_height):
	avialable_space_y = (sw_settings.screen_height - (2 * alien_height) - ship_height)
	number_rows = int(avialable_space_y / (2 * alien_height))
	return number_rows
	
def create_alien(sw_settings, screen, aliens, alien_number, row_number):
	alien = Alien(sw_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)
	
def create_fleet(sw_settings, screen, ship, aliens):
	alien = Alien(sw_settings, screen)
	number_aliens_x = get_number_aliens_x(sw_settings, alien.rect.width)
	number_rows = get_number_rows(sw_settings, ship.rect.height, alien.rect.height)
	
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(sw_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(sw_settings, aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(sw_settings, aliens)
			break
			
def change_fleet_direction(sw_settings, aliens):
	for alien in aliens.sprites():
		alien.rect.y += sw_settings.fleet_drop_speed
	sw_settings.fleet_direction *= -1
	
def ship_hit(sw_settings, game_stats, scoreboard, screen, ship, aliens, bullets, aliens_bullets, asteroids, alien_boss_bullets, aliens_bosses, capsules_shield, capsules_speed, capsules_bullet):
	if game_stats.ships_left > 0:
		game_stats.ships_left -= 1
		scoreboard.prep_ships()
		aliens.empty()
		bullets.empty()
		aliens_bullets.empty()
		asteroids.empty()
		aliens_bosses.empty()
		alien_boss_bullets.empty()
		capsules_shield.empty()
		capsules_speed.empty()
		capsules_bullet.empty()
	
		create_fleet(sw_settings, screen, ship, aliens)
		
		if game_stats.level == sw_settings.level_boss:
			create_alien_boss(sw_settings, screen, aliens_bosses)
				
		ship.center_ship()
	
		sleep(1)
	else:
		game_stats.game_active = False
		pygame.mouse.set_visible(True)
		pygame.mixer.music.set_volume(0.5)
	
def check_aliens_bottom(sw_settings, game_stats, scoreboard, screen, ship, aliens, aliens_bullets, bullets, asteroids, alien_boss_bullets, aliens_bosses, capsules_shield, capsules_speed, capsules_bullet):
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(sw_settings, game_stats, scoreboard, screen, ship, aliens, bullets, aliens_bullets, asteroids, alien_boss_bullets, aliens_bosses, capsules_shield, capsules_speed, capsules_bullet)
			break
			
def update_aliens(sw_settings, game_stats, scoreboard, screen, ship, aliens, bullets, aliens_bullets, asteroids, alien_boss_bullets, aliens_bosses, capsules_shield, capsules_speed, capsules_bullet):
	check_fleet_edges(sw_settings, aliens)
	aliens.update()
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(sw_settings, game_stats, scoreboard, screen, ship, aliens, bullets, aliens_bullets, asteroids, alien_boss_bullets, aliens_bosses, capsules_shield, capsules_speed, capsules_bullet)
	check_aliens_bottom(sw_settings, game_stats, scoreboard, screen, ship, aliens, aliens_bullets, bullets, asteroids, alien_boss_bullets, aliens_bosses, capsules_shield, capsules_speed, capsules_bullet)
	
def update_screen(sw_settings, screen, earth, moon, sun, game_stats, scoreboard, ship, aliens, bullets, aliens_bullets, asteroids, capsules_shield, capsules_bullet, capsules_speed, play_button, pause_message, win_message, lose_message, aliens_bosses, alien_boss_bullets):
	screen.fill(sw_settings.bg_color)
	earth.show_earth()
	moon.show_moon()
	sun.show_sun()
	for alien_bullet in aliens_bullets.sprites():
		alien_bullet.draw_alien_bullet()
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	for alien_boss_bullet in alien_boss_bullets:
		alien_boss_bullet.draw_alien_boss_bullet()
	ship.blitme()
	aliens.draw(screen)
	for asteroid in asteroids.sprites():
		asteroid.blitme()
	for capsule_s in capsules_shield.sprites():
		capsule_s.blitme()
	for capsule_b in capsules_bullet.sprites():
		capsule_b.blitme()
	for capsule_c in capsules_speed.sprites():
		capsule_c.blitme()
	if len(aliens) == 0:
		for alien_boss in aliens_bosses.sprites():
			alien_boss.blitme()
	scoreboard.show_score()
	if not game_stats.game_active:
		play_button.draw_button()
		if game_stats.level == 20:
			if len(aliens_bosses) == 0:
				win_message.draw_win_message()
		if game_stats.ships_left == 0:
			lose_message.draw_lose_message()
	if not game_stats.game_pause:
		pause_message.draw_pause_message()
	
	pygame.display.flip()
