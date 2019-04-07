from src.Hobbit import Hobbit
from src.Wizard import Wizard
from src.Elf import Elf
from src.Human import Human
from src.Dwarf import Dwarf
from src.Orc import Orc


class ActorFactory:

    @staticmethod
    def create_new_actor(n_actor_type: int, unit_number: int):
        return {
            0: Hobbit(unit_number),
            1: Wizard(unit_number),
            2: Elf(unit_number),
            3: Human(unit_number),
            4: Dwarf(unit_number),
            5: Orc(unit_number)
        }.get(n_actor_type, None)
