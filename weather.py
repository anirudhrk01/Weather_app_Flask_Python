from flask import Flask,request,render_template
import requests

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def weather_info():
    lat, lon = None, None
    if request.method=='POST':
      api_key = "436ac2860e3609b1a8191b05153947ab"
      lat=request.form.get('latitude')  
      lon=request.form.get('longitude') 

      url=f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
      print(url)
      response=requests.get(url)

      if response.status_code==200:
              weather_data=response.json()
              return render_template('index.html',latitude=lat, longitude=lon, weather_data=weather_data)
      else:
              return render_template("index.html", error="Unable to fetch weather data")

    return render_template("index.html",latitude=lat,longitude=lon)

app.run()