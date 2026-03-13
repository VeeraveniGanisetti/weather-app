import requests
from django.shortcuts import render

def home(request):

    data = None

    if request.method == "POST":
        city = request.POST.get("city")

        api_key = "6bf203d120b7150ada22cc32b97ae96f"

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)
        weather = response.json()

        if response.status_code == 200:
            data = {
                "city": weather["name"],
                "temperature": weather["main"]["temp"],
                "humidity": weather["main"]["humidity"],
                "description": weather["weather"][0]["description"]
            }

    return render(request, "index.html", {"data": data})