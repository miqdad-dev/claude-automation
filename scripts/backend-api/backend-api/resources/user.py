from flask_restful import Resource, reqparse
from models.user import User

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if User.query.filter_by(name=data['name']).first():
            return {"message": "A user with that username already exists"}, 400

        user = User(name=data['name'])
        user.save_to_db()

        return {"message": "User created successfully."}, 201