from flask import redirect, url_for, render_template
from app import app 



@app.route('/home')
def home():
    return render_template('home.html')