import random
import sys
from modules.DataGenerator import DataGenerator
from PyQt5 import QtWidgets, uic, QtGui, QtCore

class MainApp:
	def __init__(self):
		self.app = QtWidgets.QApplication(sys.argv)
		self.windows = uic.loadUi("ui/ui.ui")
		self.main()

	def test(self):
		sti = QtGui.QStandardItemModel(parent = self.windows)
		for i in range(self.windows.spinBox.value()):
			item = QtGui.QStandardItem(self.name._DataGenerator__getRandomName(random.randint(1, 3))) 
			sti.appendRow(item)
		sti.setHorizontalHeaderLabels(["Название компании"])
		self.windows.tableView.setModel(sti)
		self.windows.tableView.resizeColumnsToContents()
		self.windows.groupBox_2.setDisabled(False)
		self.windows.groupBox_4.setDisabled(False)
		self.windows.pushButton_2.setDisabled(False)
		self.windows.tableView.setWordWrap(True)
		# self.windows.tableView.setColumnCount(2)
		# self.windows.tableView.resizeRowsToContents()
		# self.windows.tableView.resizeColumnsToContents()   
		# self.windows.tableView.setFixedSize(self.windows.tableView.horizontalHeader().length(), self.windows.tableView.verticalHeader().length())
	
	def main(self):
		self.name = DataGenerator("sortDict.txt")
		self.windows.pushButton.clicked.connect(self.test)
		
		self.windows.spinBox.setValue(10)
		self.app.setWindowIcon(QtGui.QIcon("../img/icon.ico"))
		self.windows.setWindowFlags(QtCore.Qt.Window)



		css = open("css/mainApp.css").read()
		self.windows.setStyleSheet(css)


if __name__ == "__main__":
	
	mainApp = MainApp()
	mainApp.windows.show()
	sys.exit(mainApp.app.exec_())
