from flask import Flask, render_template, url_for, request

#flask with small f represents the library itself
#Flask with capital F shows the instance/instance varible for the libray
#render_template is used to return one html file at a time
#url_for is used to return the page as well but automatically. 
#WTForms includes (passwordfield, emailfield, textfield)
#passlib , a library for password. 
#encryption, decryption  (sha256_crypt) 
from wtforms import Form, StringField, EmailField, PasswordField, validators
from passlib.hash import sha256_crypt
import mysql.connector
#from mysql import flask_mysqldb

app = Flask(__name__)

#Flask(__name__) instance function. 
#parameter __name__ is passed through the instance function

mysql = MySQL()
app.config['MYSQL_HOST'] = 'localhost/127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'postdata'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql.init_app(app)



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

class RegisterFrom(Form):
	name = StringField('Name', [validators.length(min=3, max=40)])
	username = StringField('Username', [validators.length(min=3, max=20)])
	email = EmailField('Email', [validators.Email(), validators.length(min=3, max=20)])
	password = PasswordField('Passsword', [validators.length(min=5)])

@app.route('/register', methods=['POST', 'GET'])
def register():
	form = RegisterFrom(request.form)

	if request.method == 'POST' and form.validate():
		name = form.name.data
		username = form.username.data
		email = form.email.data
		password = form.password.data

		#cursor class
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO users(name, username, email, password) VALUES(%s, %s,%s,%s)", (name, username, email, password))
		cur.close()

		flash('You are regsitered. ', 'success')

		return redirect(url_for('login'))

	return render_template('register.html', form=form)

@app.route('/login')
def login():
	return render_template('login.html')

if __name__ == '__main__':
	app.run(debug=True)


#Vistual Studio C++ 2015, 2017
#Database Connectivity 
#Form, type of forms (WTForms)
# password, encrypted (unreadable ) - passlib
#MYSQL, flask-mysqldb, mysql-connector

#render_field 







