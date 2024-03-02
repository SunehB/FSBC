from flask import Flask, send_from_directory
import requests
import sqlite3
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)

@app.route("/")

def hello_world():
    return send_from_directory('fsbc', 'index.html')

response = requests.get('https://api.n2yo.com/rest/v1/satellite/positions/25544/41.702/-76.014/0/2/&apiKey=MX593T-FEQLPN-D2GCKS-57TD')
data = response.json()
print(data)

conn = sqlite3.connect('fsbc_db.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM satellites")
rows = cursor.fetchall()

client_id = '0d675c23e6e94e338fe636bfe439d162'
client_secret = 'a9c6f0c945344443b7a3a8c12c859759'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = sp.search(q="remaster%20track:Doxy%20artist:Miles%20Davis", type='track', limit=10)
print(results['tracks']['items'])

for row in rows:
    print(row)  # You can customize how you want to display each row

cursor.close()
conn.close()

if __name__ == '__main__':
    app.run(debug=True)

