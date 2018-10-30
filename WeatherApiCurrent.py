class WeatherApiCurrent:

    def __init__(self, data):
        global current_header
        current_header = "Current Weather: \n"
        global current_short_phrase_of_weather
        current_short_phrase_of_weather = "Weather -> " + data['weather'][0]['main'] + "\n"
        global current_weather_description
        current_weather_description = "Description -> " + data['weather'][0]['description'] + "\n"
        global current_weather_temp
        current_weather_temp = "Temperature -> " + str(data['main']['temp']) + " K" + "\n"
        global current_humidity
        current_humidity = "Humidity -> " + str(data['main']['humidity']) + "%" + "\n"
        global currentTemperature
        currentTemperature = data['main']['temp']
        global currentHumidity
        currentHumidity = data['main']['humidity']

    def weatherDataPrintCurrent(self):
        # Forecast: Midnight
        return current_header + current_short_phrase_of_weather + current_weather_description + current_weather_temp + current_humidity

    def getCurrentTemperature(self):
        return currentTemperature

    def getCurrentHumidity(self):
        return currentHumidity