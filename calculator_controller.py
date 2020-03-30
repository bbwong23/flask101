###########################
# 1. import flask library 
###########################
import service.calculator as calculator
from http import HTTPStatus

from flask import jsonify


###########################
# 2. initialize your Flask application object
###########################
app = 



###########################
# 3. define route paths for the following functions with the specified path and method
# 4. and parse the request to get the user_input given the request type
###########################


# path = '/mean', method = 'GET'
# request type = JSON
def mean():
	# user_input = 
	
	results = calculator.mean(user_input)

	return jsonify({'output':results}), HTTPStatus.OK


# path = '/median', method = 'GET and POST'
# request type = Query
def median():
	# user_input = 

	user_input = list(map(int, user_input.split(',')))
	results = calculator.median(user_input)

	return jsonify({'output':results}), HTTPStatus.OK

# path = '/mode', method = 'POST'
# request type = Form
def mode():
	# user_input = 

	user_input = list(map(int, user_input))
	results = calculator.mode(user_input)

	return jsonify({'output':results}), HTTPStatus.OK


# path = '/status', method = 'GET'
def status():
	result = "Application is running"
	return result, HTTPStatus.OK


if __name__ == '__main__':
	###########################
	# 5. Start your flask app
	###########################
