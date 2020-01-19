from flask import Flask, request, jsonify # Import the flask web server
from Referencer.ReferenceRanker import *
from Referencer.DomainCreator import *
from Referencer.TextExtractor import *
from itertools import islice
from tldextract import extract
import operator

app = Flask(__name__) # Single module that grabs all modules executing from this file

textextr = TextRank4Keyword()
entityget = EntityGetter()
domcre = DomainGetter()
refrank = RefRanker()

@app.route('/', methods=['GET', 'POST']) # Tells the flask server on which url path does it trigger which for this example is the index page calling "hello_world" function.
def handle_request():
	if request.method == 'POST':
		data = request.get_json()

		# Receive the text
		text = data['text']

		# Receive the url
		_, td, tsu = extract(data['url'])
		curr_url = td + '.' + tsu
		print("THIS IS THE TEXT")
		print(text)

		# Get keywords
		keywords = textextr.run(text, 2)

		print("THIS IS THE KEYWORDS")
		print(keywords)

		# Get entities
		entities = []
		for keyword in keywords:
			entities.append(entityget.run(keyword))

		entity = entities[0][0]
		print("THIS IS THE ENTITY")
		print(entity)

		# Get domains
		list_of_articles = domcre.run(entity, 100)

		print("THIS IS THE LIST OF ARTICLES")
		print(list_of_articles)
		
		# Rank references
		ranked_articles = refrank.run(list_of_articles)
		top_articles = dict(sorted(ranked_articles.items(), key=operator.itemgetter(1), reverse=True)[:5])
		if curr_url not in top_articles:
			curr_value = 0 if curr_url not in ranked_articles else ranked_articles[curr_url]
			top_articles[curr_url] = curr_value

		# Create the response
		response_body = {
			'ranking': top_articles,
			'request_url' : curr_url
		}
		response = app.response_class(response=json.dumps(response_body),
                                  status=200,
                                  mimetype='application/json')
		response.headers['Access-Control-Allow-Origin'] = '*'

		return response
	else:
		return 'Hello, World!'


@app.route('/keywords', methods=['GET', 'POST']) # Tells the flask server on which url path does it trigger which for this example is the index page calling "hello_world" function.
def handle_keyword_request():
	if request.method == 'POST':
		data = request.get_json()

		# Get keywords
		keywords = textextr.run(data['text'], 10)
		print('HERE ARE THE KEYWORDS')
		print(keywords)

		return jsonify(keywords)
	else:
		return 'Hello, Keywords!'
