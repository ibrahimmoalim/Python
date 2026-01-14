# PyQt5 GUI (Graphical User Interface) Introduction

# The sys module provides access to Python interpreter variables and functions,
# such as command-line arguments and exit handling. It is part of Python’s standard library.
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
# work with window icons and fonts
from PyQt5.QtGui import QIcon, QFont
# 'Qt' class is used for alignments like text centring
from PyQt5.QtCore import Qt


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

      # add text to the window, like html paragraph
      label = QLabel('Hi lad!', self)
      # change position of text (x, y)
      # label.move(0, 0)
      # or change position and text-size once with .setGeometry(x, y, width, height)
      label.setGeometry(0, 0, 700, 555)
      # change font and font-size
      label.setFont(QFont('Arial', 24))
      # use styles similar to css styles
      label.setStyleSheet("color: red;" # you could use rgb(255, 0, 0)
                          # rgba for transparency, a = alpha (0-255) or (0-1)
                          "background-color: rgba(0, 0, 255, 0.2);" # you could just use 'lightblue' without ''
                          "font-weight: bold;"
                          "font-style: italic;"
                          "text-decoration: underline;")
        # Alignments/positioning
      # label.setAlignment(Qt.AlignTop) # align to the top of it's sized block (you can tell it's block (amount of space it takes) by giving it background-color)
      # label.setAlignment(Qt.AlignBottom) # align to the bottom of it's sized block
      label.setAlignment(Qt.AlignVCenter) # align to the center(V = Vertical) of it's sized block (default)

      # label.setAlignment(Qt.AlignRight) # align to the right of it's sized block
      # label.setAlignment(Qt.AlignLeft) # align to the left of it's sized block
      label.setAlignment(Qt.AlignHCenter) # align to the center(H = Horizontal) of it's sized block (default)

      # combine both horizontal and vertical positioning with "|" ( "|" allows us to combine flags)
      label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # top vertically and horizontally centered
      # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # fully centered
      # shortcut for fully centring text
      label.setAlignment(Qt.AlignCenter) # fully centered
      


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