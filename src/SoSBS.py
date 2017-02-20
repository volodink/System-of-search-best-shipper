import random
import sys
from modules.DataGenerator import DataGenerator
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from collections import OrderedDict

class MainApp:
	def __init__(self):
		self.app = QtWidgets.QApplication(sys.argv)
		self.windows = uic.loadUi("ui/ui.ui")
		self.h1_base = 50
		self.h2_base = 50

		self.main()
		
		

	def genAndSetData(self):
		sti = QtGui.QStandardItemModel(parent = self.windows)
		self.dataDict = self.dataObj.getPartnerData(self.windows.spinBox.value())
		print(self.dataDict)
		midPrice = []
		for key in sorted(self.dataDict.keys()):
			item = QtGui.QStandardItem(self.dataDict[key]["contact"]["name"]) 
			midPrice.append(self.__getMidleValue(self.dataDict[key]["listingName"]))
			sti.appendRow(item)
		sti.setHorizontalHeaderLabels(["Название компании"])
		self.windows.tableView.setModel(sti)
		self.windows.tableView.resizeColumnsToContents()
		 
		# midPrice = [self.getMidleValue(i) for i in self.dataDict[0]["listingName"]]
		self.windows.doubleSpinBox_7.setMinimum(min(midPrice))
		self.windows.doubleSpinBox_7.setMaximum(max(midPrice))

		self.windows.doubleSpinBox_8.setMinimum(min(midPrice))
		self.windows.doubleSpinBox_8.setMaximum(max(midPrice))

		self.windows.doubleSpinBox_7.setValue(min(midPrice))
		self.windows.doubleSpinBox_8.setValue(max(midPrice))

		self.windows.groupBox_2.setDisabled(False)
		self.windows.groupBox_4.setDisabled(False)
		self.windows.pushButton_2.setDisabled(False)
		self.windows.tableView.setWordWrap(True)
	
	def __getMidleValue(self, dictValue):
		return sum([i[1] for i in dictValue])/len(dictValue)

			
	def main(self):
		self.dataObj = DataGenerator("sortDict.txt")
		self.windows.pushButton.clicked.connect(self.genAndSetData)
		
		self.windows.spinBox.setValue(10)
		self.app.setWindowIcon(QtGui.QIcon("../img/icon.ico"))
		self.windows.setWindowFlags(QtCore.Qt.Window)
		self.windows.label_3.setText(str(self.windows.horizontalSlider.value()))
		self.windows.label_6.setText(str(self.windows.horizontalSlider_4.value()))

		self.windows.horizontalSlider.valueChanged.connect(self. changeValueInSlider)
		self.windows.tableView.clicked.connect(self.getSelectRow)


		css = open("css/mainApp.css").read()
		self.windows.setStyleSheet(css)
	
	def changeValueInSlider(self):
		self.windows.horizontalSlider_4.setValue(self.windows.horizontalSlider_4.value() - (self.windows.horizontalSlider.value() - self.h1_base))
		self.h1_base = self.windows.horizontalSlider.value()
		self.h2_base = self.windows.horizontalSlider_4.value()

	def getSelectRow(self):
		indexes = self.windows.tableView.selectionModel().selectedRows()
		for index in sorted(indexes):
			print('Row %d is selected' % index.row())

if __name__ == "__main__":
	
	mainApp = MainApp()
	mainApp.windows.show()
	sys.exit(mainApp.app.exec_())
