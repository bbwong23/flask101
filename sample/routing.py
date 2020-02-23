from flask import Flask, request
app = Flask(__name__)

@app.route('/') # Defaults to allow only GET
def index():
  return 'Hello World!'

@app.route('/status', methods=['POST'])
def status():
	return 'API is running'

@app.route('/intro', methods=['POST','GET']) 
def print_name():
	req_data = request.get_json()
	name = req_data['name']
	return 'Hello my name is {}'.format(name)

# variable in path must match func arguments
@app.route('/intro2/<name>') 
def print_name_path(name):
	return 'Hello my name is {}'.format(name)

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8080)
