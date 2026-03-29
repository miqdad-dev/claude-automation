from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

@app.before_first_request
def setup():
    db.create_all()
    data = pd.read_csv('users.csv')
    for index, row in data.iterrows():
        user = User(name=row['name'], email=row['email'])
        db.session.add(user)
    db.session.commit()

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return {'users': [user.name for user in users]}

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user = User(name=data['name'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return {'message': 'User added successfully'}

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')