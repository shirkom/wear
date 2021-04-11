import requests


def choose_appropriate_clothe(temp_celsuis):
    if temp_celsuis <= 3:
        return 'snow jacket ❄️'
    if 3 < temp_celsuis < 14:
        return 'coat 🧥'
    if 13 < temp_celsuis < 21:
        return 'jacket 🧥'
    if 22 < temp_celsuis < 36:
        return 't-shirt 👕'
    if 35 < temp_celsuis < 45:
        return 'go naked 👙'
    if 45 < temp_celsuis:
        return 'something wrong! 🔥'


def what_should_wear(lat: str, lon: str):
    # url = 'http://ip-api.com/json/' + ip
    # location = requests.get(url).json()
    # lat = str(location['lat'])
    # lon = str(location['lon'])
    APIkey = '2ea7d0757ada5940b267a261f7989430'
    url_weather = 'http://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + lon + '&appid=' + APIkey \
                  + '&units=metric'
    weather = requests.get(url_weather).json()
    temp_celsuis = weather['main']['temp']
    weather_description = weather['weather'][0]['description']
    appropriate_clothe = choose_appropriate_clothe(temp_celsuis)
    return temp_celsuis, weather_description, appropriate_clothe
