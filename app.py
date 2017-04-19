from flask import Flask # Import Flask package
from flask import render_template # Import render_template function
app = Flask(__name__) # Construct Flask object named 'app'

'''
@app.route() defines the URLs that route to the index() function.
The URLs will be appended to the end of the base URL.
Links within HTML files should use the defined routes (for example '/index') as
the values for href attributes.

URLs that will call the index() function if running app.py on localhost:
	http://localhost:5000/
	http://localhost:5000/index
'''

@app.route('/') # URL for function (default for home page)
@app.route('/index') # Secondary URL for function
def index():
	return render_template('index.html') # located in templates/
	
@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/states')
def states():
	return render_template('States.html')
	
@app.route('/parks')
def parks():
	return render_template('parks_model.html')

@app.route('/parktypes')
def parktypes():
	return render_template('park_types.html')

if __name__ == '__main__':
	app.run() # Run application