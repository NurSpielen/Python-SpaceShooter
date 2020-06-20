
from gameobject import GameObject

class Bullet(GameObject):

    def __init__(self, x, y, speed, width, height, ID):
        super().__init__(x, y, speed, width, height, ID)
        self.move_up = True

    # Verifies if the bullet has hit an enemy and removes both from the game if true
    @staticmethod
    def verify_bullet_hit():
        for bullet in Player.bullets:  # Loops through all the bullets
            for enemy in Enemy.enemies:  # Loops through all the enemise
                # Verifies if the bullet is inside the enemy
                if bullet.x + bullet.width >= enemy.x and bullet.x <= enemy.x + enemy.width:
                    if bullet.y <= enemy.y + enemy.height and bullet.y >= enemy.y:
                        # Removes both the enemy and the bullet
                        Bullet.remove_bullet(bullet)
                        Enemy.remove_enemy(enemy)

    # Removes the bullets that have left the gameplay area
    @staticmethod
    def remove_out_of_gameplay_bullets():
        for bullet in Player.bullets:
            if bullet.y < 0 - bullet.height:  # Bullet has left the screen
                Bullet.remove_bullet(bullet)

    # Removes the selected bullet from the game
    @staticmethod
    def remove_bullet(bullet):
        Player.bullets.remove(bullet)
        GameObject.objects.remove(bullet)
