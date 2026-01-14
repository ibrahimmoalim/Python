# PyQt5 layouts

import sys
# QMainWindow => the main application window
# QLabel => displays text or images
# QWidget => a generic container widget
# QVBoxLayout ≈ CSS Flexbox (column)
# QHBoxLayout ≈ CSS Flexbox (row)
# QGridLayout ≈ CSS Grid
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget,
                              QVBoxLayout, QHBoxLayout, QGridLayout)

class MainWindow(QMainWindow):
    def __init__(self):
      super().__init__()
      self.setGeometry(700, 300, 700, 555)
      self.setWindowTitle("App layout practice")
      self.initUI()
    
    # anything that deals with UI (User Interface) we write in this function
    # to keep code organized and clean
    def initUI(self):
      # In PyQt, a widget is a UI element. Widgets can be visible (like labels and buttons)
      # or act as invisible containers for layouts and other widgets.
      # Create the main container widget and store it in the 'central_widget' variable
      central_widget = QWidget()

      # Set this widget as the central (main) widget of the QMainWindow.
      # All layouts and child widgets will be placed inside this container.
      self.setCentralWidget(central_widget)


      # Create some label widgets (visual blocks)
      label1 = QLabel("Grid 1", self)
      label2 = QLabel("Grid 2", self)
      label3 = QLabel("Grid 3", self)
      label4 = QLabel("Grid 4", self)
      label5 = QLabel("Grid 5", self)

      # add background colorsto make grids show
      label1.setStyleSheet("background-color: rgba(255, 0, 0, 0.5)")
      label2.setStyleSheet("background-color: rgba(0, 255, 0, 0.5)")
      label3.setStyleSheet("background-color: rgba(0, 0, 255, 0.5)")
      label4.setStyleSheet("background-color: rgba(255, 0, 255, 0.5)")
      label5.setStyleSheet("background-color: rgba(255, 255, 0, 0.5)")
      
      # Create a vertical layout (QVBoxLayout).
      # A vertical layout automatically arranges child widgets
      # from top to bottom inside the parent widget.
      vbox = QVBoxLayout()

      # vbox.addWidget(label1)
      # vbox.addWidget(label2)
      # vbox.addWidget(label3)
      # vbox.addWidget(label4)
      # vbox.addWidget(label5)

      # Apply layout
      # central_widget.setLayout(vbox)

      # Create a horizontal layout (QHBoxLayout).
      # A horizontal layout automatically arranges child widgets
      # from top to bottom inside the parent widget.
      hbox = QHBoxLayout()

      # hbox.addWidget(label1)
      # hbox.addWidget(label2)
      # hbox.addWidget(label3)
      # hbox.addWidget(label4)
      # hbox.addWidget(label5)

      # Apply layout
      # central_widget.setLayout(hbox)

      # Create a grid layout (QGridLayout).
      # A grid layout takes arguments (label, row, column)
      # 0 = row 1 or column 1 (it's like how index works, we count from 0)
      grid = QGridLayout()

      grid.addWidget(label1, 0, 0) # row 1, column 1
      grid.addWidget(label2, 1, 1) # row 2, column 2
      grid.addWidget(label3, 2, 0) # row 3, column 1
      grid.addWidget(label4, 3, 1) # row 4, column 2
      grid.addWidget(label5, 4, 0) # row 5, column 1

      # Apply layout
      central_widget.setLayout(grid)

def main():
   app = QApplication(sys.argv)
   window = MainWindow()
   window.show()
   sys.exit(app.exec())

if __name__ == '__main__':
  main()