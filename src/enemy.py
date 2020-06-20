
from gameobject import GameObject

# TODO Spawn enemies randomly
# TODO Have enemies pick a color randomly
# TODO Allow enemies to shoot
class Enemy(GameObject):
    # Keeps track of all the enemies in gameplay
    enemies = []

    def __init__(self, x, y, speed, width, height, ID):
        super().__init__(x, y, speed, width, height, ID)
        Enemy.enemies.append(self)
        self.can_move_down = False

    def update(self, dt):
        self.x += self.speed * dt

        # This is to prevent the enemy from switching direction when spawned
        if self.x > WIDTH and not self.can_move_down:
            self.can_move_down = True

        # Reverses movement direction and lowers enemy position
        if (self.x + self.width < 0 or self.x > WIDTH) and self.can_move_down:
            self.speed *= -1
            self.y += (self.height * 2)

    # Removes enemies that have left the gameplay area
    @staticmethod
    def remove_out_of_gameplay_enemies():
        for enemy in Enemy.enemies:
            if enemy.y >= (HEIGHT - (enemy.height * 2)):
                Enemy.remove_enemy(enemy)
            # DEBUG
            # print("Enemy removed")

    # Removes selected enemy from the game
    @staticmethod
    def remove_enemy(enemy):
        Enemy.enemies.remove(enemy)
        GameObject.objects.remove(enemy)
