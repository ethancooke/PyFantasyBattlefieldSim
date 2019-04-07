from src.Human import Human
from src.Orc import Orc


def test_to_string():
    human = Human(0)
    assert human.to_string().__contains__("Human Pride : ")


def test_fight():
    human = Human(0)
    human.location[0] = 1
    human.location[1] = 1
    human.strength = 50
    human.human_pride = 49
    human.health_points = 50
    enemy = Orc(0)
    enemy.health_points = 100
    enemy.strength = 5
    enemy.location[0] = 1
    enemy.location[1] = 1
    assert human.fight(enemy) == 99
    enemy.health_points = 5
    enemy.strength = 100
    assert human.fight(enemy) == 99
    enemy.health_points = 5
    enemy.strength = 5
    assert human.fight(enemy) == 50
