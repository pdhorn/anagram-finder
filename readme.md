# anagram-finder

Repo at https://github.com/pdhorn/anagram-finder

This is a simple webapp that displays anagrams of a string of letters as you type.  For example, if you type 'cytsim', it will display 'mystic', 'mist', 'cyst', 'sit', etc.

The front end is in React (with Hooks). Flask serves an API endpoint that accepts GET requests, and a homemade Python script calculates the anagrams.

Playing around with flask_restful package. Run with `python backend/application.py`

## Requirements
Python 3.6.6 (> 2.7 ?), pip, virtualenv, npm 6.8.  Flask, flask-restful, flask-cors, react (see `requirements.txt` and `frontend/package.json` for more details).

## Installation
Create a python virtual environment:


-`> virtualenv venv`

-`> source venv/bin/activate`

-`> pip install -r requirements.txt`

Then build the front end

-`> cd frontend`

-`> npm install`

## Run it

In one terminal, `> python backend/application.py`. In another terminal, `> cd frontend` and then `npm start`. A browser should open to `localhost:3000`.

## Frontend
I initially built the frontend with `> create-react-app frontend`, but with the source code and `package.json` you can just `> npm install`.

