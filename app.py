import requests
from twilio.rest import Client

account_sid = ["your account sid from twilio"]
auth_token = ["your auth token"]
OW_API = "https://api.openweathermap.org/data/2.5/onecall?lat=25.789801&lon=73.327797&exclude=current,minutely,daily&appid={your_api_key}


response = requests.get(url= OW_API)
weather_data = response.json()
weather_data = weather_data["hourly"]
will_rain = False

for i in range(0, 12):
    data = int(weather_data[i]["weather"][0]["id"])

    if data < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_='senders number',
        to='reciver number'
    )
    print(message.status)