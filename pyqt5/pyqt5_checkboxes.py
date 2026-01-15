# Working with checkboxes using qt5

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 700, 555)
        self.setWindowTitle("Working with app checkboxes practice")
        # create a checkbox
        self.checkbox = QCheckBox("Are you doing good?", self)
        self.label = QLabel("", self)
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(10, 0, 400, 50)
        self.checkbox.setStyleSheet("font-size: 24px;"
                                    "font-weight: bold;"
                                    "font-family: Arial;")
        
        # set the checkbox to be unchecked when app starts
        # this is by default so below code is not needed (i put it here for reference)
        self.checkbox.setChecked(False)

        self.label.setGeometry(10, 100, 300, 50)
        self.label.setStyleSheet("font-size: 24px;"
                                    "font-weight: bold;"
                                    "font-family: Arial;")
        
        # setup onclick functionality for checkbox
        # self.checkbox.clicked.connect(self.checkbox_checked)

        self.checkbox.stateChanged.connect(self.checkbox_changed)
    
    # do something when checkbox is checked(clicked)
    def checkbox_checked(self):
        
        # if checkbox is checked(clicked)
        if self.checkbox.isChecked():
            # change label text
            self.label.setText("You're doing good lad.")
        else:
            self.label.setText("")
    
    def checkbox_changed(self, state):
        # print(state) # if state = 2 => checkbox is checked, if state = 0 => unchecked
        # print(Qt.Checked) # 2

        # if state == 2:
        if state == Qt.Checked:
            self.label.setText("You're doing good lad.")
        # elif state == 0:
        else:
            self.label.setText("")
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
  main()