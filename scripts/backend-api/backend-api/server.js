const express = require('express');
const mongodb = require('mongodb');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

let db;

mongodb.MongoClient.connect('mongodb://localhost:27017', function(err, client) {
  if (err) throw err;

  db = client.db('test');

  app.listen(3000, () => console.log('Listening on port 3000'));
});

app.get('/items', (req, res) => {
  db.collection('items').find().toArray((err, items) => {
    if (err) throw err;

    res.json(items);
  });
});

app.post('/items', (req, res) => {
  db.collection('items').insertOne(req.body, (err, result) => {
    if (err) throw err;

    res.json(result.ops[0]);
  });
});

app.put('/items/:id', (req, res) => {
  const id = new mongodb.ObjectID(req.params.id);

  db.collection('items').updateOne({_id: id}, {$set: req.body}, (err, result) => {
    if (err) throw err;

    res.json(result);
  });
});

app.delete('/items/:id', (req, res) => {
  const id = new mongodb.ObjectID(req.params.id);

  db.collection('items').deleteOne({_id: id}, (err, result) => {
    if (err) throw err;

    res.json(result);
  });
});