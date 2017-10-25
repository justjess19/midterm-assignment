from flask import render_template
import json
import requests

## SI 364
## Fall 2017
## HW 3

## This homework has 2 parts. This file is the basis for HW 3 part 1.

## Add view functions to this Flask application code below so that the routes described in the 
#README exist and render the templates they are supposed to (all templates provided inside the HW3Part1/templates directory).

from flask import Flask, request
app = Flask(__name__)
app.debug = True 


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<name>')
def hello_user(name):
    return '<h1>Hello {0}<h1>'.format(name)


@app.route('/artistform')
def artistform():
    return render_template('artistform.html')

@app.route('/artistinfo')
def artist_info():
	if request.method == 'GET':
		result = request.args
		params = {}
		params['term'] = result.get('artist')
		params['limit'] = result.get('num')
		resp = requests.get('https://itunes.apple.com/search?', params = params)
		data = json.loads(resp.text)
		return render_template('artist_info.html', objects=data['results'])

@app.route('/artistlinks')
def artistlinks():
    return render_template('artist_links.html')

@app.route('/specific/song/<artist_name>')
def artist_name(artist_name):
	params = {}
	params['term'] = artist_name
	resp = requests.get('https://itunes.apple.com/search?', params = params)
	data = json.loads(resp.text)
#    return render_template('list.html', results = data['results'])
	return render_template('artist_links.html')



if __name__ == '__main__':
    app.run(debug = True)