# Making buttons with qt5

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 700, 555)
        self.setWindowTitle("Working with app buttons practice")
        self.button = QPushButton("click me!", self)
        self.cilcked_count = 0 # counts how many times button has been clicked
        self.label = QLabel("hello, good day to ya!", self)
        self.initUI()
    
    def initUI(self):
        self.button.setGeometry(100, 50, 100, 50)
        self.button.setStyleSheet("font-size: 16px;"
                             "font-weight: bold;")
        # setup onclick attribute and wait for button to be 'clicked'
        # then 'connect' the click to an action '(self.on_click)'
        # this will run the on_click() function below
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(200, 0, 300, 50)
        self.label.setStyleSheet("font-size: 24px;"
                                 "font-weight: bold;")
        
    # do something when button is clicked on
    def on_click(self):
        self.cilcked_count += 1
        print('button was clicked')
        print(self.button.text())


        if self.button.text() == 'clicked!':
          self.button.setText("click me!")
          self.label.setText("Freeeedoooom!!!")
        else:
           self.button.setText("clicked!")
           self.label.setText("You're doing good lad.")
        
        # if button is clicked more than 3 times, disable button
        if self.cilcked_count > 3:
          self.button.setDisabled(True)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
  main()