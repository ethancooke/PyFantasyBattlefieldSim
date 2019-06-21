from random import randint

from src.Actor import Actor


class Elf(Actor):

    def __init__(self, n_actor_count: int):
        Actor.__init__(self, n_actor_count)
        self.name += "_Elf"
        self.bow_strength = randint(15, self.unit_max())
        self.range = randint(10, self.unit_max())
        self.image_path = 'images/elf.png'

    def to_string(self) -> str:
        return Actor.to_string(
            self) + "\nBow Strength : " + str(self.bow_strength) + "\nMagic : " + "\nRange : " + str(self.range)

    def fight(self, enemy) -> int:
        damage = Actor.fight_from_distance(
            self, enemy, self.range, self.bow_strength)
        return damage
