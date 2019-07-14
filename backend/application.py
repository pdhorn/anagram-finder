from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

from anagrams import anagram_finder

# app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
# app.config['CORS_HEADERS'] = 'Content-Type'

# @app.route('/foo', methods=['POST'])
# @cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
# def foo():
    # return request.json['inputVar']

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/anagram": {"origins": "http://localhost:3000"}})


class AnagramAPI(Resource):
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('stem', type=str)
        stem = parser.parse_args()['stem']
        anagram_list = anagram_finder(stem).calculate()
        return anagram_list

api.add_resource(AnagramAPI, '/anagram', endpoint='anagram')

if __name__ == '__main__':
    app.run(debug=True)
