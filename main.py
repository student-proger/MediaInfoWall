#!/usr/bin/python3

'''
* Author:         Gladyshev Dmitriy (2022)
*
* Design Name:    MediaInfoWall
* Description:    Программа для информационных панелей
'''

import os
import sys  # sys нужен для передачи argv в QApplication
from datetime import datetime
import time
import json

# Qt
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QDir, QUrl
from PyQt5.QtWidgets import QTableWidgetItem, QMdiSubWindow, QMessageBox, QFileDialog, QMdiArea, QInputDialog, \
    QLineEdit, QVBoxLayout
from PyQt5.Qt import pyqtSignal
from PyQt5.QtGui import QColor
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
# design
import mainform

def messageBox(title: str, msg: str):
    """
    Отображение диалогового окна с сообщением.

    :param title: заголовок окна
    :param msg: сообщение
    """
    msgbox = QMessageBox()
    msgbox.setIcon(QMessageBox.Information)
    msgbox.setText(msg)
    msgbox.setWindowTitle(title)
    msgbox.exec_()

class MIWApp(QtWidgets.QMainWindow, mainform.Ui_MainWindow):
    """ Класс главного окна приложения. """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.videoWidget = QVideoWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.videoWidget)
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.videoWidget)
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)
        self.action123.triggered.connect(self.openFile)

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",
                                                  QDir.homePath())

        if fileName != '':
            self.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile(fileName)))
            #self.playButton.setEnabled(True)
        self.showFullScreen()  # self.showNormal() or self.showMaximized()
        self.play()

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def handleError(self):
        messageBox("", "Error: " + self.mediaPlayer.errorString())

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            pass
        else:
            pass

    def positionChanged(self, position):
        #self.positionSlider.setValue(position)
        pass

    def durationChanged(self, duration):
        #self.positionSlider.setRange(0, duration)
        pass

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)


def main():
    global path

    k = 0
    path = __file__
    for i in range(0, len(path)):
        if path[i] == "\\" or path[i] == "/":
            k = i
    path = path[:k + 1]
    print("PATH: " + path)

    app = QtWidgets.QApplication(sys.argv)
    window = MIWApp()
    window.show()

    app.exec_()


if __name__ == '__main__':
    main()
