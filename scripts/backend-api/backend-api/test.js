const chai = require('chai');
const chaiHttp = require('chai-http');
const server = require('./index');
const expect = chai.expect;

chai.use(chaiHttp);

describe('Users API', () => {
  it('should list all users on /users GET', done => {
    chai.request(server)
      .get('/users')
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res.body).to.be.a('array');
        done();
      });
  });

  // Other tests for POST, GET/:id, PUT/:id, DELETE/:id
});