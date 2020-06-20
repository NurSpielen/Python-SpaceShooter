import pygame
import random
import math

from colors import Color
from gameobject import GameObject
from player import Player
from enemy import Enemy
from bullet import Bullet

pygame.init()

WIDTH = 800
HEIGHT = 600

# Initializing Window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# TODO Reformat everything after this
class EnemySpawner():
    # Handles everything related to spawning enemies
    # Might implement other functionality later on

    # TODO have enemies spawn based on a timer
    def __init__(self, clock):
        self.level = 0
        self.clock = clock

    def spawn_enemies(self):
        self.level += 1
        enemy_amount = 2 + math.ceil(self.level * 1.5)
        enemy_width = 80
        beginning = 0
        print(enemy_amount)
        for i in range(0, enemy_amount):
            init_x = random.randint(beginning, beginning + 300)
            beginning = init_x + (enemy_width * 2)
            Enemy(-init_x, 0, 400, enemy_width, 30, "Enemy")


# Handles all game logic, there is no need to create instances of this class
class GameLogic:

    @staticmethod
    def key_down(event, player: Player) -> None:
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
    def key_up(event, player: Player) -> None:
        if event.key == pygame.K_a:
            player.move_left = False
        if event.key == pygame.K_d:
            player.move_right = False
        if event.key == pygame.K_w:
            player.move_up = False
        if event.key == pygame.K_s:
            player.move_down = False

    @staticmethod
    def update(spawner, dt) -> None:
        # DEBUG
        if len(Enemy.enemies) == 0:
            spawner.spawn_enemies()

        for game_object in GameObject.objects:
            game_object.update(dt, WIDTH, HEIGHT)

        Bullet.remove_out_of_gameplay_bullets()
        Enemy.remove_out_of_gameplay_enemies()
        Bullet.verify_bullet_hit()

    @staticmethod
    def render() -> None:
        WINDOW.fill(Color.BLACK.value)  # Clears the screen
        for game_object in GameObject.objects:
            game_object.render(WINDOW)

    @staticmethod
    def event_handler(player: Player) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                GameLogic.key_down(event, player)
            if event.type == pygame.KEYUP:
                GameLogic.key_up(event, player)

        return True


def main():
    FPS = 60

    p_size = 30
    px = (WIDTH / 2) - (p_size / 2)
    py = HEIGHT - p_size

    player = Player(px, py, 400, p_size, p_size, "Player")
    clock = pygame.time.Clock()

    spawner = EnemySpawner(clock)

    run = True

    # Game Loop
    while run:
        dt = clock.tick(FPS) / 1000

        run = GameLogic.event_handler(player)
        GameLogic.update(spawner, dt)
        GameLogic.render()

        pygame.display.update()

    quit()


main()
