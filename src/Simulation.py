from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton
import sys
from src.PyFantasyBattlefieldSimulator import Ui_simulationDialog
from src.Simulator import Simulator


class SimulationForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_simulationDialog()
        self.ui.setupUi(self)
        self.sim = Simulator()
        self.ui.armyOfLightSpinner.setValue(self.sim.get_light_army_size())
        self.ui.armyOfDarknessSpinner.setValue(self.sim.get_dark_army_size())
        self.ui.setArmySizeButton.clicked.connect(self.set_army_size)
        self.ui.runButton.clicked.connect(self.run_simulation)
        self.ui.quitButton.clicked.connect(self.quit_button)
        self.show()

    def disp_victor(self, victor):
        self.ui.victoryResultsLabel.setText(victor)

    def run_simulation(self):
        self.sim.run_simulation()
        self.ui.armyOfLightSpinner.setValue(self.sim.get_light_army_size())
        self.ui.armyOfDarknessSpinner.setValue(self.sim.get_dark_army_size())
        self.disp_victor(self.sim.get_victor())

    def quit_button(self):
        sys.exit(app.exec_())

    def set_army_size(self):
        self.sim.dark_army.generate_army("Dark", self.ui.armyOfDarknessSpinner.value())
        self.sim.light_army.generate_army("Light", self.ui.armyOfLightSpinner.value())


#if __name__ == "__main__":

app = QtWidgets.QApplication(sys.argv)
# simulationDialog = QtWidgets.QDialog()
ui = SimulationForm()
# ui.setupUi(simulationDialog)
ui.show()
sys.exit(app.exec_())
