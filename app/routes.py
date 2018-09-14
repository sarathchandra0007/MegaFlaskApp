from flask import render_template,flash,redirect, url_for
from app import app
from app.forms import LoginForm
@app.route('/')
@app.route('/index')
def index():
    user = {'username':'sarath'}
    posts = [
        {
            'author': {'username':'Rahul'},
            'body': 'Happy Brthday Vinayak'
        },
        {
            'author': {'username':'Suman'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author' : {'username':'Peter'},
            'body' : 'Hey!! Peter..'
        }
    ]
    return render_template('index.html',title='Home',user=user,posts=posts)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login required for user {}, remember_me={}'.format(form.username.data,form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',title='SignIn',form=form)
