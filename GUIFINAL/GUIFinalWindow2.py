from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog, QTabWidget, QCheckBox, QLineEdit, QAction
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys
import os
import platform
from PyQt5.QtWidgets import QMessageBox
import subprocess
from subprocess import call
import os.path


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        #Load the UI file
        uic.loadUi("GUIFinalWindow2.ui",self)

        #Initialize Widgets
        self.Changebutton = self.findChild(QPushButton,'pushButton')
        self.Changebutton2 = self.findChild(QPushButton,'pushButton_2')
        

        self.Changebutton.clicked.connect(self.pathwayeditor)
        self.Changebutton2.clicked.connect(lambda:self.close())

        #Shows the Window
        self.show()
    def pathwayeditor(self):
        fname = QFileDialog.getOpenFileName()
        f = open('preference1.txt', 'r+')
        f.truncate(0)
        with open('preference1.txt', 'a') as the_file:
            the_file.write(str(fname))
        
#Initialize the App

app = QApplication(sys.argv)
MainWindowWindow = MainWindow()
app.exec_()