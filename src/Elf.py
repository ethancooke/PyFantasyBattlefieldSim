from random import randint

from src.Actor import Actor


class Elf(Actor):

    def __init__(self, n_actor_count: int):
        Actor.__init__(self, n_actor_count)
        self.name += "_Elf"
        self.bow_strength = randint(1, 100)
        self.magic = randint(1, 100)
        self.range = randint(1, 100)

    def to_string(self) -> str:
        return Actor.to_string(
            self) + "\nBow Strength : " + str(self.bow_strength) + "\nMagic : " + str(
            self.magic) + "\nRange : " + str(self.range)

    def fight(self, enemy) -> int:
        damage = Actor.fight_from_distance(self, enemy, self.range, self.magic)
        return damage
