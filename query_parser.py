# File which handles parsing a user query for key terms that
# can be sent to the Evaluate method

import json
import requests

# API keys
API_KEY1 = 'XXX'

# Analytic API Constants
KEYPHRASE_URL = "https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/keyPhrases"
ANALYTICS_HEADERS = {'Content-Type': 'application/json',
                     'Ocp-Apim-Subscription-Key': API_KEY1}

def construct_query(user_input):
	""" 
	Function to insert user input into correct query format

	:returns: json formatted query
	"""
	query = { "documents": [
				{ "language": "en",
				  "id": "1",
				  "text": user_input
				}
			] }
	return query

def parseQuery(user_input):
	""" 
	Generates a keyword list given user input

	:returns: keyword list
	"""
	response = requests.post(KEYPHRASE_URL, json=construct_query(user_input) , headers=ANALYTICS_HEADERS)
	data = response.json()
	word_list = []
	if 'documents' in data:
		word_list = data['documents'][0]['keyPhrases']
		# takes the first 16 keywords returned, eliminates some less relevant keywords in most abstracts.
		# if a keyword list has less than 16 words, all of the words are used.
		word_list = word_list[0:16]
	return word_list





