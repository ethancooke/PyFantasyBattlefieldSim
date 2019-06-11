from random import randint

from src.Actor import Actor


class Hobbit(Actor):
    def __init__(self, n_actor_count: int):
        Actor.__init__(self, n_actor_count)
        self.name += "_Hobbit"
        self.stealth = randint(1, self.unit_max())
        self.has_dagger = False
        self.dependence = randint(1, self.unit_max())
        self.fear = randint(1, self.unit_max())
        self.runs = 0

    def to_string(self) -> str:
        return Actor.to_string(
            self) + "\nStealth : " + str(self.stealth) + "\nHas Dagger : " + str(
            self.has_dagger) + "\nDependence : " + str(self.dependence) + "\nFear : " + str(self.fear)

    def move_actor(self, enemy):
        if self.runs >= self.max_runs():  # Limit how often a hobbit can run away
            self.runs = 0
            Actor.move_actor(self, enemy)
        elif self.fear > enemy.strength and self.strength < enemy.health_points and self.dependence > 50:
            # X Movement
            if enemy.location[0] > self.location[0]:
                self.location[0] = self.location[0] - self.speed
            elif enemy.location[0] < self.location[0]:
                self.location[0] = self.location[0] + self.speed
            # Y Movement
            if enemy.location[1] > self.location[1]:
                self.location[1] = self.location[1] - self.speed
            elif enemy.location[1] < self.location[1]:
                self.location[1] = self.location[1] + self.speed
            self.runs += 1
        else:
            Actor.move_actor(self, enemy)
        # Actor.keep_in(self)
        # If a hobbit runs out off the battlefield they are considered dead to us
        self.seppuku()
        enemy.take_damage(Actor.fight(self, enemy))

    def take_damage(self, damage: int):
        if damage >= self.fear:
            Actor.take_damage(self, damage)

    def seppuku(self):
        if self.location[0] > self.battlefield_max():
            Actor.take_damage(self, self.unit_max())
        elif self.location[0] < 0:
            Actor.take_damage(self, self.unit_max())
        if self.location[1] > self.battlefield_max():
            Actor.take_damage(self, self.unit_max())
        elif self.location[1] < 0:
            Actor.take_damage(self, self.unit_max())

    @staticmethod
    def max_runs():
        return 2
