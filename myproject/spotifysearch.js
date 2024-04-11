const fetch = require('node-fetch');

const accessToken = 'BQCnkpOJOEXQKqVyy-uR86Gyv-_QX1gQJ9PrjGt3dTHEV8Vy7FB0tL839qct58Jt7p9fcn_twYc9nb4rHwgE6IFd2NQ7Xj3GNt8SMKLfj5fkOxs7KZE'; 
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
