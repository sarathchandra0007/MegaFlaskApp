from flask import render_template
from app import app

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
