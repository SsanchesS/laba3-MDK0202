import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QPushButton, QMessageBox

class App(QWidget):
   def __init__(self):
      super().__init__()
      self.setWindowTitle('Текстовый флаг')
      self.setFixedSize(300, 200)
      self.colors = {'Красный': None, 'Зелёный': None, 'Синий': None, 'Жёлтый': None, 'Белый': None}
      self.selected_colors = []

      layout = QVBoxLayout()

      for color in self.colors:
         radio_button = QRadioButton(color)
         radio_button.toggled.connect(self.on_radio_button_toggled)
         layout.addWidget(radio_button)

      draw_button = QPushButton('Нарисовать')
      draw_button.clicked.connect(self.draw_flag)
      layout.addWidget(draw_button)

      self.setLayout(layout)

   def on_radio_button_toggled(self):
      sender = self.sender()
      if sender.isChecked():
         self.selected_colors.append(sender.text())
         if len(self.selected_colors) > 3:
               sender.setChecked(False)
               self.selected_colors.remove(sender.text())

   def draw_flag(self):
      if len(self.selected_colors) == 3:
         message = ', '.join(self.selected_colors)
         QMessageBox.information(self, 'Результат', message)
         self.selected_colors = []
      else:
         QMessageBox.warning(self, 'Предупреждение', 'Выберите три цвета для каждой из трёх полос флага.')

if __name__ == '__main__':
   app = QApplication(sys.argv)
   app2 = App()
   app2.show()
   sys.exit(app.exec_())