from flask import Flask, request
import urllib.request
import json

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>🌤️ Weather Checker</h1>
    <form action="/weather" method="get">
        <input type="text" name="city" placeholder="Enter a city...">
        <button type="submit">Check Weather</button>
    </form>
    """

@app.route('/weather')
def weather():
    city = request.args.get('city', 'London')
    url = f"https://wttr.in/{city}?format=j1"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
        temp = data['current_condition'][0]['temp_C']
        desc = data['current_condition'][0]['weatherDesc'][0]['value']
        feels = data['current_condition'][0]['FeelsLikeC']
        return f"""
        <h1>Weather in {city.title()}</h1>
        <p>🌡️ Temperature: {temp}°C</p>
        <p>🤔 Feels like: {feels}°C</p>
        <p>☁️ Condition: {desc}</p>
        <a href="/">Search again</a>
        """
    except:
        return f"<p>Couldn't find weather for {city}. <a href='/'>Try again</a></p>"