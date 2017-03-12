"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app
from app import db
from flask import render_template, request, redirect, url_for, flash, session, abort, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from forms import SignupForm
from models import UserProfile
from werkzeug.utils import secure_filename
import time
import uuid



###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")
    
@app.route('/profile', methods=['POST','GET'])
def newprofile():
    """Creates new profile"""
    
    if request.method == 'POST':
        uid = str(uuid.uuid4().fields[-1])[:8]
        created = time.strftime('%Y/%b/%d')
        fname = request.form['first_name']
        lname = request.form['last_name']
        age = request.form['age']
        bio =request.form['bio']
        gender =request.form['gender']
        
        
        profilepic = request.files['file']
        if profilepic:
            uploadfolder = app.config['UPLOAD_FOLDER']
            filename = secure_filename(profilepic.filename)
            profilepic.save(os.path.join(uploadfolder, filename))
        user = UserProfile(userid= uid, first_name=fname, last_name=lname, age = age, gender=gender, bio=bio, created = created, pic=profilepic.filename)
        db.session.add(user)
        db.session.commit()
        flash('New User was successfully added')
        return redirect(url_for('home'))
    return render_template('Profileform.html')
    


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
