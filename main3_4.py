import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox

class App(QWidget):
   def __init__(self):
      super().__init__()
      self.setWindowTitle('Игра "Псевдоним"')
      self.setGeometry(100, 100, 400, 200)

      self.pile_size = 0
      self.current_player = 'Игрок'
      self.stones_left = 0

      self.init_ui()

   def init_ui(self):
      self.layout = QVBoxLayout()

      self.info_label = QLabel('')
      self.layout.addWidget(self.info_label)

      self.stones_label = QLabel('')
      self.layout.addWidget(self.stones_label)

      self.stones_edit = QLineEdit()
      self.layout.addWidget(self.stones_edit)

      self.play_button = QPushButton('Ход')
      self.play_button.clicked.connect(self.play_turn)
      self.layout.addWidget(self.play_button)

      self.setLayout(self.layout)

      self.new_game()

   def new_game(self):
      self.pile_size = random.randint(8, 15)
      self.stones_left = self.pile_size
      self.current_player = 'Игрок'
      self.update_info()

   def update_info(self):
      self.info_label.setText(f'Ходит: {self.current_player}')
      self.stones_label.setText(f'Количество камней: {self.stones_left}')

   def play_turn(self):
      if self.current_player == 'Игрок':
         try:
               stones_to_take = int(self.stones_edit.text())
               if stones_to_take < 1 or stones_to_take > 3 or stones_to_take > self.stones_left:
                  raise ValueError
               self.stones_left -= stones_to_take
               self.current_player = 'Компьютер'
               self.update_info()
               if self.stones_left == 0:
                  QMessageBox.information(self, 'Победа', 'Вы победили!')
                  self.new_game()
               else:
                  self.computer_turn()
         except ValueError:
               QMessageBox.warning(self, 'Ошибка', 'Введите корректное число камней (от 1 до 3)')
      else:
         pass  # Ход компьютера

   def computer_turn(self):
      # Ход компьютера
      stones_to_take = self.stones_left % 4
      if stones_to_take == 0:
         stones_to_take = random.randint(1, 3)
      self.stones_left -= stones_to_take
      self.current_player = 'Игрок'
      self.update_info()
      if self.stones_left == 0:
         QMessageBox.information(self, 'Поражение', 'Вы проиграли!')
         self.new_game()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   game = App()
   game.show()
   sys.exit(app.exec_())