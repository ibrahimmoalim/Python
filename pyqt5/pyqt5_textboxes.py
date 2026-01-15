# PyQt5 LineEdit (textbox) practice

import sys
# QLineEdit handles text input fields
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    # Configure main window properties
    self.setGeometry(700, 300, 700, 555)
    self.setStyleSheet("font-family: Arial;"
                       "font-size: 16px;"
                       "font-weight: bold;")
    self.setWindowTitle("Textbox Functionality")
    
    # Create widgets
    self.textbox = QLineEdit(self)
    self.button = QPushButton('Enter', self)

    # Initialize UI layout and signals
    self.initUI()
  
  def initUI(self):
    self.textbox.setGeometry(10, 10, 400, 30)
    self.textbox.setPlaceholderText("Type something here!")
    self.button.setGeometry(415, 10, 70, 30)

    # Connect button click to handler method
    self.button.clicked.connect(self.get_textbox_value)

  def get_textbox_value(self):
    # assign the textbox value to 'text' variable
    text = self.textbox.text()

    # Output the text to the console
    print(text)
    

def main():
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec())

if __name__ == '__main__':
  main()