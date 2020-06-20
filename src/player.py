
from gameobject import GameObject


class Player(GameObject):
    # Keeps track of the amount of bullets in the game
    bullets = []

    def __init__(self, x, y, speed, width, height, ID):
        super().__init__(x, y, speed, width, height, ID)

    def shoot(self):
        bullet_speed = 300
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
