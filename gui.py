# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 781, 25))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scriptLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.scriptLabel.setObjectName("scriptLabel")
        self.horizontalLayout.addWidget(self.scriptLabel)
        self.scriptFileLocation = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.scriptFileLocation.setObjectName("scriptFileLocation")
        self.horizontalLayout.addWidget(self.scriptFileLocation)
        self.scriptOpen = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.scriptOpen.setObjectName("scriptOpen")
        self.horizontalLayout.addWidget(self.scriptOpen)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(9, 530, 781, 25))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.windowedOption = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.windowedOption.setObjectName("windowedOption")
        self.horizontalLayout_3.addWidget(self.windowedOption)
        self.oneFile = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.oneFile.setObjectName("oneFile")
        self.horizontalLayout_3.addWidget(self.oneFile)
        self.convertPy = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.convertPy.setObjectName("convertPy")
        self.horizontalLayout_3.addWidget(self.convertPy)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(9, 39, 781, 25))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.targetLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.targetLabel.setObjectName("targetLabel")
        self.horizontalLayout_2.addWidget(self.targetLabel)
        self.outputFolderLocation = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.outputFolderLocation.setObjectName("outputFolderLocation")
        self.horizontalLayout_2.addWidget(self.outputFolderLocation)
        self.targetOpen = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.targetOpen.setObjectName("targetOpen")
        self.horizontalLayout_2.addWidget(self.targetOpen)
        self.topSeparator = QtWidgets.QFrame(self.centralwidget)
        self.topSeparator.setGeometry(QtCore.QRect(10, 66, 781, 16))
        self.topSeparator.setFrameShape(QtWidgets.QFrame.HLine)
        self.topSeparator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.topSeparator.setObjectName("topSeparator")
        self.bottomSeparator = QtWidgets.QFrame(self.centralwidget)
        self.bottomSeparator.setGeometry(QtCore.QRect(10, 500, 781, 21))
        self.bottomSeparator.setFrameShape(QtWidgets.QFrame.HLine)
        self.bottomSeparator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.bottomSeparator.setObjectName("bottomSeparator")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 89, 781, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.outputLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.outputLabel.setObjectName("outputLabel")
        self.verticalLayout.addWidget(self.outputLabel)
        self.commandOutput = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.commandOutput.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.commandOutput.setReadOnly(True)
        self.commandOutput.setObjectName("commandOutput")
        self.verticalLayout.addWidget(self.commandOutput)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyInstaller GUI"))
        self.scriptLabel.setText(_translate("MainWindow", "Script"))
        self.scriptOpen.setText(_translate("MainWindow", "Browse"))
        self.windowedOption.setText(_translate("MainWindow", "Windowed"))
        self.oneFile.setText(_translate("MainWindow", "One File"))
        self.convertPy.setText(_translate("MainWindow", "Compile"))
        self.targetLabel.setText(_translate("MainWindow", "Target"))
        self.targetOpen.setText(_translate("MainWindow", "Browse"))
        self.outputLabel.setText(_translate("MainWindow", "Output"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

