# Weather App

import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt


class Weather(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Weather App')
        self.setGeometry(700, 300, 700, 500)
        self.setWindowIcon(QIcon('/home/ibrahim/python/basic-programs/programs/weather-app/sun.png'))
        self.input = QLineEdit(self)
        self.but = QPushButton("Get Weather", self)
        self.weather_data = QLabel("", self)
        self.weather_icon = QLabel("", self)
        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout()
        self.setLayout(vbox)

        hbox = QHBoxLayout()
        hbox.addWidget(self.input)
        hbox.addWidget(self.but)

        vbox.addLayout(hbox)
        vbox.addWidget(self.weather_data)
        vbox.addWidget(self.weather_icon)

        self.weather_data.setAlignment(Qt.AlignCenter)
        self.weather_icon.setAlignment(Qt.AlignCenter)

        self.setStyleSheet('''
            QLabel, QPushButton {
                font-weight: bold;
                font-family: Arial;
            }
            QPushButton {
                background-color: hsl(207, 82%, 60%);
                font-size: 24px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: hsl(207, 82%, 70%);
            }
            QLabel {
                font-size: 24px;
            }
            QLineEdit {
                font-size: 24px;
                padding: 5px;
            }
        ''')

        self.but.setCursor(Qt.PointingHandCursor)
        self.input.setPlaceholderText("Enter a city name here")
        # wrap text to next line if it gets too long
        self.weather_data.setWordWrap(True)
        # make text selectable so you can copy it from app
        self.weather_data.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.weather_data.setCursor(Qt.IBeamCursor)

        self.but.clicked.connect(self.get_weather)
    
    def get_weather(self):
        try:
            city = self.input.text().strip().capitalize()

            base_url = f"https://api.weatherapi.com/v1/current.json?key=9d49110062374386a16172306261801&q={city}&aqi=no"

            response = requests.get(base_url)
            response = response.json()

            self.weather_data.setText(
                f"Country: {response["location"]["country"]}, "
                f"Region: {response["location"]["region"]}, "
                f"City: {response["location"]["name"]}, "
                f"Temprature °C: {response["current"]["temp_c"]}, "
                f"Feels Like °C: {response["current"]["feelslike_c"]}, "
                f"LocalTime: {response["location"]["localtime"]}, "
                f"Condition: {response["current"]["condition"]["text"]}"
            )

            # get weather icon
            icon_url = "https:" + response["current"]["condition"]["icon"]
            icon_data = requests.get(icon_url).content

            pixmap = QPixmap()
            pixmap.loadFromData(icon_data)
            pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)

            self.weather_icon.setPixmap(pixmap)
        except KeyError:
            self.weather_icon.clear()
            self.weather_data.setText(f"{city} was not found! Enter a correct city name.")
        except requests.exceptions.ConnectionError:
            self.weather_icon.clear()
            self.weather_data.setText("Connection Error! Check your internet connection.")


def main():
    app = QApplication(sys.argv)
    weather_app = Weather()
    weather_app.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()








# http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=xml