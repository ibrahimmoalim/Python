# PyQt5 Styles

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QGridLayout

class MainWindow(QMainWindow):
    def __init__(self):
      super().__init__()
      self.setGeometry(700, 300, 700, 555)
      self.setWindowTitle("PyQt5 Styles")
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
      # give a class name (column1) to labels(1,3,5), so we can style them specifically later
      label1.setProperty('class', 'column1')
      label2 = QLabel("Grid 2", self)
      label3 = QLabel("Grid 3", self)
      label3.setProperty('class', 'column1')
      label4 = QLabel("Grid 4", self)
      label5 = QLabel("Grid 5", self)
      label5.setProperty('class', 'column1')

      # you can set style for an entire widget like 'QLabel'
      # or style a specific class
      # hsl(137, 79%, 66%) , hsl is a way to describe colors using three values:
      # hsl = hue, saturation, lightness
      # hue is color type, 137 falls in the green range
      # saturation is how intense or vivid the color is, 79% means quite strong
      # lightness is how light or dark color is, 0%=black, 50%=normal, 100%=white
      # hsl coloring is great for python programs because the 'opacity' styling feature in CSS
      # is not available here, so when we do (class):hover, increase the lightness 10%
      # e.g. hsl(137, 79%, 66%) --> hsl(137, 79%, 76%) , goes from light-green to lighter-green
      self.setStyleSheet("""

          QLabel {
                background-color: hsl(137, 79%, 66%);
                border-radius: 10px;
                padding-left: 10px;
                font-size: 20px;
                font-weight: bold;
                font-family: Arial;
                border: 2px solid blue;
          }
                         
          QLabel:hover {
                    background-color: hsl(137, 79%, 76%);
          }
                         
          
          QLabel[class="column1"] {
                background-color: hsl(183, 78%, 73%);
                font-family: Sans;
                color: purple;
                border: 2px solid red;
          }
                         
          QLabel[class="column1"]:hover {
                background-color: hsl(183, 78%, 83%);
          }               
          
          
      """)
      
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