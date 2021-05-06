import pygame
from pygame.locals import*

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_height = 1000
screen_width = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Jump Back Home')

tile_size = 50
game_over = 0

bg_img = pygame.image.load('img/bg.png')
restart_img = pygame.image.load('img/restart.png')
	#adds the restart button 
class Button:
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.clicked = False

	def draw(self):
		#checks to see if the reset button has been pressed
		action = False

		pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True
		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False		


		screen.blit(self.image, self.rect)
		return action


#loads in the player
class Player ():
	def __init__(self,x,y):
		self.reset(x, y)


	def update(self, game_over):
		dx = 0
		dy = 0
		walk_cooldown = 10

		if game_over == 0:
			#Left,Right, Space key presses
			key = pygame.key.get_pressed()
			if key[pygame.K_SPACE]:
				self.vel_y = -10
				self.jump = True
			if key[pygame.K_SPACE] == True:
				self.jump = False
			if key [pygame.K_LEFT]:
				dx -= 5
				self.counter += 1
				self.direction = -1
			if key [pygame.K_RIGHT]:
				dx += 5
				self.counter += 1
				self.direction = 1
			if key [pygame.K_LEFT] == False and key [pygame.K_RIGHT] == False:
				self.counter = 0
				self.index = 0
				#stops the character from looking at one directions after key press
				if 	self.direction == 1:
					self.image = self.images_right[self.index]
				if 	self.direction == -1:
					self.image = self.images_left[self.index]

			#adding gravity
			self.vel_y += 1
			if self.vel_y > 50:
				self.vel_y = 50
			dy += self.vel_y
			#Animation
			
			if self.counter > walk_cooldown:
				self.counter = 0
				self.index += 1
			if self.index >= len(self.images_right):
				self.index = 0
			if 	self.direction == 1:
				self.image = self.images_right[self.index]
			if 	self.direction == -1:
				self.image = self.images_left[self.index]	

			
			
			# check for collision
			
			for tile in world.tile_list:
				#x direction
				if tile[1].colliderect(self.rect.x + dx,self.rect.y, self.width, self.height):
					dx = 0 
				#y direction	
				if tile[1].colliderect(self.rect.x,self.rect.y + dy, self.width, self.height):
					#check if beloe ground
					if self.vel_y < 0:
						dy = tile[1].bottom - self.rect.top
						self.vel_y = 0
					#check if above ground	
					elif self.vel_y >= 0:		
						dy = tile[1].top - self.rect.bottom	
						self.vel_y = 0
						

			#enemy collision
			if pygame.sprite.spritecollide(self, spider_group, False):
				game_over = -1

			#updates player location
			self.rect.x += dx
			self.rect.y += dy

		elif game_over == -1:
			
			self.image = self.dead_image

			if self.rect.y > 1600:
				self.rect.y -= 5
			#puts player on screen
		screen.blit(self.image, self.rect)
		return game_over
	def reset(self, x, y):
		self.images_right = []
		self.images_left = []
		self.index = 0
		self.counter = 0
		#walking images
		for num in range(1,5):
			img_right = pygame.image.load(f'img/hero{num}.png')
			img_right = pygame.transform.scale(img_right, (40, 80))
			img_left = pygame.transform.flip(img_right, True, False)
			self.images_right.append(img_right)
			self.images_left.append(img_left)
		self.dead_image = pygame.image.load('img/dead.png')
		self.image = self.images_right[self.index]	
		self.rect = self.image.get_rect() 
		self.rect.x = x
		self.rect.y = y
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.vel_y = 0
		self.jump = False
		self.direction = 0
	


#creates the world
class World():
	def __init__(self, data):
		self.tile_list = []
		grass_img = pygame.image.load('img/grass.png')

		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:
				if tile == 1:
					img = pygame.transform.scale(grass_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img , img_rect)
					self.tile_list.append(tile)
				if tile == 2:
					spider = Enemy(col_count * tile_size, row_count * tile_size + 25)
					spider_group.add(spider)
				col_count += 1 
			row_count += 1

	def draw(self):
		for tile in self.tile_list:
			screen.blit(tile[0], tile[1])
			pygame.draw.rect(screen,(255,255,255),tile[1],2)
	#creates the enemy in the game
class Enemy(pygame.sprite.Sprite):
	def __init__(self,x,y):

		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('img/spider.png')
		self.image = pygame.transform.scale(img,(tile_size,tile_size // 2 ) )
		self.rect= self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.move_direction = 1
		self.move_counter = 0
 		
		#movement of the enemy
	def update(self):
		self.rect.x += self.move_direction
		self.move_counter += 1
		if abs(self.move_counter) >50:
			self.move_direction *= -1
			self.move_counter *= -1

		
		

			#sets the tile for the world
world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], 
[1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 1], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

]

player = Player(100, screen_height - 130)

spider_group = pygame.sprite.Group()

world = World(world_data)
	#placement of button on the screen
restart_button = Button(screen_width // 2 - 50, screen_height // 2 + 100,restart_img)

run = True
while run:

	clock.tick(fps)

	screen.blit(bg_img, (0,0))

	world.draw()

	if game_over == 0:
		spider_group.update()

	spider_group.update()
	spider_group.draw(screen)

	game_over = player.update(game_over)
	#sets the player back in the original spot after hitting restart button
	if game_over == -1:
			if restart_button.draw():
				player.reset(100, screen_height - 130)
				game_over = 0
	#press the X in the game window
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()

