import requests
api_key = "1a782b0dd47504d428893e826f1ab32c"

def pronostico_ciudad():
    ciudad = input("Ingrese el nombre de la ciudad: ")
    url = "https://api.openweathermap.org/data/2.5/forecast?&q=%s&appid=%s&units=metric" % (ciudad, api_key)
    res = requests.get(url)
    data = res.json()
    mostrar_pronostico(data)

def pronostico_por_lat_lan():
    lat = float(input("Ingrese la latitud de la ciudad: "))
    lon = float(input("Ingrese la longitud de la ciudad: "))
    url = "https://api.openweathermap.org/data/2.5/forecast?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
    res = requests.get(url)
    data = res.json()
    mostrar_pronostico(data)

def actual_por_ciudad():
    ciudad = input("Ingrese el nombre de la ciudad: ")
    url = "http://api.openweathermap.org/data/2.5/weather?&q=%s&appid=%s&units=metric" % (ciudad, api_key)
    res = requests.get(url)
    data = res.json()
    mostrar_clima(data)


def actual_por_lat_lan():
    lat = float(input("Ingrese la latitud de la ciudad: "))
    lon = float(input("Ingrese la longitud de la ciudad: "))
    url = "http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s&units=metric"% (lat, lon, api_key)
    res = requests.get(url)
    data = res.json()
    mostrar_clima(data)


def mostrar_clima(data):
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    description = data["weather"][0]["description"]

    print()
    print("Temperatura : {} grados Celsius".format(temp))
    print("Sensación Térmica: {} grados Celsius".format(feels_like))
    print("Humedad: {} %".format(humidity))
    print("Velocidad del viento : {} m/s".format(wind_speed))
    print("Descripción : {}".format(description))

def mostrar_pronostico(data):
    dt_txt = data["list"][0]["dt_txt"]
    temp = data["list"][0]["main"]["temp"]
    feels_like = data["list"][0]["main"]["feels_like"]
    humidity = data["list"][0]["main"]["humidity"]
    weather = data["list"][0]["weather"]
    clouds = data["list"][0]["clouds"]

    print()
    print("Pronóstico para el día: {}".format(dt_txt))
    print("Temperatura: {} grados Celsius".format(temp))
    print("Sensación térmica: {} grados Celsius".format(feels_like))
    print("Humedad: {} %".format(humidity))
    print("Clima: {}".format(weather))
    print("Nubosidad: {} %".format(clouds))


def main():
    print("1. Mostrar clima actual")
    print("2. Mostrar pronóstico")
    print("A. Mostrar clima por ciudad")
    print("B. Mostrar clima por latitud y longitud")
    clima1_2 = input("Ingrese 1 o 2: ")
    climaA_B = input("Ingrese A o B: ")

    if clima1_2 == "1":
        climaA_B
        if climaA_B.upper() == "A":
            actual_por_ciudad()
        else:
            actual_por_lat_lan()
    elif clima1_2 == "2":
        climaA_B
        if climaA_B.upper() == "A":
            pronostico_ciudad()
        else:
            pronostico_por_lat_lan()
    

if __name__ == "__main__":
    main()

