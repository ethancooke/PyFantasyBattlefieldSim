from random import randint

from src.Actor import Actor


class Orc(Actor):

    def __init__(self, n_actor_count: int):
        Actor.__init__(self, n_actor_count)
        self.name += "_Orc"
        self.anger = randint(1, 50)
        self.size = randint(5, 50)
        self.location = [randint(500, self.battlefield_max()), randint(
            0, self.battlefield_max())]

    def fight(self, enemy) -> int:
        damage = 0
        if self.get_distance_from(enemy) == 0:
            damage = self.strength + self.anger
        return damage

    def to_string(self) -> str:
        return Actor.to_string(self) + "\nAnger : " + str(self.anger) + "\nSize : " + str(self.size)

    def take_damage(self, damage):
        if damage >= self.size:
            Actor.take_damage(self, damage)
