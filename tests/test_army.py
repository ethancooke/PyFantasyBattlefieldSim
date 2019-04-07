from src.Army import Army
from src.Orc import Orc


def test_army_unit_type():
    army = Army("Dark", 100)
    type(army.unit[0])
    assert type(army.unit[0]) == Orc
    army = Army("Light", 100)
    type(army.unit[0])
    assert type(army.unit[0]) != Orc


def test_army_generation_size():
    army = Army("Dark", 100)
    assert army.get_size() == 100
    assert type(army.unit[0]) == Orc
    army.generate_army("Light", 250)
    assert army.get_size() == 250
    assert type(army.unit[0]) != Orc


def test_army_to_string():
    army = Army("Dark", 100)
    assert army.to_string().__contains__(army.unit[0].to_string()) and army.to_string().__contains__(
        army.unit[99].to_string())


def test_get_random_actor():
    army = Army("Dark", 100)
    assert type(army.get_random_actor()) == Orc


def test_find_nearest_actor():
    army = Army("Dark", 1)
    enemy = Army("Light", 1)
    assert army.find_nearest_actor(enemy.unit[0]) == army.unit[0]


def test_kill_actor():
    army = Army("Dark", 2)
    army.kill_actor(1)
    assert army.get_size() == 1


def test_check_if_destroyed():
    army = Army("Dark", 1)
    assert army.check_if_destroyed() is False
    army.kill_actor(0)
    assert army.check_if_destroyed() is True


def test_get_size():
    army = Army("Dark", 123)
    assert army.get_size() == 123 and army.get_size() == len(army.unit)
