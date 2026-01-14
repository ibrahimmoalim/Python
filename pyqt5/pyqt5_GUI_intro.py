# PyQt5 GUI (Graphical User Interface) Introduction

# The sys module provides access to Python interpreter variables and functions,
# such as command-line arguments and exit handling. It is part of Python’s standard library.
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
# work with window icons like app icon on taskbar(QIcon), fonts(QFont) and images(QPixmap)
# 'QPixmap' class is used for handling images and provides functionality for loading,
# manipulating and displaying images
from PyQt5.QtGui import QIcon, QFont, QPixmap
# 'Qt' class is used for alignments like text and image centring
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
      self.setGeometry(700, 300, 600, 500)
      # set icon image (make the path absolute if relative path doesn't work)
      self.setWindowIcon(QIcon("/home/ibrahim/python/pyqt5/face.png"))

          # add text to the app, like html paragraph
      text = QLabel('Hi lad!', self)
      # change position of text (x, y)
      # text.move(0, 0)
      # or change position and text-size once with .setGeometry(x, y, width, height)
      text.setGeometry(0, 0, self.width(), self.height())
      # change font and font-size
      text.setFont(QFont('Arial', 24))
      # use styles similar to css styles
      text.setStyleSheet("color: black;" # you could use rgb(255, 0, 0)
                          # rgba for transparency, a = alpha (0-255) or (0-1)
                          "background-color: rgba(255, 255, 255, 1);" # you could just use 'lightblue' without ''
                          "font-weight: bold;"
                          "font-style: italic;"
                          "text-decoration: none;") # use underline or anyother decoration
        # Alignments/positioning
      # text.setAlignment(Qt.AlignTop) # align to the top of it's sized block (you can tell it's block (amount of space it takes) by giving it background-color)
      # text.setAlignment(Qt.AlignBottom) # align to the bottom of it's sized block
      text.setAlignment(Qt.AlignVCenter) # align to the center(V = Vertical) of it's sized block (default)

      # text.setAlignment(Qt.AlignRight) # align to the right of it's sized block
      # text.setAlignment(Qt.AlignLeft) # align to the left of it's sized block
      text.setAlignment(Qt.AlignHCenter) # align to the center(H = Horizontal) of it's sized block (default)

      # combine both horizontal and vertical positioning with "|" ( "|" allows us to combine flags)
      text.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # top vertically and horizontally centered
      # text.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # fully centered
      # shortcut for fully centring text
      # text.setAlignment(Qt.AlignCenter) # fully centered

          # Add images to the app
      image = QLabel(self)
      # set image position (x, y) and size (width, height)
      image.setGeometry(300, 50, 100, 100)
      # load image
      pixmap = QPixmap("/home/ibrahim/python/pyqt5/face.png")
      # display image
      image.setPixmap(pixmap)
      # enable correct scaling
      image.setScaledContents(True)

      # self.width() => window width = 700, so 700 - 100(image width) = 600 (horizontal position)
      # self.height() => window height = 550, so 550 - 100(image height) = 450 (vertical position)
      # this would put the image at the bottom left of app screen
      image.setGeometry(self.width() - image.width(),
                        self.height() - image.height(),
                        image.width(),
                        image.height())
      # to fully center the image to the starting window size of the app
      # do window size - image size / 2 (use // to avoid float result)
      # for both width and height of the image
      image.setGeometry((self.width() - image.width()) // 2,
                        (self.height() - image.height()) // 2,
                        image.width(),
                        image.height())


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