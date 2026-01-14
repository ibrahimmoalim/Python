# PyQt5 GUI (Graphical User Interface) Introduction

# The sys module provides access to Python interpreter variables and functions,
# such as command-line arguments and exit handling. It is part of Python’s standard library.
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
# work with window icons
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
      # initializes the parent 'QMainWindow'
      super().__init__()
      # set window title
      self.setWindowTitle("My first GUI")
      # Sets the window position (x, y) and size (width, height) in pixels.
      # first 2 parameters are x(horizontal) position of window/app on screen
      # and y(vertical) respectively, the 3rd and 4th params are for size (width, height) respectively
      self.setGeometry(700, 300, 700, 550)
      # set icon image (make the path absolute if relative path doesn't work)
      self.setWindowIcon(QIcon("/home/ibrahim/python/pyqt5/face.png"))


def main():
  # Create the application object and pass command-line arguments with the help of 'sys.argv'
  app = QApplication(sys.argv)
  # create the main application window
  window = MainWindow()
  # make the window appear on screen
  window.show()
  # Start the Qt event loop and exit the program cleanly when the application closes
  sys.exit(app.exec())


if __name__ == "__main__":
  main()