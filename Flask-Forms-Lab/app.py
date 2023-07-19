from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

users = {"siwarha": "123", "tamar" : "T000", "ella": "Ella123", "avinoam":"Avi456"}
facebook_friends=["ella","avinoam","ido", "yael", "nili", "naomi", "milky"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')

	else:

		username2 = request.form['username'].lower()
		password2 = request.form['password']

		if username2 in users:
			if users[username2] == password2:
				return redirect(url_for('home'))
		
			else: 
				return render_template('login.html')
				
		else:
			return render_template('login.html')
			

@app.route('/home')  # '/' for the default page
def home():
	return render_template('home.html', friends = facebook_friends)

       
@app.route('/friend_exists/<string:name>')  # '/' for the default page
def friend_exists(name):
	if name.lower() in facebook_friends:
		return render_template('friend_exists.html', result = "True")
	else:
		return render_template('friend_exists.html', result = "False")



  



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
