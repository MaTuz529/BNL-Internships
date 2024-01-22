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
import shutil

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        #Load the UI file
        uic.loadUi("GUIFinalWindow3.ui",self)

        #Initialize Widgets
        self.Yesbutton = self.findChild(QPushButton,'pushButton')

        self.Nobutton = self.findChild(QPushButton,'pushButton_2')

        self.Nobutton.clicked.connect(lambda:self.close())

        self.Yesbutton.clicked.connect(self.yes)
             
        self.show()
    def yes(self):
        #This is the function to copy the file into the other file
        def append_files_method2(file1_path, file2_path):
            with open(file1_path, 'r') as file1:
                with open(file2_path, 'a') as file2:
                    shutil.copyfileobj(file1, file2)
        #Need something to read the file
        f = open("filenamer.txt", "r")
        nameoffile2 = f.readline()
        #Open and copy for the file
        with open(str(nameoffile2)+".inp", 'w') as f:
            file1_path = "skel.inp"
            file2_path = nameoffile2+".inp"
            append_files_method2(file1_path, file2_path)
        self.close()
#Initialize the App

app = QApplication(sys.argv)
MainWindowWindow = MainWindow()
app.exec_()