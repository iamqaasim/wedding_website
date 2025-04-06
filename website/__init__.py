'''
Converts the website folder into a python package so that we can export data between files
'''
# Flask is used to create a quick website backend 
from flask import Flask
# Import connection variables
#from .configurations.connections import *

# Create the flask app
def create_app():
  # App configs
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'secret_key'

  # Since we are using Blueprint all our pages are stored under 'views' and 'auth'
  from .routes.views import views
  from .routes.auth import auth


  # Register the route to access our views ad auth pages
  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/')

 
  return app