'''
This is file contains all the website general routes.
We are using Blueprints to organize our routes.


'''

# Blueprint is used to sort our routes
# Render_template is used to render the html pages
# Request is used to get POST data
# Session is used to handle session database_name
# Redirect is used to redirect pages
# Url_for is used to get the url for a route
# Flash is used to flash success or error messages
from flask import Blueprint, render_template, request, session, redirect, url_for, flash

# Create the blueprint views
views = Blueprint('views',__name__)


# Create Home route
@views.route('/')
def home():
  '''
  Create a route for the Home page

  Functionality:
    clickable cards to navigate to different pages/sections of the website

  Return:
    clickable buttons to navigate to different pages/sections of the website
  '''
  return render_template("home.html")