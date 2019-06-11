from src.Hobbit import Hobbit
from src.Orc import Orc


def test_to_string():
    hobbit = Hobbit(0)
    assert hobbit.to_string().__contains__("Stealth : ")


def test_move_actor():
    hobbit = Hobbit(0)
    hobbit.fear = 50
    hobbit.strength = 30
    hobbit.dependence = 51
    enemy = Orc(1)
    enemy.health_points = 70
    enemy.strength = 40
    hobbit.location[0] = 40  #
    hobbit.location[1] = 40  #
    enemy.location[0] = 10  #
    enemy.location[1] = 50  #
    hobbit.speed = 10
    hobbit.runs = hobbit.max_runs()
    hobbit.move_actor(enemy)
    assert hobbit.location[0] == 30  # 40 - 10 = 30
    assert hobbit.location[1] == 50  # 40 + 10 = 50
    hobbit.runs = 0
    hobbit.location[0] = 20
    hobbit.location[1] = 20
    hobbit.move_actor(enemy)
    assert hobbit.location[0] == 30  # 20 + 10 = 30 because of running away
    assert hobbit.location[1] == 10  # 20 - 10 = 10 because of running away


def test_take_damage():
    hobbit = Hobbit(0)
    hobbit.fear = 50
    hobbit.health_points = 100
    hobbit.take_damage(40)
    assert hobbit.health_points == hobbit.unit_max()
    hobbit.take_damage(60)
    assert hobbit.health_points == 40
