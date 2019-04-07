from src.Simulator import Simulator


def test_simulator_has_armies():
    sim = Simulator()
    assert len(sim.dark_army.unit) > 0
    assert len(sim.light_army.unit) > 0


def test_simulator_turn():
    sim = Simulator()
    assert sim.turn(sim.dark_army, sim.light_army) is False


def test_simulator_run_simulation():
    sim = Simulator()
    sim.dark_army.generate_army("Dark", 5)
    sim.light_army.generate_army("Light", 5)
    sim.run_simulation()
    assert sim.victory is True
