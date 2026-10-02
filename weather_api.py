import requests

print("Weather API Application")

city = input("Enter city name: ")

url = f"https://wttr.in/{city}?format=j1"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    current = data["current_condition"][0]

    temperature = current["temp_C"]
    humidity = current["humidity"]
    description = current["weatherDesc"][0]["value"]

    print("\nWeather Details")
    print("----------------")
    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Condition:", description)

else:
    print("Unable to fetch weather data.")
