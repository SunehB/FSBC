import requests

access_token = ''
query = 'Yesterday artist:The Beatles'
year = 1969
url = f'https://api.spotify.com/v1/search?q={requests.utils.quote(query)}&type=track'

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)

try:
    data = response.json()
    print(data)
except Exception as err:
    print(err)
