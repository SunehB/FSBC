const fetch = require('node-fetch');

const accessToken = ''; 
const query = encodeURIComponent('Yesterday artist:The Beatles');
const url = `https://api.spotify.com/v1/search?q=${query}&type=track`;

fetch(url, {
  method: 'GET',
  headers: {
    'Authorization': `Bearer ${accessToken}`,
    'Content-Type': 'application/json'
  }
})
.then(response => response.json())
.then(data => console.log(data))
.catch(err => console.error(err));
