from app import app,db
from flask import render_template

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html')

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()   #We get 505 status code error because of not commiting
    return render_template('500.html')
