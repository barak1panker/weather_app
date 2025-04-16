import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PyQt5.QtGui import QFont, QColor, QPalette


city = "tel aviv"
def get_icon(code):
    if code.startswith("01"):
        return "☀️"
    elif code.startswith("02"):
        return "🌤️"
    elif code.startswith("03") or code.startswith("04"):
        return "☁️"
    elif code.startswith("09") or code.startswith("10"):
        return "🌧️"
    elif code.startswith("11"):
        return "⛈️"
    elif code.startswith("13"):
        return "❄️"
    elif code.startswith("50"):
        return "🌫️"
    return "🌈"

def get_color_by_temp(temp):
    if temp < 0:
        return "#003366"
    elif temp < 10:
        return "#6699FF"
    elif temp < 20:
        return "#99CC99"
    elif temp < 30:
        return "#FFD700"
    else:
        return "#FF4500"

class WeatherCard(QWidget):
    def __init__(self, temp, icon, description):
        super().__init__()
        self.setAutoFillBackground(True)

        bg_color = QColor(get_color_by_temp(temp))
        palette = self.palette()
        palette.setColor(QPalette.Window, bg_color)
        self.setPalette(palette)

        layout = QHBoxLayout()
        layout.setContentsMargins(20, 10, 20, 10)

        icon_label = QLabel(icon)
        icon_label.setFont(QFont("Arial", 24))
        layout.addWidget(icon_label)

        desc_label = QLabel(description)
        desc_label.setFont(QFont("Arial", 12))
        desc_label.setStyleSheet("color: white")
        layout.addWidget(desc_label)

        temp_label = QLabel(f"{temp:.0f}°C")
        temp_label.setFont(QFont("Arial", 16))
        temp_label.setStyleSheet("color: white")
        layout.addWidget(temp_label)

        self.setLayout(layout)

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("תחזית מזג אוויר לשבוע")
        self.setGeometry(300, 100, 400, 600)

        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)

        cards = self.get_data()
        for card in cards:
            main_layout.addWidget(card)


        self.setLayout(main_layout)

    def get_data(self):
        API_KEY = "YOUR API KEY"
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric&lang=en"

        response = requests.get(url)
        data = response.json()
        forecast_list = data["list"]

        seen_days = set()
        cards = []

        for entry in forecast_list:
            dt_txt = entry["dt_txt"]
            date = dt_txt.split(" ")[0]

            if date in seen_days:
                continue

            if "12:00:00" in dt_txt:
                temp_c = entry["main"]["temp"]
                cloud = entry["clouds"]["all"]
                description = entry["weather"][0]["description"]
                icon = get_icon(entry["weather"][0]["icon"])

                card = WeatherCard(temp_c, icon, f"{date}: {description}")
                cards.append(card)
                seen_days.add(date)

            if len(cards) >= 5:
                break

        return cards

def main():
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
