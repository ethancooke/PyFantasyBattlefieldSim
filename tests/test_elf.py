from src.Elf import Elf
from src.Orc import Orc


def test_to_string():
    elf = Elf(5)
    assert elf.to_string().__contains__("Bow Strength : ")


def test_fight():
    elf = Elf(0)
    elf.range = 10
    elf.bow_strength = 50
    elf.location[0] = 1
    elf.location[1] = 1
    enemy = Orc(0)
    enemy.location[0] = 10
    enemy.location[1] = 1
    assert elf.fight(enemy) == 50
    enemy.location[0] = 99
    enemy.location[1] = 99
    assert elf.fight(enemy) == 0