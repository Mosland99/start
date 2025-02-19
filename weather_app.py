from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your OpenWeatherMap API key
API_KEY = "b589bf07fdcccfb9d127da7fdb95de49"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    error_message = None

    if request.method == "POST":
        city = request.form["city"]
        if city:
            response = requests.get(
                BASE_URL,
                params={
                    "q": city,
                    "appid": API_KEY,
                    "units": "imperial"  # Use "metric" for Celsius
                }
            )

            # Debugging: Print the response to the console
            print(response.status_code)
            print(response.json())  # Print the response JSON

            if response.status_code == 200:
                weather_data = response.json()
            else:
                error_message = f"Error fetching weather data: {response.status_code}. Please try again."

    return render_template("index.html", weather_data=weather_data, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)