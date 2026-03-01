const chai = require('chai');
const chaiHttp = require('chai-http');
const mongodb = require('mongodb');
const server = require('../server');
const expect = chai.expect;

chai.use(chaiHttp);

describe('Items API', () => {

  it('should list all items on /items GET', (done) => {
    chai.request(server)
      .get('/items')
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res).to.be.json;
        expect(res.body).to.be.a('array');
        done();
      });
  });

  it('should add a single item on /items POST', (done) => {
    chai.request(server)
      .post('/items')
      .send({'title': 'Test', 'description': 'Test item'})
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res).to.be.json;
        expect(res.body).to.be.a('object');
        expect(res.body).to.have.property('title');
        expect(res.body).to.have.property('description');
        done();
      });
  });

  it('should update a single item on /items/:id PUT', (done) => {
    const id = new mongodb.ObjectID();
    chai.request(server)
      .put(`/items/${id}`)
      .send({'title': 'Test Updated', 'description': 'Test item updated'})
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res).to.be.json;
        expect(res.body).to.be.a('object');
        expect(res.body).to.have.property('title');
        expect(res.body).to.have.property('description');
        done();
      });
  });

  it('should delete a single item on /items/:id DELETE', (done) => {
    const id = new mongodb.ObjectID();
    chai.request(server)
      .delete(`/items/${id}`)
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res).to.be.json;
        expect(res.body).to.be.a('object');
        done();
      });
  });

});