import random
import sys
from modules.DataGenerator import DataGenerator
from PyQt5 import QtWidgets, uic, QtGui

def test():
	sti = QtGui.QStandardItemModel(parent = windows)
	for i in range(windows.spinBox.value()):
		item = QtGui.QStandardItem(name.getRandomName(random.randint(1, 4))) 
		sti.appendRow(item)
	windows.tableView.setModel(sti)
	windows.tableView.resizeColumnsToContents()


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	name = DataGenerator("sortDict.txt")
	
	windows = uic.loadUi("ui/ui.ui")
	windows.pushButton.clicked.connect(test)
	windows.spinBox.setValue(10)
	app.setWindowIcon(QtGui.QIcon("../img/icon.png"))
	windows.setWindowIcon(QtGui.QIcon("../img/icon.png"))
	windows.show()
	sys.exit(app.exec_())
