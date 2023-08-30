import os.path
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
SECRET_KEY = '123456789'
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir,'app.db')