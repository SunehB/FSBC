import requests

access_token = 'BQB2UWHHvPaFYJIfvjeB2Hgp-dfuXHVYn0NrTT5uPyyF24v2StqkHQyUp0yAALaIG2lwqEtCu9hbyIsIQLTMxXNQOavhzwKLt1A9x_W_z0i73XgMo4k'
query = 'Yesterday artist:The Beatles'
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
