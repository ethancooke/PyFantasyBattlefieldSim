from src.Orc import Orc
from src.Human import Human


def test_to_string():
    orc = Orc(0)
    assert orc.to_string().__contains__("Anger : ")


def test_fight():
    orc = Orc(0)
    orc.location[0] = 1
    orc.location[1] = 1
    orc.anger = 49
    orc.strength = 50
    enemy = Human(0)
    enemy.location[0] = 1
    enemy.location[1] = 1
    assert orc.fight(enemy) == 99


def test_take_damage():
    orc = Orc(0)
    orc.size = 40
    orc.health_points = 90
    orc.take_damage(39)
    assert orc.health_points == 90
    orc.take_damage(50)
    assert orc.health_points == 40
