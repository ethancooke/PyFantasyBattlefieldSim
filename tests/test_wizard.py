from src.Wizard import Wizard
from src.Orc import Orc


def test_to_string():
    wizard = Wizard(5)
    assert wizard.to_string().__contains__("Intelligence : ")


def test_fight():
    wizard = Wizard(0)
    wizard.intelligence = 10
    wizard.magic = 50
    wizard.location[0] = 1
    wizard.location[1] = 1
    enemy = Orc(0)
    enemy.location[0] = 10
    enemy.location[1] = 1
    assert wizard.fight(enemy) == 50
    enemy.location[0] = 99
    enemy.location[1] = 99
    assert wizard.fight(enemy) == 0
