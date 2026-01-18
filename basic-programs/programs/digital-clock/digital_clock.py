# Digital Clock Program

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer, QTime, Qt


# Inheriting from QWidget to create a lightweight main window for a simple GUI program
class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Digital Clock')
        self.setGeometry(700, 300, 300, 100)
        self.setWindowIcon(QIcon('/home/ibrahim/python/basic-programs/digital_clock/digital_clock.png'))
        # setup text to desplay time
        self.time_label = QLabel(self)
        # Create a QTimer object to schedule code execution at timed intervals.
        # The timer emits a timeout signal after a specified amount of time has passed.
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        # setup a layout manager
        vbox = QVBoxLayout()
        # add our label(text) to the layout manager
        vbox.addWidget(self.time_label)
        # apply layout
        self.setLayout(vbox)

        # align the text to center of screen
        self.time_label.setAlignment(Qt.AlignCenter)
        # give text a class name 'time' to style later
        self.time_label.setProperty('class', 'time')

        # access class by calling parent widget name and the class
        # e.g. QLabel[class='time']
        self.setStyleSheet('''
                           
            QLabel[class='time'] {
                font-size: 150px;
                font-weight: bold;
                font-family: Arial;
                color: lime;
            }
            
            QWidget {
                background-color: black;
            }
                           
        ''')

        # call time function to display time
        self.update_time()

        # Connect the timer's timeout signal to the update_time method,
        # so the clock updates automatically at regular intervals
        self.timer.timeout.connect(self.update_time)
        # Start the timer to trigger every 1000 milliseconds (1 second),
        # allowing the clock to run in real time and update once per second
        self.timer.start(1000)

    def update_time(self):
        # get the current time in a string format hour:min:sec (AP displays AM/PM)
        current_time = QTime.currentTime().toString('hh:mm:ss AP')
        # make our text show time
        self.time_label.setText(current_time)

def main():
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()