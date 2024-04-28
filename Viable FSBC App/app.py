from flask import Flask, redirect, request, render_template
from spotipy import Spotify, util, oauth2
import requests
import random
import sqlite3

#Before running, make sure the Spotify CLIENT_ID, CLIENT_SECRET, and REDIRECT_URI are correct.
#Also ensure the N2YO key is correct
#Delete any stored SQL Database and .cache to ensure correct ID identification (residue from previous runs breaks integrety)
#When run for the first time, Spotify will require authentication to a premium spotify account, do this and click the button.
#If not song plays in 5 seconds, the program needed time to generate the cache so click it again.

app = Flask(__name__)

# Spotify credentials
CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = 'http://localhost:5000/callback'
SCOPE = 'user-read-playback-state user-modify-playback-state'

# Spotify authentication
sp_oauth = oauth2.SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE)


def insertRow (db, cursor, id, date, song, client, satid):
      try:
         cursor.execute("INSERT INTO fsbcDB (id, date, song, client, satid) VALUES (?, ?, ?, ?, ?)", (id, date, song, client, satid))
         db.commit()
         print("Insert operation successful")
      except sqlite3.Error as e:
         print("Insert operation failed:", e)

def deleteRow(db, cursor, id_toDelete):
      try:
         cursor.execute("DELETE FROM fsbcDB WHERE id=?", (id_toDelete,))
         db.commit()
         print("Delete operation successful")
      except sqlite3.Error as e:
         print("Delete operation failed:", e)

def printTable(cursor):
      cursor.execute("SELECT * FROM fsbcDB")
      rows = cursor.fetchall()
      for row in rows:
         print(row)
         
logID = 0

@app.route('/')
def index():
    # Render the template and pass an empty result initially
    return render_template('index.html', n2yo_result=None)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    token = token_info['access_token']
    return redirect('/')

@app.route('/play', methods=['POST'])
def play():
#--------------------------------------------------------------------------------------------------------------
	#N2YO Call to retrieve Satillite
    lat = 42.360
    long = -71.059
    response = requests.get(f'https://api.n2yo.com/rest/v1/satellite/above/{lat}/{long}/0/10/0/&apiKey=') #key hidden (Dont Forget to Readd)
    data = response.json()  #returns a dictionary with two keys: info (metadata) and above (the actual satellite info)
    sat_info = data["above"]    #sat_info is the array containing a dictionary for each satellite
    satellites = []
    for satellite in sat_info:
      satellites.append([satellite['satid'], satellite['satname'], satellite["intDesignator"][:4]])
    if len(satellites) == 0:
      print("Sorry, no satellites ahead.")        #no satellites found case
    random_index = random.randint(0, len(satellites)-1)    #get a random index to choose a random year
    N2YO_result = satellites[random_index]      #result is an array containing the satellite id, name, and year
    satId = N2YO_result[0]
    satName = N2YO_result[1]
    satYear = N2YO_result[2]
    #get_satellite_image_url finds a picture of satellite based on ID
    print("Completed N2YO and selected: ", N2YO_result)
#--------------------------------------------------------------------------------------------------------------
	#Make a Spotify search based on the N2YO results
    if 'USA' in satName:
        #THIS IS CRITICAL!!! DO NOT CHANGE THIS FOR ANY REASON
        song_name = 'Fortunate son'
    else:
        song_name = satYear
        
    token_info = sp_oauth.get_cached_token()
    if not token_info:
        return redirect(sp_oauth.get_authorize_url())
    token = token_info['access_token']
    sp = Spotify(auth=token)

    # Get user devices to play the song through (must have spotify open)
    devices = sp.devices()
    if devices['devices']:
        device_id = devices['devices'][0]['id']  # Use the first available device
        results = sp.search(q='track:' + song_name, type='track', limit=1)
        if results['tracks']['items']:
            song_uri = results['tracks']['items'][0]['uri']
            song_name = results['tracks']['items'][0]['name']
            sp.start_playback(device_id=device_id, uris=[song_uri])
            print('--------------------------------')
            print('Playing: ' + song_name + ' based on satName and Id: ' + satName + ' ' + str(satId) + ' launched in year: ' + satYear)
            print('--------------------------------')
            
#--------------------------------------------------------------------------------------------------------------
			#Store The Entry into SQL
            db = sqlite3.connect('DataBase.db')
            cursor = db.cursor()
            table ="""CREATE TABLE IF NOT EXISTS fsbcDB (id INTEGER PRIMARY KEY, date STRING, song STRING, client INTEGER, satid INTEGER);"""
            cursor.execute(table)
            global logID
            logID += 1
            song = song_name
            client = 0
            insertRow(db, cursor, logID, satYear, song, client, satId)
            printTable(cursor)
#--------------------------------------------------------------------------------------------------------------
            return redirect('/')
        else:
            return 'Song not found'
    else:
        return 'No active device available'
        
    return render_template('index.html', n2yo_result=N2YO_result)


if __name__ == '__main__':
    app.run(debug=True)
