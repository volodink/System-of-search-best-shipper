import random
import sys
from modules.DataGenerator import DataGenerator
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from modules import mathRating 
from math import floor, ceil
# from collections import OrderedDict

class MainApp:
	def __init__(self):
		self.app = QtWidgets.QApplication(sys.argv)
		self.windows = uic.loadUi("ui/mainUI.ui")
		self.h1_base = 50
		self.h2_base = 50

		self.main()
		
		
	def genAndSetData(self):
		sti = QtGui.QStandardItemModel(parent = self.windows)
		self.dataDict = self.dataObj.getPartnerData(self.windows.spinBox.value())
		# print(self.dataDict)
		self.midPrice = []
		diliveryStat = []
		self.reliability = []
		self.quality = []
		for key in sorted(self.dataDict.keys()):
			item = QtGui.QStandardItem(self.dataDict[key]["contact"]["name"]) 
			self.midPrice.append(self.__getMidleValue(self.dataDict[key]["listingName"]))
			diliveryStat.append(self.dataDict[key]["dateOfDelivery"])
			self.quality.append(self.dataDict[key]["quality"])
			self.reliability.append(mathRating.getReliabilityRating(self.dataDict[key]["reliability"]["numBrokeSupply"],
										self.dataDict[key]["reliability"]["numLawsuitsNow"],
										self.dataDict[key]["reliability"]["numLawsuitsPast"],
										self.dataDict[key]["reliability"]["companyAge"],
										self.dataDict[key]["reliability"]["financPosition"],
										self.dataDict[key]["reliability"]["numberOfClient"]))
										
			sti.appendRow(item)
		self.maxReliability = max([i/50 for i in self.reliability])
		self.maxQuality = max([i/50 for i in self.quality])
		sti.setHorizontalHeaderLabels(["Название компании"])
		self.windows.tableView.setModel(sti)
		self.windows.tableView.resizeColumnsToContents()
		 
		# self.midPrice = [self.getMidleValue(i) for i in self.dataDict[0]["listingName"]]
		self.windows.doubleSpinBox_7.setMinimum(float(floor(min(self.midPrice))))
		self.windows.doubleSpinBox_7.setMaximum(float(ceil(max(self.midPrice))))

		self.windows.doubleSpinBox_8.setMinimum(float(floor(min(self.midPrice))))
		self.windows.doubleSpinBox_8.setMaximum(float(ceil(max(self.midPrice))))

		self.windows.doubleSpinBox_7.setValue(float(floor(min(self.midPrice))))
		self.windows.doubleSpinBox_8.setValue(float(ceil(max(self.midPrice))))

		self.windows.spinBox_2.setMinimum(min(diliveryStat))
		self.windows.spinBox_2.setMaximum(max(diliveryStat))

		self.windows.spinBox_3.setMinimum(min(diliveryStat))
		self.windows.spinBox_3.setMaximum(max(diliveryStat))

		self.windows.spinBox_2.setValue(min(diliveryStat))
		self.windows.spinBox_3.setValue(max(diliveryStat))

		self.windows.groupBox_2.setDisabled(False)
		self.windows.groupBox_4.setDisabled(False)
		self.windows.pushButton_2.setDisabled(False)
		self.windows.tableView.setWordWrap(True)


	def searchBestPartner(self):
		sti = QtGui.QStandardItemModel(parent = self.windows)
		self.windows.tableView.setModel(sti)
		
		
		for key in sorted(self.dataDict.keys()):
			if not (self.windows.doubleSpinBox_7.value() < self.midPrice[key] < self.windows.doubleSpinBox_8.value()):
				continue
			if not ((self.windows.spinBox_2.value() <= self.dataDict[key]["dateOfDelivery"] <= self.windows.spinBox_3.value())):
				continue
			raiting = str(mathRating.getPartnerRating(self.reliability[key],
										self.quality[key],
										self.maxReliability,
										self.maxQuality,
										self.windows.horizontalSlider.value(),
										self.windows.horizontalSlider_4.value()))

			row1 = QtGui.QStandardItem(self.dataDict[key]["contact"]["name"])
			row2 = QtGui.QStandardItem(raiting)
			row3 = QtGui.QStandardItem(str(self.midPrice[key]))
			row4 = QtGui.QStandardItem(str(self.dataDict[key]["dateOfDelivery"]))
			row5 = QtGui.QStandardItem(str(self.dataDict[key]["reliability"]["financPosition"]))
			row6 = QtGui.QStandardItem(str(self.dataDict[key]["reliability"]["numBrokeSupply"]))
			row7 = QtGui.QStandardItem(str(self.dataDict[key]["reliability"]["numLawsuitsNow"]))
			row8 = QtGui.QStandardItem(str(self.dataDict[key]["reliability"]["companyAge"]))
			row9 = QtGui.QStandardItem(str(self.dataDict[key]["reliability"]["numberOfClient"]))
			row10 = QtGui.QStandardItem(str(self.dataDict[key]["contact"]["phoneNumber"]))
			row11 = QtGui.QStandardItem(str(self.dataDict[key]["contact"]["email"]))
			row12 = QtGui.QStandardItem(str(self.dataDict[key]["contact"]["site"]))
			row13 = QtGui.QStandardItem(str(self.dataDict[key]["quality"]))
			row14 = QtGui.QStandardItem(str(self.reliability[key]))
			sti.appendRow([row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11, row12, row13, row14])
		
		sti.setHorizontalHeaderLabels(["Название компании", 
										"Рейтинг", 
										"Средняя цена",
										"Время доставки",
										"Финансовый оборот", 
										"Количество сорваных доставок", 
										"Количество судов (сейчас)",
										"Количество судов (в прошлом)",
										"Возраст компании (лет)" , 
										"Номер телефона", 
										"Email",
										"Сайт",
										"Качество",
										"Надежность"]) 
		self.windows.tableView.setModel(sti)
		self.windows.tableView.setSortingEnabled(True)
		self.windows.tableView.sortByColumn(1, QtCore.Qt.DescendingOrder)
		self.windows.tableView.resizeColumnsToContents()

			
	def __getMidleValue(self, dictValue):
		return sum([i[1] for i in dictValue])/len(dictValue)

			
	def main(self):
		self.dataObj = DataGenerator("txt/sortDict.txt")
		self.windows.pushButton.clicked.connect(self.genAndSetData)
		self.windows.pushButton_2.clicked.connect(self.searchBestPartner)
		
		self.windows.spinBox.setValue(50)
		self.app.setWindowIcon(QtGui.QIcon("../img/icon.ico"))
		self.windows.setWindowFlags(QtCore.Qt.Window)
		self.windows.label_3.setText(str(self.windows.horizontalSlider.value()))
		self.windows.label_6.setText(str(self.windows.horizontalSlider_4.value()))

		# self.windows.horizontalSlider.valueChanged.connect(lambda: self.changeValueInSlider(self.windows.horizontalSlider, 
		# 																					self.windows.horizontalSlider_4, 
		# 																					self.windows.label_3, 
		# 																					self.windows.label_6,
		# 																					True))
		# self.windows.horizontalSlider_4.valueChanged.connect(lambda: self.changeValueInSlider(self.windows.horizontalSlider_4, 
		# 																					  self.windows.horizontalSlider, 
		# 																					  self.windows.label_6, 
		# 																					  self.windows.label_3,
		# 																					  False))
		self.windows.tableView.clicked.connect(self.getSelectRow)


		css = open("css/mainApp.css").read()
		self.windows.setStyleSheet(css)

	##############################################
	### ВНИМАНИЕ!! ПРЕВЫШЕН УРОВЕНЬ ГОВНОКОДА! ### 
	def changeValueInSlider(self, first, second, firstLable, secondLable, boolPr):
		second.blockSignals(True)
		if boolPr:
			second.setValue(second.value() - (first.value() - self.h1_base))
		else:
			second.setValue(second.value() - (first.value() - self.h2_base))
		secondLable.setText(str(second.value()))
		if boolPr:
			self.h1_base = first.value()
			self.h2_base = second.value()
		else:
			self.h1_base = second.value()
			self.h2_base = first.value()
		second.blockSignals(False)
	########## НИКОГДА ТАК НЕ ДЕЛАЙТЕ!!! ##########
	###############################################

	def getSelectRow(self):
		indexes = self.windows.tableView.selectionModel().selectedIndexes()
		# print([i for i in indexes])
		# print(len(indexes))
		for index in sorted(indexes):
			print('Row %d is selected' % index.row())

if __name__ == "__main__":
	mainApp = MainApp()
	mainApp.windows.show()
	sys.exit(mainApp.app.exec_())
