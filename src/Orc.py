from random import randint

from src.Actor import Actor


class Orc(Actor):

    def __init__(self, n_actor_count: int):
        Actor.__init__(self, n_actor_count)
        self.name += "_Orc"
        self.anger = randint(1, 50)
        self.hunger = randint(1, 100)
        self.size = randint(1, 50)
        self.leadership = randint(1, 100)
        self.location = [randint(500, 1000), randint(0, 1000)]

    def fight(self, enemy) -> int:
        damage = 0
        if self.get_distance_from(enemy) == 0:
            damage = self.strength + self.anger
        return damage

    def to_string(self) -> str:
        return Actor.to_string(self) + "\nAnger : " + str(self.anger) + "\nHunger : " + str(
            self.hunger) + "\nSize : " + str(
            self.size) + "\nLeadership : " + str(self.leadership)

    def take_damage(self, damage):
        if damage >= self.size:
            Actor.take_damage(self, damage)
