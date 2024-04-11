import requests

access_token = 'BQD_xPHyO_mPFQm8cLHNdZNWXEc338gXC8ombPzqWXejjs3bhIId6KHXZFe_ronJ_6QwKwAHecIrfZ03h03YUssFveG5CjZuuYlM8l4-SG9qIHdCu5c'
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
    for track in tracks[:10]:  # Adjust as needed to display more or fewer results
        print(f"Track Name: {track['name']}")
        print(f"Popularity: {track['popularity']}")
        print(f"Album Name: {track['album']['name']}")
        print(f"Artists: {', '.join(artist['name'] for artist in track['artists'])}")
        print(f"Release Date: {track['album']['release_date']}")
        print(f"Spotify URL: {track['external_urls']['spotify']}\n")
    
except Exception as err:
    print(err)
