from flask import Flask
from flask_restful import Resource, Api, reqparse

from anagrams import anagram_finder

app = Flask(__name__)
api = Api(app)

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
