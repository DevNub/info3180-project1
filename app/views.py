"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import os
from app import app, db
import datetime
from flask import render_template, request, redirect, url_for, flash, abort

from werkzeug.utils import secure_filename

from .forms import UploadForm

from flask_login import login_user, logout_user, current_user, login_required
from app.models import UserProfile


now = datetime.datetime.now() # today's date
join_date = datetime.date(2019, 2, 7) # a specific date 

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
    return render_template('about.html', name="INFO3180 Project 1")


@app.route('/user')
def user():
    """Render the profile page."""
    date=format_date_joined(join_date)
    return render_template('user.html', name="Mickey Mouse", joindate=date, loca="Clubhouse, Disney", usern="doubleM")
    
    
@app.route('/profiles')
def profiles():
    """Render page with uploaded profiles"""
    filename='filename'
    return render_template('profiles.html', filename=filename)


@app.route('/profile', methods=['POST', 'GET'])
def profile():
    # Instantiate your form class
    form = UploadForm()
    # Validate file upload on submit
    if request.method == 'POST' and profile.validate_on_submit():
        # Get file data and save to your uploads folder
        photo = form.upload.data # we could also use request.files['photo']
        description = form.description.data
        
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        flash('File Saved', 'success')
        return redirect(url_for('home'))

    return render_template('profile.html', form=form)
    
    
    
    
###
# The functions below should be applicable to all Flask apps.
###
#Get uploaded images 
def get_uploaded_images():
    fileList = []
    rootdir = os.getcwd()
    print (rootdir)
    for subdir, dirs, files in os.walk(rootdir + '/some/folder'):
        for file in files:
            fileList.append(os.path.join(subdir, file))
    return render_template('files.html', fileList=fileList)



# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error), 'danger')


def format_date_joined(date):
    """ Returns Month, Year from a given date """
    newdate = date.strftime("%B, %Y")
    return newdate
    
@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
