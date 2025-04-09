
#  Weather Forecast App (PyQt5 + OpenWeatherMap)

A simple desktop weather forecast app built with PyQt5 and OpenWeatherMap API.  
It shows a 5-day forecast with clean visuals and color-coded temperature cards.

##  Features

- Displays one forecast per day (at 12:00 PM).
- Shows temperature, weather icon, and description.
- Background color changes based on the temperature.
- Currently set to **Tel Aviv** (can be changed in the code).

##  Interface

Each forecast appears as a card with:
- A weather emoji (☀️ 🌧️ ❄️ etc.)
- Temperature in °C
- Description of the weather

##  Requirements

- Python 3.x  
- Libraries:
  - `PyQt5`
  - `requests`

Install them via pip:
```bash
pip install PyQt5 requests
```

##  Run the App

```bash
python weather_app.py
```

##  API Key

You’ll need an API key from [OpenWeatherMap](https://openweathermap.org/api).  
Replace the placeholder in the `get_data()` method:
```python
API_KEY = "your_api_key_here"
```

---

