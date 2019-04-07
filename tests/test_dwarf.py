from src.Dwarf import Dwarf
from src.Orc import Orc


def test_to_string():
    dwarf = Dwarf(0)
    assert dwarf.to_string().__contains__("Axe Strength : ")


def test_fight():
    dwarf = Dwarf(0)
    dwarf.location[0] = 1
    dwarf.location[1] = 1
    dwarf.strength = 50
    dwarf.axe_strength = 49
    enemy = Orc(0)
    enemy.location[0] = 1
    enemy.location[1] = 1
    assert dwarf.fight(enemy) == 99


def test_take_damage():
    dwarf = Dwarf(0)
    dwarf.health_points = 100
    dwarf.armor = 50
    dwarf.take_damage(10)
    assert dwarf.health_points == 100
    dwarf.take_damage(90) == 90
    assert dwarf.health_points == 10
