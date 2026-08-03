import requests

api_key = "ed3367e70276d6ae1d9f860a5174ed43"
api_url = f"https://api.weatherstack.com/current?access_key={api_key}&query=Bangkok"

def fetch_data():
    print("Fetching weather data from weatherstack API...")
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("API response received successfully.")
        print(response.json())

    except request.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        raise

#fetch_data()

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'Bangkok, Thailand', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'Bangkok', 'country': 'Thailand', 'region': 'Krung Thep', 'lat': '13.750', 'lon': '100.517', 'timezone_id': 'Asia/Bangkok', 'localtime': '2026-07-25 15:01', 'localtime_epoch': 1784991660, 'utc_offset': '7.0'}, 'current': {'observation_time': '08:01 AM', 'temperature': 35, 'weather_code': 116, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0002_sunny_intervals.png'], 'weather_descriptions': ['Partly Cloudy '], 'astro': {'sunrise': '06:01 AM', 'sunset': '06:48 PM', 'moonrise': '03:31 PM', 'moonset': '02:04 AM', 'moon_phase': 'Waxing Gibbous', 'moon_illumination': 81}, 'air_quality': {'co': '209', 'no2': '7', 'o3': '91', 'so2': '4.1', 'pm2_5': '8.4', 'pm10': '13.1', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 15, 'wind_degree': 243, 'wind_dir': 'WSW', 'pressure': 1003, 'precip': 0, 'humidity': 47, 'cloudcover': 25, 'feelslike': 40, 'uv_index': 4, 'visibility': 10, 'is_day': 'yes'}}