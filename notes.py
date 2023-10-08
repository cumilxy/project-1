from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout


import json

app = QApplication([])


'''Інтерфейс програми'''
# параметри вікна програми
notes_win = QWidget()
notes_win.setWindowTitle('Розумні замітки')
notes_win.resize(900, 600)


# віджети вікна програми
list_notes = QListWidget()
list_notes.setStyleSheet("background-color: aqua; color: black")
list_notes_label = QLabel('Список заміток')



button_note_create = QPushButton('Створити замітку') # з'являється вікно з полем "Введіть ім'я замітки"
button_note_create.setStyleSheet("background-color: yellow; color: black")
button_note_del = QPushButton('Видалити замітку')
button_note_del.setStyleSheet("background-color: yellow; color: black")
button_note_save = QPushButton('Зберегти замітку')
button_note_save.setStyleSheet("background-color: yellow; color: black")
button_note_save.setStyleSheet("background-color: yellow; color: purple")


field_tag = QLineEdit('')
field_tag.setStyleSheet("background-color: aqua; color: black")
field_tag.setPlaceholderText('Введіть тег...')
field_text = QTextEdit()
field_text.setStyleSheet("background-color: aqua; color:black")
button_tag_add = QPushButton('Додати до замітки')
button_tag_add.setStyleSheet("background-color: orange; color: green")
button_tag_del = QPushButton('Відкріпити від замітки')
button_tag_del.setStyleSheet("background-color: orange; color: green")
button_tag_search = QPushButton('Шукати замітки по тегу')
button_tag_search.setStyleSheet("background-color: orange; color: green")
list_tags = QListWidget()
list_tags.setStyleSheet("background-color: aqua; color: black")
list_tags_label = QLabel('Список тегів')


# розташування віджетів по лейаутах
layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)


col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)


col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)


col_2.addLayout(row_3)
col_2.addLayout(row_4)


layout_notes.addLayout(col_1, stretch = 2)
layout_notes.addLayout(col_2, stretch = 1)
notes_win.setLayout(layout_notes)

def show_notes():
    key = list_notes.selectedItems()[0].text()
    field_text.setText(notes[key]["текст"])

def add_notes():
    dialog, ok = QInputDialog.getText(notes_win, "додати замітку","назва замітки")
    if dialog and ok != "":
        notes[dialog] = {"текст":"","теги":[]}
        list_notes.addItem(dialog)

def save_notes():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]['текст']=field_text.toPlainText()
        with open("f.json", "w") as file:
            json.dump(notes,file)
    
def del_notes():
     if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        field_text.clear()
        list_notes.clear()
        list_notes.addItems(notes)
        with open("f.json", "w") as file:
            json.dump(notes,file)
     

list_notes.itemClicked.connect(show_notes)
button_note_create.clicked.connect(add_notes)
button_note_save.clicked.connect(save_notes)
button_note_del.clicked.connect(del_notes)

with open("f.json", "r") as file:
    notes = json.load(file)
list_notes.addItems(notes)


# запуск програми
notes_win.show()
app.exec_()