import json
import requests
import urllib.request

from MyHTMLParser import *
from WeatherApiForecast import *
from WeatherApiCurrent import *
import os.path


class ArduinoPortal:

    requestCurrent = requests.get('http://api.openweathermap.org/data/2.5/weather?id=3987342&APPID=d2669a720677f99ab5ac96c0dca9a399')
    requestForecast = requests.get('http://api.openweathermap.org/data/2.5/forecast?id=3987342&APPID=d2669a720677f99ab5ac96c0dca9a399')
    apiDataForecast = json.loads(requestForecast.text)
    apiDataCurrent = json.loads(requestCurrent.text)

    # Generic Information
    name_of_city = "City -> " + apiDataForecast['city']['name']

    # Current Weather Data
    currentWeatherData = WeatherApiCurrent(apiDataCurrent).weatherDataPrintCurrent()

    # Index values for Midnight: 0,8,16,24,32
    # Index values for Noon: 4,12,20,28,36
    firstDayMidnight = WeatherApiForecast(0, 4, apiDataForecast).weatherDataPrintMidnight()
    firstDayNoon = WeatherApiForecast(0, 4, apiDataForecast).weatherDataPrintNoon()

    secondDayMidnight = WeatherApiForecast(8, 12, apiDataForecast).weatherDataPrintMidnight()
    secondDayNoon = WeatherApiForecast(8, 12, apiDataForecast).weatherDataPrintNoon()

    thirdDayMidnight = WeatherApiForecast(16, 20, apiDataForecast).weatherDataPrintMidnight()
    thirdDayNoon = WeatherApiForecast(16, 20, apiDataForecast).weatherDataPrintNoon()

    fourthDayMidnight = WeatherApiForecast(24, 28, apiDataForecast).weatherDataPrintMidnight()
    fourthDayNoon = WeatherApiForecast(24, 28, apiDataForecast).weatherDataPrintNoon()

    fifthDayMidnight = WeatherApiForecast(32, 36, apiDataForecast).weatherDataPrintMidnight()
    fifthDayNoon = WeatherApiForecast(32, 36, apiDataForecast).weatherDataPrintNoon()

    weatherData = name_of_city + "\n" + currentWeatherData + "\n" + firstDayMidnight + "\n" + firstDayNoon + "\n" + secondDayMidnight + "\n" + secondDayNoon + "\n" + thirdDayMidnight + "\n" + thirdDayNoon + "\n" + fourthDayMidnight + "\n" + fourthDayNoon + "\n" + fifthDayMidnight + "\n" + fifthDayNoon
    fileName = 'WeatherData.txt'
    filePath = 'Upload/'
    completename = os.path.join(filePath, fileName)
    file = open(completename, 'w+')
    file.write(weatherData)
    file.close()

    contents = urllib.request.urlopen("http://172.20.10.3").read()      # Getting data from arduino
    print(contents)
    print("Pre Parser: ", contents)
    parser = MyHTMLParser()
    parser.feed(str(contents))

    humiditySensor = dataList[3]
    temperatureSensor = dataList[4]
    moistureSensor = dataList[5]

    humiditySensorList = humiditySensor.split()
    humiditySensorValue = humiditySensorList[1]

    temperatureSensorList = temperatureSensor.split()
    temperatureSensorValue = temperatureSensorList[1]

    moistureSensorList = moistureSensor.split()
    moistureSensorValue = moistureSensorList[2]

    print(humiditySensorValue)
    print(temperatureSensorValue)
    print(moistureSensorValue)
    #
    #
    # All Watering will occur at 12 pm
    # First check: Current Soil Moisture
    # moisture threshold :
    #       Min  Typ  Max  Condition
    # #       0    0    0    sensor in open air
    # #       0    20   300  sensor in dry soil
    # #       300  580  700  sensor in humid soil
    # #       700  940  950  sensor in water
    # Writing max values can change upon testing
    moistureDiscrepencyBoolLow = False
    moistureDiscrepencyBoolHigh = False
    if int(moistureSensorValue) < 300:
        print("Soil Moisture Value is too low: Water plants")
        mositureSensorDecision1 = "Soil Moisture Value is too low: Water plants"
        moistureSensorDiscrepancyBoolLow = True
    elif int(moistureSensorValue) > 580:
        print("Soil Moisture Value is too high: Don't Water Plants")
        mositureSensorDecision2 = "Soil Moisture Value is too high: Don't Water Plants"
        moistureDiscrepencyBoolHigh = True

    # Second check: Current Sensor value vs API value
    temperatureDiscrepencyBoolHigh = False
    temperatureDiscrepencyBoolLow = False
    humidityDiscrepencyBoolHigh = False
    humidityDiscrepencyBoolLow = False
    # curData = WeatherApiCurrent(apiDataCurrent)
    # if abs(temperatureSensorValue - curData.getCurrentTemperature()) > 5:
    #     print("Current Temperature Discrepency")
    #     temperatureDiscrepencyBool = True
    # if abs(humiditySensorValue - curData.getCurrentHumidity()) > 10:
    #     print("Current Humidity Discrepency")
    #     humidityDiscrepencyBool = True

    # Third Check: current temperature determines if too hot or cold to water RIGHT NOW
    # temperature  Threshold = 10C (less than this is too cold dont water)  > 30C Water its too hot;
    currentData = WeatherApiCurrent(apiDataCurrent)
    forecastData1 = WeatherApiForecast(0, 4, apiDataForecast)
    forecastData2 = WeatherApiForecast(8, 12, apiDataForecast)
    forecastData3 = WeatherApiForecast(16, 20, apiDataForecast)
    forecastData4 = WeatherApiForecast(24, 28, apiDataForecast)
    forecastData5 = WeatherApiForecast(32, 36, apiDataForecast)


    # 4 more instantiation here

    if float(temperatureSensorValue) > 30.00 or forecastData1.getForecastTemperatureMidnight() > 30 or forecastData1.getForecastTemperatureNoon() > 30 or forecastData2.getForecastTemperatureMidnight() > 30 or forecastData2.getForecastTemperatureNoon() > 30 or forecastData3.getForecastTemperatureMidnight() > 30 or forecastData3.getForecastTemperatureNoon() > 30:
        print("Water Plants Today")
        temperatureSensorDecision1 = "Water Plants"
        temperatureDiscrepencyBoolHigh = True
    elif temperatureSensorValue < 10 or forecastData1.getForecastTemperatureMidnight() < 10 or forecastData1.getForecastTemperatureNoon() < 10 or forecastData2.getForecastTemperatureMidnight() < 10 or forecastData2.getForecastTemperatureNoon() < 10 or forecastData3.getForecastTemperatureMidnight() < 10 or forecastData3.getForecastTemperatureNoon() < 10:
        print("Too Cold Don't Water Plants")
        temperatureSensorDecision2 = "Too Cold Don't Water Plants"
        temperatureDiscrepencyBoolLow = True

    # Fourth Check: Humidity
    # humidity threshold = >70% dont water or <20% DO water ;
    if float(humiditySensorValue) > 70.00 or forecastData1.getForecastHumidityMidnight() > 70 or forecastData1.getForecastHumidityNoon() > 70:
        print("Too Huimid, Don't Water Plants")
        humiditySensorDecision1 = "Too Humid, Don't Water Plants"
        humidityDiscrepencyBoolHigh = True
    elif humiditySensorValue < 20 or forecastData1.getForecastHumidityMidnight() < 20 or forecastData1.getForecastHumidityNoon() < 20:
        print("Too Dry, Water Plants Today")
        humiditySensorDecision2 = "Too Dry, Water Plants Today"
        humidityDiscrepencyBoolLow = True
    # today's temperature is used to check and make sure our previous predictions held true
    # future temperature should determine when to water plants,
    # but dont actually water plants until current temperature verafies

    if moistureDiscrepencyBoolHigh == True:
        decision = mositureSensorDecision2
    elif moistureDiscrepencyBoolLow == True:
        decision = mositureSensorDecision1
    elif temperatureDiscrepencyBoolHigh == True:
        decision = temperatureSensorDecision1
    elif temperatureDiscrepencyBoolLow == True:
        decision = temperatureSensorDecision2
    elif humidityDiscrepencyBoolHigh == True:
        decision = humiditySensorDecision1
    elif humidityDiscrepencyBoolLow == True:
        decision = humiditySensorDecision2



    fileName = 'API_Decision.txt'
    filePath = 'Upload/'
    completename = os.path.join(filePath, fileName)
    file = open(completename, 'w+')
    file.write(decision)
    file.close()