// index.js
const express = require('express');
const app = express();
var cors = require('cors')

const analysis = require('./analysis')


app.use(cors())

app.get('/', (req, res) => {
  res.send('Homepage! Hello world.');
});

app.get('/about', (req, res) => { // new
  res.send('About page. Nice.');
});

app.get('/analysis', (req, res) => {

  const response = {
    'Politics': 25,
    'Education': 25,
    'Technology': 25,
    'Environment': 25,
  }

  res.json(response)
})

app.listen(8000, () => console.log('listening on port 8000'));

// current data model:
const response = {
  'Politics': 25,
  'Education': 25,
  'Technology': 25,
  'Environment': 25,
}


// replacement data model:

