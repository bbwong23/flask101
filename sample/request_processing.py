from flask import Flask, request
app = Flask(__name__)

@app.route('/json', methods=['POST'])
def json_request():
	req_data = request.get_json()
	name = req_data['name']
	return 'Hello my name is {}'.format(name)

@app.route('/query')
def query_request():
	name = request.args.get('name') 
	# name = request.args['name']
	return 'Hello my name is {}'.format(name)

@app.route('/form', methods=['POST'])
def form_request():
	name = request.form.get('name')
	# name = request.form['name']
	return 'Hello my name is {}'.format(name)

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8080)

