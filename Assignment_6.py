import requests

def weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=fdf07437a1bedbdf0089ba3d9d1744d8&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        print("\n--- Weather Report ---")
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Feels Like: {data['main']['feels_like']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Pressure: {data['main']['pressure']} hPa")
        print(f"Weather: {data['weather'][0]['description']}")
        print(f"Wind Speed: {data['wind']['speed']} m/s")

    except requests.exceptions.RequestException as e:
        print("Error:", e)

city = input("Enter city name: ")
weather_data(city)