from flask import Flask, render_template
import requests
import geocoder

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/four')
def two2():
    RAIN = 100000
    INCHES = 0
    link = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&appid={}".format(
        lat, lon, api_key)
    data = requests.get(link)
    data = data.json()
    for i in data["daily"]:
        try:
            print(i["rain"])
            RAIN += 27154*i["rain"]
            INCHES+=i["rain"]
        except:
            pass
    USAGE = RAIN*0.00001
    return render_template('four.html', inch=INCHES, rain = RAIN, usage=USAGE)

@app.route('/<string:name>')
def two(name):
    return render_template(name  + '.html')


g = geocoder.ip('me')
lat, lon = g.latlng
api_key = "3bb8aadaa3f8d3fd4a54f576f1945112"
link = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(
    lat, lon, api_key)
data = requests.get(link)
data = data.json()
print(data)


RAIN = 100000
link = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&appid={}".format(lat, lon, api_key)
data = requests.get(link)
data = data.json()
for i in data["daily"]:
    try:
        print(i["rain"])
        RAIN += 27154*i["rain"]
    except: 
        pass
# humidity = data['main']['humidity']

if __name__ == '__main__':
    app.run(port=5000, debug=True)
