from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QRadioButton, QMessageBox, QTextEdit, QListWidget, QLineEdit, QInputDialog
from PyQt5.QtGui import QFont

app = QApplication([])

main_win = QWidget()
main_win.show()

main_win.setWindowTitle("Winner ..")
main_win.resize(1500, 700)

layout_main = QHBoxLayout()
# left
layout_left = QVBoxLayout()
layout_main.addLayout(layout_left, stretch= 2)
edit_text = QTextEdit()
edit_text.setFont(QFont('Ariel', 10))
layout_left.addWidget(edit_text)

# right
layout_right = QVBoxLayout()
layout_main.addLayout(layout_right, stretch= 1)
# top right
layout_top_right = QVBoxLayout()
layout_right.addLayout(layout_top_right)
label_note = QLabel("List of notes")

label_note.setFont(QFont('Ariel', 10))

layout_top_right.addWidget(label_note)
list_note = QListWidget()
layout_top_right.addWidget(list_note)

layout_note_button = QHBoxLayout()
layout_top_right.addLayout(layout_note_button)
button_create_note_tr = QPushButton("Create Note")
button_create_note_tr.setFont(QFont('Ariel', 10))
layout_note_button.addWidget(button_create_note_tr)
button_delete_note_tr = QPushButton("Delete Note")
button_delete_note_tr.setFont(QFont('Ariel', 10))
layout_note_button.addWidget(button_delete_note_tr)
button_save_note_tr = QPushButton("Save Note")
button_save_note_tr.setFont(QFont('Ariel', 10))
layout_top_right.addWidget(button_save_note_tr)

# bottom right
layout_bottom_right = QVBoxLayout()
layout_right.addLayout(layout_bottom_right)
label_tag = QLabel("List of tags")

label_tag.setFont(QFont('Ariel', 10))

layout_bottom_right.addWidget(label_tag)
list_tag = QListWidget()
layout_bottom_right.addWidget(list_tag)

edit_line = QLineEdit()
edit_line.setPlaceholderText("Enter tag...")
edit_line.setFont(QFont('Ariel', 10))
layout_bottom_right.addWidget(edit_line)

layout_tag_button = QHBoxLayout()
layout_bottom_right.addLayout(layout_tag_button)
button_create_tag_br = QPushButton("Create Tag")
button_create_tag_br.setFont(QFont('Ariel', 10))
layout_tag_button.addWidget(button_create_tag_br)
button_delete_tag_br = QPushButton("Delete Tag")
button_delete_tag_br.setFont(QFont('Ariel', 10))
layout_tag_button.addWidget(button_delete_tag_br)

button_search_tag_br = QPushButton("Search Tag")
button_search_tag_br.setFont(QFont('Ariel', 10))
layout_bottom_right.addWidget(button_search_tag_br)

main_win.setLayout(layout_main)

import json
file = open("notes_data_Finn.json", "r")
note_data = json.load(file)
# print(note_data["NOTE1"])
# print(note_data["NOTE1"]["tags"])
# print(note_data["NOTE1"]["text"])
# print(note_data.keys
list_note.addItems(note_data.keys())

def show_note():
    select_note = list_note.selectedItems()[0].text()
    tags = note_data[select_note]["tags"]
    list_tag.clear()
    list_tag.addItems(tags)

    text = note_data[select_note]["text"]
    edit_text.setText(text)

list_note.itemClicked.connect(show_note)

def create_tag():
    new_tag = edit_line.text()
    select_note = list_note.selectedItems()[0].text()
    tags = note_data[select_note]["tags"]
    print("Before", tags)
    if new_tag in tags:
        print("Already added")    
    else:
        tags.append(new_tag)
        print("After", tags)
    list_tag.clear()
    list_tag.addItems(tags)

button_create_tag_br.clicked.connect(create_tag)

def delete_tag():
    if len(list_note.selectedItems()) > 0 and len(list_tag.selectedItems()) > 0:
        select_tag = list_tag.selectedItems()[0].text()
        select_note = list_note.selectedItems()[0].text()
        tags = note_data[select_note]["tags"]
        tags.remove(select_tag)
        list_tag.clear()
        list_tag.addItems(tags)
button_delete_tag_br.clicked.connect(delete_tag)

def search_tag():
    text_results = "Found in: \n"
    count = 0

    search_tag = edit_line.text()
    for note_name in note_data:
        tags = note_data[note_name]["tags"]
        if search_tag in tags:
            text_results += " - " + note_name + "\n"
            count = count + 1
    if count == 0:
        text_results = "Found nothing"
    edit_text.setText(text_results)
button_search_tag_br.clicked.connect(search_tag)

def delete_note():
    if len(list_note.selectedItems()) > 0 :
        select_note = list_note.selectedItems()[0].text()
        del note_data[select_note]
        list_tag.clear()
        list_note.clear()
        edit_text.clear()
        list_note.addItems(note_data)
button_delete_note_tr.clicked.connect(delete_note)

def create_note():
    inputDialog = QInputDialog()
    inputDialog.resize(500,1)
    inputDialog.setFont(QFont('Ariel', 20))
    inputDialog.setInputMode(QInputDialog.TextInput)
    inputDialog.setWindowTitle('Add note')
    inputDialog.setLabelText('Note name:')
    ok = inputDialog.exec_()
    new_note_name = inputDialog.textValue()

    # print(ok, new_note_name)
    # QInputDialog.getText(main_win, "Add note:", "Note name:")
    # new_note_name = "NOTE 3"

    note_data[new_note_name] = {"tags": [], "text": ""}
    print(note_data)
    list_note.clear()
    list_note.addItems(note_data)
button_create_note_tr.clicked.connect(create_note)

app.exec_()