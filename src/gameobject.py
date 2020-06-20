
import pygame

from colors import Color


# Base class for everything in the game
class GameObject():
	# Keeps track of all of the game objects
	objects = []

	def __init__(self, x: int, y: int, speed: int, width: int, height: int, ID: str):
		self.width = width
		self.height = height
		self.x = x
		self.y = y
		self.speed = speed
		self.ID = ID
		self.color = self.set_color()  # Initializes object color
		self.move_left = False
		self.move_right = False
		self.move_up = False
		self.move_down = False
		self.objects.append(self)  # Appends instance to the objects list

	def set_color(self):
		if self.ID == "Player":
			return Color.GREEN.value
		elif self.ID == "Enemy":
			return Color.RED.value
		elif self.ID == "Bullet":
			return Color.YELLOW.value
		else:
			return Color.BLUE.value

	def update(self, dt: float, WIDTH: int, HEIGHT: int):
		if self.move_left:
			self.x -= self.speed * dt
		if self.move_right:
			self.x += self.speed * dt
		if self.move_up:
			self.y -= self.speed * dt
		if self.move_down:
			self.y += self.speed * dt

		# If the object is the player it will not allow it to go outside of the screen
		if self.ID == "Player":
			self.x = GameObject.clamp(self.x, 0, WIDTH - self.width)
			self.y = GameObject.clamp(self.y, 0, HEIGHT - self.height)

	def render(self, WINDOW):
		pygame.draw.rect(WINDOW, self.color, [int(self.x), int(self.y), self.width, self.height])

	@staticmethod
	# Prevents an object from moving past a certain point in the screen
	def clamp(pos: float, min_val: float, max_val: float) -> float:
		if pos < min_val:
			return min_val
		elif pos > max_val:
			return max_val
		else:
			return pos
