
import pygame

# Base class for everything in the game
class GameObject():

	# Keeps track of all of the game objects
	objects = []

	def __init__(self, x, y, speed, width, height, ID):
		self.width = width
		self.height = height
		self.x = x
		self.y = y
		self.speed = speed
		self.ID = ID
		self.color = self.set_color() # Initializes object color
		self.move_left = False
		self.move_right = False
		self.move_up = False
		self.move_down = False
		self.objects.append(self) # Appends instance to the objects list

	def set_color(self):
		if self.ID == "Player":
			return GREEN
		elif self.ID == "Enemy":
			return RED
		elif self.ID == "Bullet":
			return YELLOW
		else:
			return BLUE

	def update(self):
		if self.move_left:
			self.x -= self.speed
		if self.move_right:
			self.x += self.speed
		if self.move_up:
			self.y -= self.speed
		if self.move_down:
			self.y += self.speed

		# If the object is the player it will not allow it to go outside of the screen
		if self.ID == "Player":
			self.x = GameLogic.clamp(self.x, 0, WIDTH - self.width)
			self.y = GameLogic.clamp(self.y, 0, HEIGHT - self.height)

	def render(self):
		pygame.draw.rect(WINDOW, self.color, [int(self.x), int(self.y), self.width, self.height])