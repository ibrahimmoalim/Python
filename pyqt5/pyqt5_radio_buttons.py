# PyQt5 radio buttons

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setGeometry(700, 300, 700, 555)
    self.setWindowTitle("PyQt5 Radio Buttons Practice")
    # set general styles that apply to everything inside the mainwindow
    # can be overrided later if we set styles targeting a specific widget
    # self.setStyleSheet("font-family: Arial;"
    #                    "font-weight: bold;"
    #                    "font-size: 16px;")
    self.radio1 = QRadioButton("Visa", self)
    self.radio2 = QRadioButton("Mastercard", self)
    self.radio3 = QRadioButton("Gift Card", self)
    self.radio4 = QRadioButton("In-Store", self)
    self.radio5 = QRadioButton("Online", self)
    self.button_group1 = QButtonGroup(self)
    self.button_group2 = QButtonGroup(self)
    self.initUI()

  def initUI(self):
    self.radio1.setGeometry(0, 0, 400, 50)
    self.radio2.setGeometry(0, 30, 400, 50)
    self.radio3.setGeometry(0, 60, 400, 50)
    self.radio4.setGeometry(0, 90, 400, 50)
    self.radio5.setGeometry(0, 120, 400, 50)

    # set styles for all radio buttons
    self.setStyleSheet("QRadioButton{"
                       "font-size: 16px;"
                       "font-family: Arial;"
                       "font-weight: bold;"
                       "padding: 10px;"
                       "}")
    
    # Group radios 1–3 together so only one can be selected at a time
    # This group is independent from radios 4–5
    self.button_group1.addButton(self.radio1)
    self.button_group1.addButton(self.radio2)
    self.button_group1.addButton(self.radio3)

    # Group radios 4–5 together so only one can be selected at a time
    self.button_group2.addButton(self.radio4)
    self.button_group2.addButton(self.radio5)

    # Connect all radio buttons to a single handler method
    self.radio1.toggled.connect(self.radio_checked)
    self.radio2.toggled.connect(self.radio_checked)
    self.radio3.toggled.connect(self.radio_checked)
    self.radio4.toggled.connect(self.radio_checked)
    self.radio5.toggled.connect(self.radio_checked)

  # do something when radio button is checked
  def radio_checked(self):
    # sender() returns the widget that sent the signal(radio that was checked).
    # So if we click on radio1, radio_button = self.radio1
    # this makes it so that we don't have to write many if-statements
    # checking which radio button was clicked.
    radio_button = self.sender()
    
    # Only react when the radio button is checked (not unchecked)
    if radio_button.isChecked():
      print(f"{radio_button.text()} has been selected.")


def main():
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec())

if __name__ == '__main__':
  main()