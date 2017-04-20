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

@app.route('/anzaborrego')
def anzaborrego():
	return render_template('Anza-Borrego_park.html')

@app.route('/bigbend')
def bigbend():
	return render_template('bigbend_park.html')

@app.route('/california')
def california():
	return render_template('California.html')

@app.route('/centralpark')
def centralpark():
	return render_template('Central_Park.html')

@app.route('/florida')
def florida():
	return render_template('Florida.html')

@app.route('/historictrail')
def historictrail():
	return render_template('Historic_Trail.html')

@app.route('/monument')
def monument():
	return render_template('Monument.html')

@app.route('/nationalpark')
def nationalpark():
	return render_template('National_Park.html')

@app.route('/newyork')
def newyork():
	return render_template('New York.html')

@app.route('/preserve')
def preserve():
	return render_template('Preserve.html')

@app.route('/statepark')
def statepark():
	return render_template('State_Park.html')

@app.route('/texas')
def texas():
	return render_template('Texas.html')

@app.route('/timucuanpark')
def timucuanpark():
	return render_template('Timucuan_park.html')

@app.route('/washingtonstatepark')
def washingtonstatepark():
	return render_template('Washington_State_park.html')

@app.route('/washington')
def washington():
	return render_template('Washington.html')

@app.route('/wildscenicriver')
def wildscenicriver():
	return render_template('Wild_Scenic_River.html')

@app.route('/wyoming')
def wyoming():
	return render_template('Wyoming.html')

@app.route('/yellowstonepark')
def yellowstonepark():
	return render_template('Yellowstone_park.html')


if __name__ == '__main__':
	app.run('107.170.39.210','80') # Run application