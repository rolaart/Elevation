import requests
import json
from flask import Flask, render_template
from key import key


# Basically the whole task without the front-end
def get_elevation(latitude=0.0, longitude=0.0):
    if 91 > latitude > -91 and 181 > longitude > -181:
        elevation_url = "https://maps.googleapis.com/maps/api/elevation/json?locations={latitude}%2C{longitude}" \
                        "&key={key}".format(latitude=str(latitude), longitude=str(longitude), key=key)

        payload = {}
        headers = {}

        response = requests.request("GET", elevation_url, headers=headers, data=payload)
        read = json.loads(response.text)

        # This returns the elevation, use it however you see as good
        return str(read['results'][0]['elevation'])
    else:
        return "Please follow the constrictions [-90:90] for latitude and [-180:180] for longitude!"


# And this is the front-end. Not much but works
app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/sendRequest/<string:coordinates>")
def func(coordinates):
    coordinates = coordinates.split(",")
    return "<p>The elevation is: {}</p>".format(get_elevation(float(coordinates[0]), float(coordinates[1])))


if __name__ == "__main__":
    app.run(debug=True)
    print(get_elevation())
