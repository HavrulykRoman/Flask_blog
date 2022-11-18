from flask import render_template, flash, redirect, url_for
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog import app



posts = [
    {'author': 'Jon Doe',
     'title': 'First post',
     'content': 'First post content',
     'data_posted': 'November 7, 2022'},
    {'author': 'Ivan Petriv',
     'title': 'Second post',
     'content': 'Second post content',
     'data_posted': 'November 7, 2022'}
]

@app.route('/')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'test@email.com' and form.password.data == '12345':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)
