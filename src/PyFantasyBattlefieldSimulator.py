# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyFantasyBattlefieldSimulator.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_simulationDialog(object):
    def setupUi(self, simulationDialog):
        simulationDialog.setObjectName("simulationDialog")
        simulationDialog.resize(1280, 720)
        simulationDialog.setAccessibleName("")
        self.armyOfLightLabel = QtWidgets.QLabel(simulationDialog)
        self.armyOfLightLabel.setGeometry(QtCore.QRect(10, 680, 101, 22))
        self.armyOfLightLabel.setObjectName("armyOfLightLabel")
        self.armyOfDarknessLabel = QtWidgets.QLabel(simulationDialog)
        self.armyOfDarknessLabel.setGeometry(QtCore.QRect(250, 680, 131, 22))
        self.armyOfDarknessLabel.setObjectName("armyOfDarknessLabel")
        self.armyOfLightSpinner = QtWidgets.QSpinBox(simulationDialog)
        self.armyOfLightSpinner.setGeometry(QtCore.QRect(120, 670, 121, 36))
        self.armyOfLightSpinner.setMaximum(100000)
        self.armyOfLightSpinner.setObjectName("armyOfLightSpinner")
        self.armyOfDarknessSpinner = QtWidgets.QSpinBox(simulationDialog)
        self.armyOfDarknessSpinner.setGeometry(QtCore.QRect(390, 670, 121, 36))
        self.armyOfDarknessSpinner.setMaximum(100000)
        self.armyOfDarknessSpinner.setObjectName("armyOfDarknessSpinner")
        self.frame = QtWidgets.QFrame(simulationDialog)
        self.frame.setGeometry(QtCore.QRect(20, 30, 1261, 631))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.runButton = QtWidgets.QPushButton(simulationDialog)
        self.runButton.setGeometry(QtCore.QRect(1060, 670, 99, 38))
        self.runButton.setObjectName("runButton")
        self.quitButton = QtWidgets.QPushButton(simulationDialog)
        self.quitButton.setGeometry(QtCore.QRect(1170, 670, 99, 38))
        self.quitButton.setObjectName("quitButton")
        self.victorLabel = QtWidgets.QLabel(simulationDialog)
        self.victorLabel.setGeometry(QtCore.QRect(640, 680, 67, 22))
        self.victorLabel.setObjectName("victorLabel")
        self.victoryResultsLabel = QtWidgets.QLabel(simulationDialog)
        self.victoryResultsLabel.setGeometry(QtCore.QRect(690, 680, 251, 22))
        self.victoryResultsLabel.setText("")
        self.victoryResultsLabel.setObjectName("victoryResultsLabel")
        self.setArmySizeButton = QtWidgets.QPushButton(simulationDialog)
        self.setArmySizeButton.setGeometry(QtCore.QRect(520, 670, 111, 38))
        self.setArmySizeButton.setObjectName("setArmySizeButton")

        self.retranslateUi(simulationDialog)
        QtCore.QMetaObject.connectSlotsByName(simulationDialog)

    def retranslateUi(self, simulationDialog):
        _translate = QtCore.QCoreApplication.translate
        simulationDialog.setWindowTitle(_translate(
            "simulationDialog", "Py Fantasy Battlefield Simulator"))
        self.armyOfLightLabel.setText(_translate(
            "simulationDialog", "Army of Light"))
        self.armyOfDarknessLabel.setText(_translate(
            "simulationDialog", "Army of Darkness"))
        self.runButton.setText(_translate("simulationDialog", "Run"))
        self.runButton.setShortcut(_translate("simulationDialog", "Ctrl+R"))
        self.quitButton.setText(_translate("simulationDialog", "Quit"))
        self.quitButton.setShortcut(_translate("simulationDialog", "Ctrl+Q"))
        self.victorLabel.setText(_translate("simulationDialog", "Victor:"))
        self.setArmySizeButton.setText(
            _translate("simulationDialog", "Set Army Size"))
        self.setArmySizeButton.setShortcut(
            _translate("simulationDialog", "Ctrl+S"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    simulationDialog = QtWidgets.QDialog()
    ui = Ui_simulationDialog()
    ui.setupUi(simulationDialog)
    simulationDialog.show()
    sys.exit(app.exec_())
