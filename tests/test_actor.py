from src.Actor import Actor


def test_actor_name():
    actor = Actor(5)
    assert actor.name == "Unit_5"


def test_actor_health_is_within_50_to_100():
    actor = Actor(0)
    assert 50 <= actor.health_points <= 100


def test_actor_strength_is_within_1_to_100():
    actor = Actor(0)
    assert 1 <= actor.strength <= 100


def test_actor_speed_is_within_1_to_100():
    actor = Actor(0)
    assert 1 <= actor.speed <= 100


def test_actor_location_xy_is_within_0_to_100():
    actor = Actor(0)
    assert 0 <= actor.location[0] <= 1000
    assert 0 <= actor.location[1] <= 1000


def test_to_string():
    actor = Actor(25)
    assert actor.to_string().__contains__("Name : Unit_25")


def test_get_distance_between_actors():
    actor0 = Actor(0)
    actor0.location[0] = 0
    actor0.location[1] = 2
    actor1 = Actor(1)
    actor1.location[0] = 10
    actor1.location[1] = 2
    assert actor0.get_distance_from(actor1) == 10


def test_keep_in():
    actor = Actor(0)
    actor.location[0] = -1
    actor.location[1] = 1001
    actor.keep_in()
    assert actor.location[0] == 0
    assert actor.location[1] == 1000
    actor.location[0] = 1001
    actor.location[1] = -1
    actor.keep_in()
    assert actor.location[0] == 1000
    assert actor.location[1] == 0
    actor.location[0] = 50
    actor.location[1] = 50
    actor.keep_in()
    assert actor.location[0] == 50
    assert actor.location[1] == 50


def test_move_actor():
    actor = Actor(0)
    enemy = Actor(1)
    actor.location[0] = 20
    actor.location[1] = 10
    enemy.location[0] = 10
    enemy.location[1] = 50
    actor.speed = 30
    actor.move_actor(enemy)
    assert actor.location[0] == 10  # 20 - 30 = -10 but enemy is at 10 so stop at 10
    assert actor.location[1] == 40  # 10 + 30 = 40
    actor.location[0] = 100
    actor.location[1] = 100
    actor.move_actor(enemy)
    assert actor.location[0] == 70
    assert actor.location[1] == 70


def test_fight():
    actor = Actor(0)
    actor.strength = 25
    enemy = Actor(1)
    enemy.health_points = 100
    actor.location[0] = 50
    actor.location[1] = 50
    enemy.location[0] = 50
    enemy.location[1] = 50
    assert actor.fight(enemy) == 25


def test_fight_from_distance():
    actor = Actor(0)
    enemy = Actor(1)
    enemy.health_points = 100
    actor.location[0] = 50
    actor.location[1] = 40
    enemy.location[0] = 50
    enemy.location[1] = 50
    weapon_range = 10
    weapon = 25
    assert actor.fight_from_distance(enemy, weapon_range, weapon) == 25
    weapon_range = 1
    assert actor.fight_from_distance(enemy, weapon_range, weapon) == 0


def test_take_damage():
    actor = Actor(0)
    actor.health_points = 50
    actor.take_damage(40)
    assert actor.health_points == 10
