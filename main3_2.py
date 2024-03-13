import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QListWidget, QCalendarWidget, QTimeEdit
from PyQt5.QtCore import QDateTime

class App(QWidget):
   def __init__(self):
      super().__init__()
      self.setWindowTitle('Ежедневник')
      self.setGeometry(100, 100, 400, 400)

      self.events = []

      layout = QVBoxLayout()

      event_layout = QHBoxLayout()
      event_layout.addWidget(QLabel('Событие:'))
      self.event_edit = QLabel('')
      event_layout.addWidget(self.event_edit)
      layout.addLayout(event_layout)

      calendar_layout = QHBoxLayout()
      calendar_layout.addWidget(QLabel('Дата:'))
      self.calendar = QCalendarWidget()
      calendar_layout.addWidget(self.calendar)
      layout.addLayout(calendar_layout)

      time_layout = QHBoxLayout()
      time_layout.addWidget(QLabel('Время:'))
      self.time_edit = QTimeEdit()
      time_layout.addWidget(self.time_edit)
      layout.addLayout(time_layout)

      add_button = QPushButton('Добавить')
      add_button.clicked.connect(self.add_event)
      layout.addWidget(add_button)

      layout.addWidget(QLabel('События:'))
      self.event_list = QListWidget()
      layout.addWidget(self.event_list)

      self.setLayout(layout)

   def add_event(self):
      event = self.event_edit.text()
      date = self.calendar.selectedDate()
      time = self.time_edit.time()

      datetime = QDateTime(date, time)

      self.events.append((datetime, event))
      self.events.sort()

      self.event_list.clear()
      for event in self.events:
         self.event_list.addItem(f'{event[0].toString("dd.MM.yyyy HH:mm")} - {event[1]}')

if __name__ == '__main__':
   app = QApplication(sys.argv)
   planner = App()
   planner.show()
   sys.exit(app.exec_())