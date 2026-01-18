const express = require('express');
const app = express();
const port = 3000;

let users = [];

app.use(express.json());

app.get('/users', (req, res) => {
  res.send(users);
});

app.post('/users', (req, res) => {
  const user = req.body;
  users.push(user);
  res.send(user);
});

app.get('/users/:id', (req, res) => {
  const user = users.find(u => u.id === req.params.id);
  if (user) {
    res.send(user);
  } else {
    res.status(404).send();
  }
});

app.put('/users/:id', (req, res) => {
  const user = users.find(u => u.id === req.params.id);
  if (user) {
    Object.assign(user, req.body);
    res.send(user);
  } else {
    res.status(404).send();
  }
});

app.delete('/users/:id', (req, res) => {
  const index = users.findIndex(u => u.id === req.params.id);
  if (index !== -1) {
    users.splice(index, 1);
    res.status(204).send();
  } else {
    res.status(404).send();
  }
});

app.listen(port, () => {
  console.log(`API server listening at http://localhost:${port}`)
});

module.exports = app;