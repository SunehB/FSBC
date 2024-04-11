from flask import Flask, render_template
from flask_cors import CORS, cross_origin
import requests
import random
import sqlite3
from N2YO_call import get_sat_data

app = Flask(__name__, static_url_path='/static')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

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

@app.route('/')
def home():
   return render_template('index.html')

#returns satelite info to website
@app.route("/satelite")
@cross_origin()
def satelite():
    return get_sat_data()

@app.route('/process', methods=['POST']) 
def process(): 
   # This function will be called when the button is clicked 
   # You can write your Python code here 
   print('Function called successfully' )

   #--------------------------------------------------------------------------------------------------------------
   
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
   random_index = random.randint(0, len(satellites))    #get a random index to choose a random year
   N2YO_result = satellites[random_index]      #result is an array containing the satellite id, name, and year

   #--------------------------------------------------------------------------------------------------------------
   db = sqlite3.connect('DataBase.db')
   cursor = db.cursor()

   table ="""CREATE TABLE IF NOT EXISTS fsbcDB (id INTEGER PRIMARY KEY, date STRING, song STRING, client INTEGER, satid INTEGER);"""
   cursor.execute(table)

   id = 0
   date = '4-7-24'
   song = 'Never Gonna Give You Up'
   client = 83902
   satid = years[random_index]
   insertRow(db, cursor, id, date, song, client, satid)
    #--------------------------------------------------------------------------------------------------------------
    access_token = ''
    year = N2YO_result[2]
    search_query = f'year:{year}'
      
    url = 'https://api.spotify.com/v1/search'
      
    headers = {
          'Authorization': f'Bearer {access_token}',
          'Content-Type': 'application/json'
    }
    params = {
          'q': search_query,
          'type': 'track',
          'limit': 50,  
          'market': 'US' 
    }
      
      
    response = requests.get(url, headers=headers, params= params)
      
      
      
    try:
          data = response.json()
          tracks = data['tracks']['items']
          for track in tracks[:10]: 
              print(f"Track Name: {track['name']}")
              print(f"Popularity: {track['popularity']}")
              print(f"Album Name: {track['album']['name']}")
              print(f"Artists: {', '.join(artist['name'] for artist in track['artists'])}")
              print(f"Release Date: {track['album']['release_date']}")
              print(f"Spotify URL: {track['external_urls']['spotify']}\n")
          
    except Exception as err:
          print(err)
  
   return render_template('index.html')

if __name__ == '__main__':
   app.run()

#http://127.0.0.1:5000/
