from flask import Flask, jsonify, make_response
from flask_restful import Resource, Api, reqparse
import psycopg2
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

conn = psycopg2.connect(
    host="localhost",
    database="coding_made_easy",
    password=""
)

curr = conn.cursor()


class Users(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True)
        parser.add_argument('password', required=True)
        args = parser.parse_args()
        username = args['username']
        password = args['password']
        curr.execute(
            f"SELECT * FROM users WHERE user_name=%s and password=%s", (username, password, ))
        result = pd.DataFrame(curr.fetchall(), columns=[
                              i[0] for i in curr.description])
        resp = result.to_dict(orient='records')

        return make_response(jsonify(resp), 200)


class Questions(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', required=True)
        args = parser.parse_args()
        user_id = args['user_id']
        curr.execute("SELECT * FROM questions WHERE user_id=%s", (user_id))
        result = pd.DataFrame(curr.fetchall(), columns=[
                              i[0] for i in curr.description])
        resp = result.to_dict(orient='records')
        return make_response(jsonify(resp), 200)


class Question(Resource):
    
    def get(self, question_id):
        print(question_id)
        curr.execute(
            f"SELECT * FROM questions WHERE question_id=%s", (question_id, ))
        result = pd.DataFrame(curr.fetchall(), columns=[
                              i[0] for i in curr.description])
        resp = result.to_dict(orient='records')
        return make_response(jsonify(resp), 200)
    
    def put(self, question_id):
        print(question_id)

        parser = reqparse.RequestParser()
        parser.add_argument('user_id', required=True)
        parser.add_argument('title', required=True)
        parser.add_argument('url', required=True)
        parser.add_argument('short_desc', required=True)
        parser.add_argument('description', required=True)
        parser.add_argument('tags', required=True)
        parser.add_argument('difficulty_level', required=True)
        parser.add_argument('notes', required=True)
        args = parser.parse_args()

        curr.execute('''
        UPDATE questions SET title=%s, url=%s, short_desc=%s, description=%s, difficulty_level=%s, tags=%s, notes=%s, user_id=%s RETURNING question_id''', 
        (args['title'], args['url'], args['short_desc'], args['description'], args['difficulty_level'], 
         args['tags'], args['notes'], args['user_id'],))
        result = curr.fetchone()[0]
        resp = {'question_id': result}
        return make_response(jsonify(resp), 200)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', required=True)
        parser.add_argument('title', required=True)
        parser.add_argument('url', required=True)
        parser.add_argument('short_desc', required=True)
        parser.add_argument('description', required=True)
        parser.add_argument('tags', required=True)
        parser.add_argument('difficulty_level', required=True)
        parser.add_argument('notes', required=True)
        args = parser.parse_args()
        curr.execute('''
        INSERT INTO questions (title, url, short_desc, description, difficulty_level, tags, notes, user_id) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING question_id''', 
        (args['title'], args['url'], args['short_desc'], args['description'], args['difficulty_level'], 
         args['tags'], args['notes'], args['user_id'],))
        question_id = curr.fetchone()[0]
        conn.commit()
        return make_response(jsonify({'question_id': question_id}), 200)


api.add_resource(Users, '/users')
api.add_resource(Questions, '/questions')
api.add_resource(Question, '/question/<question_id>')

if __name__ == '__main__':
    app.run()
