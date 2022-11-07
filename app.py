from flask import Flask, render_template, url_for

#flask with small f represents the library itself
#Flask with capital F shows the instance/instance varible for the libray
#render_template is used to return one html file at a time
#url_for is used to return the page as well but automatically. 


app = Flask(__name__)


#Flask(__name__) instance function. 
#parameter __name__ is passed through the instance function


@app.route('/') #it creates a path for the page on the browser
def home(): #function which returns
	return render_template('home.html') #using render_template fun, you return one html page at a time

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')


@app.route('/team')
def team():
	return render_template('team.html')



if __name__ == '__main__':
	app.run(debug=True)





