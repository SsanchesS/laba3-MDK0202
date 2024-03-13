import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QPushButton, QStatusBar
from PyQt5.QtGui import QColor

class App(QWidget):
   def __init__(self):
      super().__init__()
      self.setWindowTitle('Антиплагиат')
      self.setGeometry(100, 100, 500, 300)

      layout = QVBoxLayout()

      self.text_edit_1 = QTextEdit()
      layout.addWidget(self.text_edit_1)

      self.text_edit_2 = QTextEdit()
      layout.addWidget(self.text_edit_2)

      self.check_button = QPushButton('Проверить')
      self.check_button.clicked.connect(self.check_plagiarism)
      layout.addWidget(self.check_button)

      self.status_bar = QStatusBar()
      layout.addWidget(self.status_bar)

      self.setLayout(layout)

   def check_plagiarism(self):
      text_1 = self.text_edit_1.toPlainText().lower()
      text_2 = self.text_edit_2.toPlainText().lower()

      words_1 = set(text_1.split())
      words_2 = set(text_2.split())

      common_words = words_1.intersection(words_2) # только те элементы, которые есть и в words_1, и в words_2
      similarity_percentage = (len(common_words) / max(len(words_1), len(words_2))) * 100

      if not text_1.strip() or not text_2.strip() or similarity_percentage >= 50:  # Порог антиплагиата 50%
         self.status_bar.showMessage('Сходство обнаружено', 5000)
         self.status_bar.setStyleSheet("color: red")
      else:
         self.status_bar.showMessage('Сходство не обнаружено', 5000)
         self.status_bar.setStyleSheet("color: green")

if __name__ == '__main__':
   app = QApplication(sys.argv)
   game = App()
   game.show()
   sys.exit(app.exec_())