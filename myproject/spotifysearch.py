import requests

<<<<<<< HEAD
access_token = ''
=======
access_token = ''
>>>>>>> b7b34fc5b39d85468d5c2a87d9fb725b202ed8b3
year = 1969
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
