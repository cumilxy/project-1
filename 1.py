from PyQt5.QtWidgets import ( QApplication, QWidget, QPushButton, QLabel, QListWidget,QHBoxLayout, QVBoxLayout, QFileDialog)
from PyQt5.QtCore import Qt

import os
app = QApplication([])

'''Інтерфейс програми'''
window = QWidget()
window.setWindowTitle('Фотошопчик')
window.resize(900,600)

move_left = QPushButton('Вліво')
move_left.setStyleSheet("background-color:lightgreen; color:olive")
move_right = QPushButton('Вправо')
move_right.setStyleSheet("background-color:lightgreen; color:olive")
mirrorro = QPushButton('Дзеркало')
mirrorro.setStyleSheet("background-color:lightgreen; color:olive")
Sharpness_knopka = QPushButton('Різкість')
Sharpness_knopka.setStyleSheet("background-color:lightgreen; color:olive")
BandW_knopka = QPushButton('Ч\Б')
BandW_knopka.setStyleSheet("background-color:lightgreen; color:olive")
folderrr = QPushButton('ПАПКА')
folderrr.setStyleSheet("background-color:lightgreen; color:olive")
list_things = QListWidget()
list_things.setStyleSheet("background-color:wheat; color:black")

pole_with_kartinka = QLabel()
pole_with_kartinka.setStyleSheet("background-color:wheat; color:black")

v1 = QVBoxLayout()
v1.addWidget(folderrr)
v1.addWidget(list_things)

h1 = QHBoxLayout()
h1.addWidget(move_left)
h1.addWidget(move_right)
h1.addWidget(mirrorro)
h1.addWidget(Sharpness_knopka)
h1.addWidget(BandW_knopka)

v2 = QVBoxLayout()
v2.addWidget(pole_with_kartinka)
v2.addLayout(h1)
h2 = QHBoxLayout()
h2.addLayout(v1)
h2.addLayout(v2)
window.setLayout(h2)
window.show()

def choise_workdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    
def filter(files, extensions):
    result = []
    for f in files:
        for e in extensions:
            if f.endswith(e):
                result.append(f)
    return result

def showfiles():
    extensions = ['jpeg','png','svg','jpg']
    choise_workdir()
    filenames = os.listdir(workdir)
    list_things.clear()
    for f in filenames:
        list_things.addItem(f)
folderrr.clicked.connect(showfiles)
app.exec_()

