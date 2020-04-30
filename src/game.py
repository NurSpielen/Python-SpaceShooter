
import os
import pygame
import random
import time

pygame.init()

WIDTH = 800
HEIGHT = 600

# Initialiing Window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(("Space Shooter"))

# Creating Colors
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,186,0)
ORANGE = (255,120,0)
WHITE = (255,255,255)
BLACK = (0,0,0)

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
        pygame.draw.rect(WINDOW, self.color, [self.x, self.y, self.width, self.height])


class Player(GameObject):

    # Keeps track of the amount of bullets that the player shot
    bullets = []

    def __init__(self, x, y, speed, width, height, ID):
        super().__init__(x, y, speed, width, height, ID)

    def shoot(self):
        bullet_speed = 5
        side = 10
        bx = self.x + (self.width / 2) - (side / 2)
        by = self.y
        if len(self.bullets) < 2:
            self.bullets.append(Bullet(bx, by, bullet_speed, side, side, "Bullet"))

        # DEBUG
        '''
        print(f"Player bullets = { len(self.bullets) }")
        print(f"Game Objects = { len(GameObject.objects) }")
        '''


# TODO Spawn enemies randomly
# TODO Have enemies pick a color randomly
# TODO Allow enemies to shoot
class Enemy(GameObject):

    def __init__(self, x, y, speed, width, height, ID):
        super().__init__(x, y, speed, width, height, ID)
        self.move_down = True


class Bullet(GameObject):

    def __init__(self, x, y, speed, width, height, ID):
        super().__init__(x, y, speed, width, height, ID)
        self.move_up = True

    @staticmethod
    def remove_player_bullets():
        # Removes the player bullets from the game
        for bullet in Player.bullets:
            if bullet.y < 0 - bullet.height: # Bullet has left the screen
                Player.bullets.remove(bullet)
                GameObject.objects.remove(bullet)
    

# Handles all game logic, there is no need to create instances of this class
class GameLogic:

    @staticmethod
    def key_down(event, player):
        if event.key == pygame.K_a:
            player.move_left = True
        if event.key == pygame.K_d:
            player.move_right = True
        if event.key == pygame.K_w:
            player.move_up = True
        if event.key == pygame.K_s:
            player.move_down = True
        if event.key == pygame.K_SPACE:
            player.shoot()

    @staticmethod
    def key_up(event, player):
        if event.key == pygame.K_a:
            player.move_left = False
        if event.key == pygame.K_d:
            player.move_right = False
        if event.key == pygame.K_w:
            player.move_up = False
        if event.key == pygame.K_s:
            player.move_down = False

    @staticmethod
    def update():
        for game_object in GameObject.objects:
            game_object.update()

        Bullet.remove_player_bullets()
        
    @staticmethod
    def render():
        WINDOW.fill(BLACK) # Clears the screen
        for game_object in GameObject.objects:
            game_object.render()

    @staticmethod
    # Prevents an object for moving past a certain point in the screen
    def clamp(pos, min, max):
        if pos < min:
            return min
        elif pos > max:
            return max
        else:
            return pos


def main():

    FPS = 60

    p_size = 30
    px = (WIDTH / 2) - (p_size / 2)
    py = HEIGHT - p_size

    player = Player(px, py, 10, p_size, p_size, "Player")
    clock = pygame.time.Clock()

    run = True

    # Game Loop
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                GameLogic.key_down(event, player)
            if event.type == pygame.KEYUP:
                GameLogic.key_up(event, player)

        GameLogic.update()
        GameLogic.render()

        pygame.display.update()

    quit()
        
main()
