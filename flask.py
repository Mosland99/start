from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your OpenWeatherMap API key
API_KEY = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def main():
    weather_data = None
    error_message = None

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            params = {
                "q": city,
                "appid": API_KEY,
                "units": "metric"  # Celsius
            }

            # Make the request to OpenWeatherMap
            response = requests.get(BASE_URL, params=params)
            data = response.json()

            if data["cod"] == 200:
                weather_data = {
                    "city": city,
                    "temperature": data["main"]["temp"],
                    "description": data["weather"][0]["description"],
                    "humidity": data["main"]["humidity"],
                    "wind_speed": data["wind"]["speed"]
                }
            else:
                error_message = data.get("message", "Could not retrieve weather data.")

    return render_template("index.html", weather_data=weather_data, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)