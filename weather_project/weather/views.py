from django.shortcuts import render, redirect
import requests

def index(request):
    return render(request, 'weather/index.html')

def weather(request):
    if request.method == "POST":
        city = request.POST['city']
        api_key = 'd3211ffe8627fb0a22fe11fd26815698'  # Replace with your OpenWeatherMap API key
        # URL to fetch 5-day weather forecast
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
        
        response = requests.get(url)
        data = response.json()

        if data['cod'] == '200':
            weather_data = {
                'city': city,
                'temperature': data['list'][0]['main']['temp'],  # Current temperature
                'description': data['list'][0]['weather'][0]['description'],  # Weather description
                'icon': data['list'][0]['weather'][0]['icon'],  # Icon for current weather
                'humidity': data['list'][0]['main']['humidity'],  # Humidity
                'pressure': data['list'][0]['main']['pressure'],  # Pressure
                'wind_speed': data['list'][0]['wind']['speed'],  # Wind speed
                'forecast': []  # List for storing next 5 days of weather forecast
            }

            # Extract the forecast for the next 5 days
            for day in range(1, 6):  # Skip the first item, as it's the current weather
                day_forecast = {
                    'date': data['list'][day]['dt_txt'],  # Date and time
                    'temperature': data['list'][day]['main']['temp'],  # Temperature
                    'description': data['list'][day]['weather'][0]['description'],  # Weather description
                    'icon': data['list'][day]['weather'][0]['icon'],  # Icon
                    'humidity': data['list'][day]['main']['humidity'],  # Humidity
                    'wind_speed': data['list'][day]['wind']['speed'],  # Wind speed
                }
                weather_data['forecast'].append(day_forecast)

            # Store weather data in session
            request.session['weather_data'] = weather_data
            request.session.modified = True  # Ensure session is saved immediately
            # Redirect to weather_display page to display data
            return redirect('weather_display')
        else:
            error_message = "City not found or incorrect data entered."
            return render(request, 'weather/index.html', {'error_message': error_message})
    
    # If it's a GET request, render the index page
    return redirect('index')

def weather_display(request):
    # Retrieve weather data from the session
    weather_data = request.session.get('weather_data')
    if weather_data:
        return render(request, 'weather/weather.html', {'weather_data': weather_data})
    else:
        return redirect('index')  # If no data, redirect to the index page
