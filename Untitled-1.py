from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout


app = QApplication([])


'''Інтерфейс програми'''
# параметри вікна програми
notes_win = QWidget()
notes_win.setWindowTitle('Розумні замітки')
notes_win.resize(900, 600)


text = QLabel('Текст')
button = QPushButton('кнопка')
button2 = QPushButton('кнопка')
v1 = QVBoxLayout()
h1 = QHBoxLayout()
v1.addWidget(text)
h1.addWidget(button)
h1.addWidget(button2)
v1.addLayout(h1)
notes_win.setLayout(v1)
# запуск програми
notes_win.show()
app.exec_()