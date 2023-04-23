from flask import Flask, jsonify, make_response
from flask_restful import Resource, Api, reqparse
import psycopg2
import pandas as pd
from flask_cors import CORS
import os
from waitress import serve


app = Flask(__name__)
CORS(app)
api = Api(app)

# conn = psycopg2.connect(
#     host = os.getenv("CODE_TIME_DB_HOST"),
#     database = os.getenv("CODE_TIME_DB_DATABSE"),
#     user = os.getenv("CODE_TIME_DB_USERNAME"),
#     password = os.getenv("CODE_TIME_DB_PASSWORD")
# )

conn = psycopg2.connect(
    host = "localhost",
    database = 'coding_made_easy',
    password = ''
)

class Welcome(Resource):
    def get(self):
        return "Welcome! Server is running", 200

class Users(Resource):
    def post(self):
        try:
            curr = conn.cursor()
            parser = reqparse.RequestParser()
            parser.add_argument('username', required=True)
            parser.add_argument('password', required=True)
            args = parser.parse_args()
            username = args['username']
            password = args['password']
            curr.execute(
                'SELECT * FROM users WHERE user_name=%s and password=%s', (username, password, ))
            result = pd.DataFrame(curr.fetchall(), columns=[
                                i[0] for i in curr.description])
            result.drop('password', axis=1)
            resp = result.to_dict(orient='records')
            return make_response(jsonify(resp), 200)
        except Exception as error:
            print(error)
            conn.rollback()
        finally:
            curr.close()


class Questions(Resource):
    def post(self):
        try:
            curr = conn.cursor()
            parser = reqparse.RequestParser()
            parser.add_argument('user_id', required=True)
            args = parser.parse_args()
            user_id = args['user_id']
            curr.execute(
                "SELECT * FROM questions WHERE user_id=%s ORDER BY question_id", (user_id, ))
            result = pd.DataFrame(curr.fetchall(), columns=[
                                i[0] for i in curr.description])
            resp = result.to_dict(orient='records')
            return make_response(jsonify(resp), 200)
        except Exception as error:
            print(error)
            conn.rollback()
        finally:
            curr.close()
        


class Question(Resource):
    def get(self, question_id):
        try:
            curr = conn.cursor()
            curr.execute(
                f"SELECT * FROM questions WHERE question_id=%s", (question_id, ))
            result = pd.DataFrame(curr.fetchall(), columns=[
                                i[0] for i in curr.description])
            resp = result.to_dict(orient='records')
        except Exception as error:
            print(error)
            conn.rollback()
        finally:
            curr.close()
        return make_response(jsonify(resp), 200)
    
    def delete(self, question_id):
        try:
            curr = conn.cursor()
            curr.execute(
                "DELETE FROM questions WHERE question_id=%s", (question_id, ))
            return make_response('Deleted', 200)
        except Exception as error:
            print(error)
            conn.rollback()
        finally:
            conn.commit()
            curr.close()

    def put(self, question_id):
        try:
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
            return make_response(jsonify(resp), 200)
        except Exception as error:
                print(error)
                conn.rollback()
        finally:
                curr.close()


class CreateQuestion(Resource):
    def post(self):
        try:
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
            return make_response(jsonify({'question_id': question_id}), 200)
        except Exception as error:
            print(error)
            conn.rollback()
        finally:
            curr.close()


class MarkSolved(Resource):
    def get(self, question_id, solved):
        try:
            curr = conn.cursor()
            curr.execute(
                "INSERT INTO last_revised (question_id, solved, revised_time) VALUES(%s, %s, NOW()) RETURNING question_id", (question_id, solved, ))
            conn.commit()
            return make_response({}, 200)
        except Exception as error:
            print(error)
            conn.rollback()
        finally:
            curr.close()

class QuestionsRevised(Resource):
    def get(self, user_id):
        try:
            curr = conn.cursor()
            curr.execute("SELECT * FROM get_revise_questions(%s)", (user_id, ))
            result = pd.DataFrame(curr.fetchall(), columns=[
                                i[0] for i in curr.description])
            resp = result.to_dict(orient='records')
            return make_response(jsonify(resp), 200)
        except Exception as error:
            print(error)
            conn.rollback()
        finally:
            curr.close()


class ProblemCount(Resource):
    def get(self, user_id):
        try:
            curr = conn.cursor()
            curr.execute("SELECT * FROM get_problems_count(%s)", (user_id, ))
            count = curr.fetchone()[0]
            return make_response(jsonify({'count': count}), 200)
        except Exception as error:
            print(error)
            conn.rollback()
        finally:
            curr.close()


class SolvedProblemCount(Resource):
    def get(self, user_id):
        try:
            curr = conn.cursor()
            curr.execute(
                "SELECT * FROM get_solved_problems_count(%s)", (user_id, ))
            count = curr.fetchone()[0]
            return make_response(jsonify({'count': count}), 200)
        except Exception as error:
            print(error)
            conn.rollback()
        finally:
            curr.close()


class CreateUser(Resource):
    def post(self):
        try:
            curr = conn.cursor()
            parser = reqparse.RequestParser()
            parser.add_argument('firstname', required=True)
            parser.add_argument('lastname', required=True)
            parser.add_argument('email', required=True)
            parser.add_argument('password', required=True)
            args = parser.parse_args()
            curr.execute("INSERT INTO users (first_name, last_name, user_name, password) VALUES (%s, %s, %s, %s) RETURNING user_name", 
                        (args['firstname'], args['lastname'], args['email'], args['password']))
            user_name = curr.fetchone()[0]
            curr.execute("SELECT * from users WHERE user_name=%s", (user_name, ))
            result = pd.DataFrame(curr.fetchall(), columns=[
                                i[0] for i in curr.description])
            result.drop('password', axis=1)
            resp = result.to_dict(orient='records')
            conn.commit()
            return make_response(jsonify(resp), 200)
        except Exception as error:
            print(error)
            return make_response("Error", 404)
        finally:
            curr.close()
        


api.add_resource(Welcome, '/')
api.add_resource(Users, '/users')
api.add_resource(Questions, '/questions')
api.add_resource(CreateQuestion, '/question')
api.add_resource(Question, '/question/<question_id>')
api.add_resource(MarkSolved, '/marksolved/<question_id>/<solved>')
api.add_resource(QuestionsRevised, '/questionsrevise/<user_id>')
api.add_resource(ProblemCount, '/get_problems_count/<user_id>')
api.add_resource(SolvedProblemCount, '/get_solved_problems_count/<user_id>')
api.add_resource(CreateUser, '/createuser')

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8000, threads=100)
    # app.run()
