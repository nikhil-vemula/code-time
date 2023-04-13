from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        return {'message': 'hello world'}, 200

api.add_resource(Users, '/users')


if __name__ == '__main__':
    app.run() 