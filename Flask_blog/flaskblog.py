from flask import Flask , render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)



app.config['SECRET_KEY'] = 'af2350781f78dff43c07c0c41cad0453'

posts = [
	{
		'author':'Kishore',
		'title':'Blog_Post 1',
		'content':'First post',
		'date':'April 20'
	},
	{
		'author':'K',
		'title':'Blog_Post 2',
		'content':'second post',
		'date':'may 20'
	}


]



@app.route("/")
def hello():
	return '<h1> Hello World </h1>'

@app.route("/home")
def home():
	return render_template('home.html',posts=posts)


@app.route("/about")
def about():
	return render_template('about.html')



@app.route("/register", methods = ['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash('Account created for {}!'.format(form.username.data),'success')
		return redirect(url_for('home'))
	return render_template('register.html',title = 'Register', form=form)

@app.route("/login",methods = ['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password' :
			flash('you have been logged in','success')
			return redirect(url_for('home'))
		else:
			flash("Login Unsuccesfull. check username and password",'danger')
			
	return render_template('login.html',title = 'Login', form=form)





if __name__ == '__main__':
	app.run(debug = True)