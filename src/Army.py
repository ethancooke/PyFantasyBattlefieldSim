from src.ActorFactory import ActorFactory
from random import randint


class Army:
    def __init__(self, s_army_name: str, n_size: int):
        self.unit = []
        self.s_army_name = s_army_name
        self.generate_army(s_army_name, n_size)

    def generate_army(self, s_army_type: str, n_size: int):
        self.unit.clear()
        if s_army_type == "Light":
            for unit in range(n_size):
                self.unit += [ActorFactory.create_new_actor(randint(0, 4), unit)]
        if s_army_type == "Dark":
            for unit in range(n_size):
                self.unit += [ActorFactory.create_new_actor(5, unit)]

    def to_string(self) -> str:
        army_string = ""
        for i in range(self.get_size()):
            army_string += self.unit[i].to_string()
        return army_string

    def get_random_actor(self):
        random_index = randint(1, self.get_size()) - 1
        return self.unit[random_index]

    def find_nearest_actor(self, actor):
        current_distance = 100
        new_distance = 0
        l_unit_number = 0
        for index in range(self.get_size()):
            new_distance = actor.get_distance_from(self.unit[index])
            if new_distance < current_distance and self.unit[index].health_points >= 0:
                l_unit_number = index
                current_distance = new_distance
        return self.unit[l_unit_number]

    def kill_actor(self, index):
        del self.unit[index]
        # print("Killed actor: " + str(index) + " of army " + self.s_army_name)

    def check_if_destroyed(self) -> bool:
        defeated = False
        for index in range(self.get_size()):
            if self.unit[index].health_points <= 0:
                self.kill_actor(index)
                break
        if self.get_size() == 0:
            defeated = True
            print("Force of " + self.s_army_name + " were destroyed!")
        return defeated

    def get_size(self):
        return len(self.unit)
