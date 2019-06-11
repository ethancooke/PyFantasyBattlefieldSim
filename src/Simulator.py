from src.Army import Army
import matplotlib.pyplot as plt
import time


class Simulator:
    def __init__(self):
        self.dark_army = Army("Dark", 1000)
        self.light_army = Army("Light", 1000)
        self.victory = False
        self.victor = ""
        self.count = 0

    def run_simulation(self):
        start = time.time()
        plt.ion
        self.count = 0
        self.victory = False
        self.victor = ""
        if self.get_light_army_size() > 0 and self.get_dark_army_size() > 0:
            while self.victory is False:
                self.count += 1
                self.draw_scatter('Turn: ' + str(self.count) + ' | Dark: ' + str(self.dark_army.get_size()) + ' | Light: ' +
                                  str(self.light_army.get_size()), self.display_scatter(
                                      self.dark_army), self.display_scatter(self.light_army))
                # Light Turn
                self.victory = self.turn(self.light_army, self.dark_army)
                if self.victory:
                    self.victor = "Light"
                    break
                # Dark Turn
                self.victory = self.turn(self.dark_army, self.light_army)
                if self.victory:
                    self.victor = "Darkness"
                    break
        else:
            self.victor = "Army has 0 units"
        print(time.time() - start)
        print(str(self.count))

    def get_dark_army_size(self) -> int:
        return self.dark_army.get_size()

    def get_light_army_size(self) -> int:
        return self.light_army.get_size()

    def get_victor(self) -> str:
        return self.victor

    def turn(self, attacker, defender):
        actor = attacker.get_random_actor()
        enemy = defender.find_nearest_actor(actor)
        actor.move_actor(enemy)
        enemy.take_damage(actor.fight(enemy))
        victory = defender.check_if_destroyed()
        return victory

    def display_scatter(self, army):
        x = []
        y = []
        for index in range(army.get_size()):
            x.append(army.unit[index].location[0])
        for index in range(army.get_size()):
            y.append(army.unit[index].location[1])
        return [x, y]

    def draw_scatter(self, title, dark, light):
        plt.cla()
        plt.title(title)
        plt.scatter(dark[0], dark[1], 10, c='r', marker='^', alpha=0.5)
        plt.scatter(light[0], light[1], 10, c='b', marker='s', alpha=0.5)
        plt.draw()
        plt.pause(0.000001)  # Screen doesn't appear without this pause


def main():
    sim = Simulator()
    sim.run_simulation()


if __name__ == '__main__':
    main()
