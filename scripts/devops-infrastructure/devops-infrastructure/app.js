const express = require('express');
const pg = require('pg');
const redis = require('redis');

const app = express();
const port = 5000;

const db = new pg.Pool({
  user: 'postgres',
  host: 'db',
  database: 'testdb',
  password: 'postgres',
  port: 5432
});

const cache = redis.createClient({
  host: 'cache'
});

app.get('/', (req, res) => {
  db.query('SELECT NOW()', (err, result) => {
    if (err) return res.status(500).send(err);
    cache.set('timestamp', result.rows[0].now, redis.print);
    cache.get('timestamp', (err, reply) => {
      if (err) return res.status(500).send(err);
      res.send(`Timestamp: ${reply}`);
    });
  });
});

app.listen(port, () => {
  console.log(`App running on port ${port}`);
});