from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    get_jwt_identity
)
from secure_check import authenticate

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'mysecretkey'

api = Api(app)
jwt = JWTManager(app)

# in-memory database
puppies = []

class Login(Resource):
    def post(self):
        data = request.get_json()

        username = data.get('username')
        password = data.get('password')

        user = authenticate(username, password)

        if not user:
            return {'message': 'Invalid credentials'}, 401

        access_token = create_access_token(identity=str(user.id))
        return {'access_token': access_token}, 200

class PuppyNames(Resource):
    def get(self, name):
        for pup in puppies:
            if pup['name'] == name:
                return pup
        return {'name': None}, 404

    def post(self, name):
        pup = {'name': name}
        puppies.append(pup)
        return pup, 201

    def delete(self, name):
        for ind, pup in enumerate(puppies):
            if pup['name'] == name:
                puppies.pop(ind)
                return {'note': 'delete success'}, 200
        return {'message': 'Puppy not found'}, 404


class AllNames(Resource):
    @jwt_required()
    def get(self):
        return {'puppies': puppies}, 200


api.add_resource(Login, '/login')
api.add_resource(PuppyNames, '/puppy/<string:name>')
api.add_resource(AllNames, '/puppies')

if __name__ == '__main__':
    app.run(debug=True)
