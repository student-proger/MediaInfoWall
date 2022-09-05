# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainform.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1011, 622)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("mainicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1011, 21))
        self.menuBar.setObjectName("menuBar")
        self.menu123 = QtWidgets.QMenu(self.menuBar)
        self.menu123.setObjectName("menu123")
        MainWindow.setMenuBar(self.menuBar)
        self.loadCommandsAction = QtWidgets.QAction(MainWindow)
        self.loadCommandsAction.setObjectName("loadCommandsAction")
        self.saveCommandsAction = QtWidgets.QAction(MainWindow)
        self.saveCommandsAction.setObjectName("saveCommandsAction")
        self.clearCommandsAction = QtWidgets.QAction(MainWindow)
        self.clearCommandsAction.setObjectName("clearCommandsAction")
        self.loadTaskHostsAction = QtWidgets.QAction(MainWindow)
        self.loadTaskHostsAction.setObjectName("loadTaskHostsAction")
        self.clearHostsAction = QtWidgets.QAction(MainWindow)
        self.clearHostsAction.setObjectName("clearHostsAction")
        self.aboutAction = QtWidgets.QAction(MainWindow)
        self.aboutAction.setObjectName("aboutAction")
        self.subWindowViewAction = QtWidgets.QAction(MainWindow)
        self.subWindowViewAction.setObjectName("subWindowViewAction")
        self.tabbedWindowViewAction = QtWidgets.QAction(MainWindow)
        self.tabbedWindowViewAction.setObjectName("tabbedWindowViewAction")
        self.action123 = QtWidgets.QAction(MainWindow)
        self.action123.setObjectName("action123")
        self.menu123.addAction(self.action123)
        self.menuBar.addAction(self.menu123.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Linux Remote Master"))
        self.menu123.setTitle(_translate("MainWindow", "123"))
        self.loadCommandsAction.setText(_translate("MainWindow", "Загрузить..."))
        self.loadCommandsAction.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.saveCommandsAction.setText(_translate("MainWindow", "Сохранить..."))
        self.saveCommandsAction.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.clearCommandsAction.setText(_translate("MainWindow", "Очистить"))
        self.clearCommandsAction.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.loadTaskHostsAction.setText(_translate("MainWindow", "Загрузить список..."))
        self.loadTaskHostsAction.setShortcut(_translate("MainWindow", "Ctrl+Shift+O"))
        self.clearHostsAction.setText(_translate("MainWindow", "Очистить список"))
        self.clearHostsAction.setShortcut(_translate("MainWindow", "Ctrl+Shift+N"))
        self.aboutAction.setText(_translate("MainWindow", "О программе..."))
        self.subWindowViewAction.setText(_translate("MainWindow", "Отдельные окна"))
        self.tabbedWindowViewAction.setText(_translate("MainWindow", "Вкладки"))
        self.action123.setText(_translate("MainWindow", "123"))
