from random import randint

from src.Actor import Actor


class Human(Actor):
    def __init__(self, n_actor_count: int):
        Actor.__init__(self, n_actor_count)
        self.name += "_Human"
        self.human_pride = randint(1, 50)
        self.image_path = 'images/human.png'

    def to_string(self):
        return Actor.to_string(
            self) + "\nHuman Pride : " + str(self.human_pride)

    def fight(self, enemy) -> int:
        damage = 0
        if enemy.location == self.location:
            if enemy.strength > self.strength or enemy.health_points > self.health_points:
                damage = (self.strength + self.human_pride)
            else:
                damage = Actor.fight(self, enemy)
        return damage
