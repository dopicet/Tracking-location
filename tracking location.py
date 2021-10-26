# importing modules
import requests
import folium
import os

# geting your ip address from https://ipinfo.io/ using requests.get() method
res = requests.get('https://ipinfo.io/')

# parsing the json content
location_data = res.json()['loc'].split(",")

# creating a html page
location = folium.Map(location_data, zoom_start=6)

# adding a marker
folium.Marker(location_data, popup="location").add_to(location)

# save the html page with a name
location.save("My location.html")

# starting the html page
os.startfile("My location.html")
