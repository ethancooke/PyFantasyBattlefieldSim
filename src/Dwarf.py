from random import randint

from src.Actor import Actor


class Dwarf(Actor):
    def __init__(self, n_actor_count: int):
        Actor.__init__(self, n_actor_count)
        self.name += "_Dwarf"
        self.armor = randint(1, 50)
        self.axe_strength = randint(1, 50)
        self.image_path = 'images/dwarf.png'

    def to_string(self):
        return Actor.to_string(
            self) + "\nArmor : " + str(self.armor) + "\nAxe Strength : " + str(self.axe_strength)

    def fight(self, enemy) -> int:
        damage = 0
        if enemy.location == self.location:
            damage = self.strength + self.axe_strength
        return damage

    def take_damage(self, damage: int):
        if damage >= self.armor:
            Actor.take_damage(self, damage)
