from src.Army import Army
import time
import pygame


class Simulator:
    def __init__(self):
        self.dark_army = Army("Dark", 1000)
        self.light_army = Army("Light", 1000)
        self.victory = False
        self.victor = ""
        self.count = 0
        self.tick_rate = 60
        self.screen_title = 'Python Fantasy Battlefield Simulator'
        self.width = 1000
        self.height = 1000
        self.game_screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(self.screen_title)

    def run_simulation(self):
        start = time.time()
        self.count = 0
        self.victory = False
        self.victor = ""
        if self.get_light_army_size() > 0 and self.get_dark_army_size() > 0:
            while self.victory is False:
                self.count += 1
                self.game_screen.fill((0, 0, 0))
                self.draw_image(self.light_army, self.dark_army)
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

                pygame.display.update()
                self.clock.tick(self.tick_rate)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.victory = True
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

    def draw_image(self, light, dark):

        for index in range(light.get_size()):
            self.game_screen.blit(light.unit[index].playerImage(),
                                  (light.unit[index].location[0], light.unit[index].location[1]))
        for index in range(dark.get_size()):
            self.game_screen.blit(dark.unit[index].playerImage(),
                                  (dark.unit[index].location[0], dark.unit[index].location[1]))


def main():
    pygame.init()
    sim = Simulator()
    sim.run_simulation()
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
