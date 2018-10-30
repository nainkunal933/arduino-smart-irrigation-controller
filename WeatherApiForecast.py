
class WeatherApiForecast:

    def __init__(self, index1, index2, data):
        global forecast_header
        forecast_header = str((index1 / 8) + 1) + " Day Forecast at 12:00AM: " + "\n"
        global forecast_short_phrase_of_weather_Midnight
        forecast_short_phrase_of_weather_Midnight= "Weather -> " + data['list'][index1]['weather'][0]['main'] + "\n"
        global forecast_weather_description_Midnight
        forecast_weather_description_Midnight= "Description -> " + data['list'][index1]['weather'][0]['description'] + "\n"
        global forecast_weather_temp_Midnight
        forecast_weather_temp_Midnight = "Temperature -> " + str(data['list'][index1]['main']['temp']) + " K" + "\n"
        global forecast_humidity_Midnight
        forecast_humidity_Midnight = "Humidity -> " + str(data['list'][index1]['main']['humidity']) + "%" + "\n"

        global forecast_weather_temp_Midnight_numeric
        forecast_weather_temp_Midnight_numeric = data['list'][index1]['main']['temp']
        global forecast_weather_humidity_Midnight_numeric
        forecast_weather_humidity_Midnight_numeric = data['list'][index1]['main']['humidity']

        global forecast12_header
        forecast12_header = str((index2 / 8) + 0.5) + " Day Forecast at 12:00PM: " + "\n"
        global short12_phrase_of_weather_Noon
        short12_phrase_of_weather_Noon = "Weather -> " + data['list'][index2]['weather'][0]['main'] + "\n"
        global weather12_description_Noon
        weather12_description_Noon = "Description -> " + data['list'][index2]['weather'][0]['description'] + "\n"
        global weather12_temp_Noon
        weather12_temp_Noon = "Temperature -> " + str(data['list'][index2]['main']['temp']) + " K" + "\n"
        global humidity12_Noon
        humidity12_Noon = "Humidity -> " + str(data['list'][index2]['main']['humidity']) + "%" + "\n"

        global forecast_weather_temp_Noon_numeric
        forecast_weather_temp_Noon_numeric = data['list'][index2]['main']['temp']
        global forecast_weather_humidity_Noon_numeric
        forecast_weather_humidity_Noon_numeric = data['list'][index2]['main']['humidity']

    def weatherDataPrintMidnight(self):
        # Forecast: Midnight
        return forecast_header + forecast_short_phrase_of_weather_Midnight + forecast_weather_description_Midnight + forecast_weather_temp_Midnight + forecast_humidity_Midnight

    def weatherDataPrintNoon(self):
        # Forecast: Noon
        return forecast12_header + short12_phrase_of_weather_Noon + weather12_description_Noon + weather12_temp_Noon + humidity12_Noon

    def getForecastTemperatureMidnight(self):
        return forecast_weather_temp_Midnight_numeric

    def getForecastTemperatureNoon(self):
        return forecast_weather_temp_Noon_numeric

    def getForecastHumidityMidnight(self):
        return forecast_weather_humidity_Midnight_numeric

    def getForecastHumidityNoon(self):
        return forecast_weather_humidity_Noon_numeric

