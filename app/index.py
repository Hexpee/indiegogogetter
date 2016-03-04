from app import app
from flask import render_template
import simplejson as json
from urllib2 import urlopen

@app.route('/')
def index():
	api_endpoint = urlopen('https://api.indiegogo.com/1/search/campaigns.json?api_token=e377270bf1e9121da34cb6dff0e8af52a03296766a8e955c19f62f593651b346').read()
	items = json.loads(api_endpoint)['response']
	return render_template('index.html', **locals())





