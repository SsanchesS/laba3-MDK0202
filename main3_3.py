import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget

class App(QWidget):
   def __init__(self):
      super().__init__()
      self.setWindowTitle('Записная книжка')
      self.setGeometry(100, 100, 400, 300)

      self.contacts = []

      layout = QVBoxLayout()

      contact_layout = QHBoxLayout()
      contact_layout.addWidget(QLabel('Имя контакта:'))
      self.name_edit = QLineEdit()
      contact_layout.addWidget(self.name_edit)
      layout.addLayout(contact_layout)

      number_layout = QHBoxLayout()
      number_layout.addWidget(QLabel('Номер телефона:'))
      self.number_edit = QLineEdit()
      number_layout.addWidget(self.number_edit)
      layout.addLayout(number_layout)

      add_button = QPushButton('Добавить')
      add_button.clicked.connect(self.add_contact)
      layout.addWidget(add_button)

      layout.addWidget(QLabel('Контакты:'))
      self.contact_list = QListWidget()
      layout.addWidget(self.contact_list)

      self.setLayout(layout)

   def add_contact(self):
      name = self.name_edit.text()
      number = self.number_edit.text()
      contact = f'{name}: {number}'
      self.contacts.append(contact)
      self.update_contact_list()

   def update_contact_list(self):
      self.contact_list.clear()
      self.contact_list.addItems(self.contacts)

if __name__ == '__main__':
   app = QApplication(sys.argv)
   address_book = App()
   address_book.show()
   sys.exit(app.exec_())