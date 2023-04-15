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


class Users(Resource):
    def post(self):
        curr = conn.cursor()
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
        curr.close()
        return make_response(jsonify(resp), 200)


class Questions(Resource):
    def post(self):
        curr = conn.cursor()
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', required=True)
        args = parser.parse_args()
        user_id = args['user_id']
        curr.execute("SELECT * FROM questions WHERE user_id=%s ORDER BY question_id", (user_id))
        result = pd.DataFrame(curr.fetchall(), columns=[
                              i[0] for i in curr.description])
        resp = result.to_dict(orient='records')
        curr.close()
        return make_response(jsonify(resp), 200)


class Question(Resource):
    def get(self, question_id):
        curr = conn.cursor()
        print(question_id)
        curr.execute(
            f"SELECT * FROM questions WHERE question_id=%s", (question_id, ))
        result = pd.DataFrame(curr.fetchall(), columns=[
                              i[0] for i in curr.description])
        resp = result.to_dict(orient='records')
        curr.close()
        return make_response(jsonify(resp), 200)
    
    def put(self, question_id):
        curr = conn.cursor()
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
        UPDATE questions SET title=%s, url=%s, short_desc=%s, description=%s, difficulty_level=%s, tags=%s, notes=%s
        WHERE question_id= %s and user_id=%s RETURNING question_id''', 
        (args['title'], args['url'], args['short_desc'], args['description'], args['difficulty_level'], 
         args['tags'], args['notes'], question_id, args['user_id']))
        result = curr.fetchone()[0]
        resp = {'question_id': result}
        curr.close()
        return make_response(jsonify(resp), 200)

class CreateQuestion(Resource):
    def post(self):
        curr = conn.cursor()
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
        curr.close()
        return make_response(jsonify({'question_id': question_id}), 200)
    
class MarkSolved(Resource):
    def get(self, question_id, solved):
        curr = conn.cursor()
        curr.execute("INSERT INTO last_revised (question_id, solved, revised_time) VALUES(%s, %s, NOW()) RETURNING question_id", (question_id, solved, ))
        conn.commit()
        curr.close()
        return make_response({}, 200)

class QuestionsRevised(Resource):
    def get(self, user_id):
        curr = conn.cursor()
        curr.execute("SELECT * FROM get_revise_questions(%s)", (user_id, ))
        result = pd.DataFrame(curr.fetchall(), columns=[
                              i[0] for i in curr.description])
        resp = result.to_dict(orient='records')
        curr.close()
        return make_response(jsonify(resp), 200)
    
class ProblemCount(Resource):
    def get(self, user_id):
        curr = conn.cursor()
        print(user_id)
        print("1-1")
        curr.execute("SELECT * FROM get_problems_count(%s)", (user_id, ))
        print("1-2")
        count = curr.fetchone()[0]
        curr.close()
        return make_response(jsonify({'count': count}), 200)

class SolvedProblemCount(Resource):
    def get(self, user_id):
        curr = conn.cursor()
        curr.execute("SELECT * FROM get_solved_problems_count(%s)", (user_id, ))
        count = curr.fetchone()[0]
        curr.close()
        return make_response(jsonify({'count': count}), 200)

api.add_resource(Users, '/users')
api.add_resource(Questions, '/questions')
api.add_resource(CreateQuestion, '/question')
api.add_resource(Question, '/question/<question_id>')
api.add_resource(MarkSolved, '/marksolved/<question_id>/<solved>')
api.add_resource(QuestionsRevised, '/questionsrevise/<user_id>')
api.add_resource(ProblemCount, '/get_problems_count/<user_id>')
api.add_resource(SolvedProblemCount, '/get_solved_problems_count/<user_id>')

if __name__ == '__main__':
    app.run()
