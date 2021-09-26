import requests
import json

key = 'AIzaSyBocINofpRwo_-kC0pDQ6FD_mxKa29UU8o'
latitude = -25.18414486
longitude = 125.92395378


# Basically the whole task without the front-end
def get_elevation():
    if 91 > latitude > -91 and 181 > longitude > -181:
        elevation_url = "https://maps.googleapis.com/maps/api/elevation/json?locations={latitude}%2C{longitude}" \
                        "&key={key}".format(latitude=str(latitude), longitude=str(longitude), key=key)

        payload = {}
        headers = {}

        response = requests.request("GET", elevation_url, headers=headers, data=payload)
        read = json.loads(response.text)

        # This returns the elevation, use it however you see as good
        return read['results'][0]['elevation']
    else:
        return "Please follow the constrictions [-90:90] for latitude and [-180:180] for longitude!"


if __name__ == "__main__":
    print(get_elevation())
    print("You are stupid, indeed...")
