from random import randint

from src.Actor import Actor


class Wizard(Actor):
    def __init__(self, n_actor_count: int):
        Actor.__init__(self, n_actor_count)
        self.name += "_Wizard"
        self.magic = randint(1, 100)
        self.has_staff = True
        self.will = randint(1, 10)
        self.intelligence = randint(1, 100)

    def to_string(self):
        return Actor.to_string(
            self) + "\nHas Staff : " + str(self.has_staff) + "\nMagic : " + str(self.magic) + "\nWill : " + str(
            self.will) + "\nIntelligence : " + str(self.intelligence)

    def fight(self, enemy) -> int:
        damage = Actor.fight_from_distance(self, enemy, self.intelligence, self.magic)
        return damage
