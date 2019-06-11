from random import randint
from math import sqrt


class Actor():
    def __init__(self, n_actor_count):
        self.name = "Unit_" + str(n_actor_count)
        # Start atleast at 50% of health
        self.health_points = randint(50, self.unit_max())
        self.strength = randint(15, self.unit_max())
        # On a scale of 1000x1000, movement of 1 takes too long
        self.speed = randint(50, self.unit_max())
        self.location = [randint(0, 500), randint(0, self.battlefield_max())]

    def to_string(self) -> str:
        return "Name : " + str(self.name) + "\nHealth Points : " + str(self.health_points) + "\nStrength : " + str(
            self.strength) + "\nSpeed : " + str(self.speed) + "\nLocation x,y : " + str(self.location)

    def get_distance_from(self, other_actor):
        ax = self.location[0]
        ay = self.location[1]
        ex = other_actor.location[0]
        ey = other_actor.location[1]
        a = ax - ex
        b = ay - ey
        c2 = (a ** 2) + (b ** 2)
        distance = sqrt(c2)
        return distance

    def keep_in(self):
        if self.location[0] > self.battlefield_max():
            self.location[0] = self.battlefield_max()
        elif self.location[0] < 0:
            self.location[0] = 0
        if self.location[1] > self.battlefield_max():
            self.location[1] = self.battlefield_max()
        elif self.location[1] < 0:
            self.location[1] = 0

    def move_actor(self, enemy):
        ax = self.location[0]
        ay = self.location[1]
        ex = enemy.location[0]
        ey = enemy.location[1]

        # X
        if ex > ax:
            if (ax + self.speed) > ex:
                ax = ex  # Don't run past the enemy
            else:
                ax += self.speed
        elif ex < ax:
            if (ax - self.speed) < ex:
                ax = ex  # Don't run past the enemy
            else:
                ax -= self.speed
        else:
            ax = ex
        # Y
        if ey > ay:
            if (ay + self.speed) > ey:
                ay = ey  # Don't run past the enemy
            else:
                ay += self.speed
        elif ey < ay:
            if (ay - self.speed) < ey:
                ay = ey  # Don't run past the enemy
            else:
                ay -= self.speed
        else:
            ay = ey
        self.location[0] = ax
        self.location[1] = ay
        self.keep_in()

    def fight(self, enemy) -> int:
        damage = 0
        if enemy.location == self.location:
            damage = self.strength
        return damage

    def fight_from_distance(self, enemy, weapon_range, weapon) -> int:
        ax = self.location[0]
        ay = self.location[1]
        ex = enemy.location[0]
        ey = enemy.location[1]
        # Enemy must me on the same x or y coordinate
        if ((ax <= ex <= (ax + weapon_range) and ay == ey) or (
                ax >= ex >= (ax - weapon_range) and ay == ey)
                or (ay <= ey <= (ay + weapon_range) and ax == ex) or (
                ay >= ey >= (ay - weapon_range) and ax == ex)):
            return weapon
        else:
            return 0
        # Should an actor be able to attack if the enemy is ontop of them?
        # Should I alter the damage based on the distance percentage? Example full range = half damage
        # Should an actor move if damage from a distance is possible?

    def take_damage(self, damage: int):
        if damage > 0:
            self.health_points -= damage

    @staticmethod
    def unit_max():
        return 100

    @staticmethod
    def battlefield_max():
        return 1000
