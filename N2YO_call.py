import requests
import random

#how do we get the lat and longitude, also what about the API key?

#lat and lon for Boston
lat = 42.360
long = -71.059

response = requests.get(f'https://api.n2yo.com/rest/v1/satellite/above/{lat}/{long}/0/10/0/&apiKey=') #key hidden

data = response.json()  #returns a dictionary with two keys: info (metadata) and above (the actual satellite info)

sat_info = data["above"]    #sat_info is the array containing a dictionary for each satellite

years = []

for satellite in sat_info:
    years.append(satellite["intDesignator"][:4])

if len(years) == 0:
    print("Sorry, no satellites ahead.")        #no satellites found case

random_index = random.randint(0, len(years))    #get a random index to choose a random year

print(years[random_index])