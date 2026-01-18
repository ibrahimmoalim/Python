# Stopwatch
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QHBoxLayout, QVBoxLayout, QPushButton)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QTimer, QTime


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Stopwatch')
        self.setGeometry(100, 750, 150, 150)
        self.setWindowIcon(QIcon("/home/ibrahim/python/basic-programs/programs/stopwatch/stopwatch.jpg"))
        self.label = QLabel("00:00:00.00",self)
        self.start = QPushButton("Start", self)
        self.stop = QPushButton("Stop", self)
        self.reset = QPushButton("Reset", self)
        # set base time hour:min:sec:millisec
        self.time = QTime(0, 0, 0, 0)
        # setup a timer event
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        self.setLayout(vbox)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start)
        hbox.addWidget(self.stop)
        hbox.addWidget(self.reset)
        # add the horizontal layout as a row inside the vertical layout
        vbox.addLayout(hbox)

        self.label.setAlignment(Qt.AlignCenter)

        # make cursor pointer
        self.start.setCursor(Qt.PointingHandCursor)
        self.stop.setCursor(Qt.PointingHandCursor)
        self.reset.setCursor(Qt.PointingHandCursor)

        self.setStyleSheet('''
            QPushButton, QLabel {
                font-weight: bold;
                font-family: calibri;
                border-radius: 15px;
            }
            QPushButton {
                font-size: 24px;
                border: 2px solid black;
                padding: 10px 16px;
                background-color: hsl(135, 84%, 63%)
            }
            QPushButton:hover {
                background-color: hsl(135, 84%, 73%)
            }
            QLabel {
                background-color: lightblue;
                font-size: 100px;
            }
        ''')

        self.start.clicked.connect(self.start_stop_watch)
        self.stop.clicked.connect(self.stop_stop_watch)
        self.reset.clicked.connect(self.reset_stop_watch)
        
        # start timer event, and update every 1000ms(1sec)
        self.timer.timeout.connect(self.update_time)
    
    def start_stop_watch(self):
        self.timer.start(10)

    def stop_stop_watch(self):
        self.timer.stop()

    def reset_stop_watch(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.label.setText("00:00:00.00")
    
    def format_time(self, time):
        hour = time.hour()
        min = time.minute()
        sec = time.second()
        # divide msec by 10 to get 2 digits only (// is used to not get float numbers)
        msec = time.msec() // 10

        return f"{hour:02}:{min:02}:{sec:02}.{msec:02}"

    def update_time(self):
        self.time = self.time.addMSecs(10)
        self.label.setText(self.format_time(self.time))



def main():
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()