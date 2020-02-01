from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
####### Database#######

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/somil/Desktop/corona/corona.db'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:////' + os.path.join(basedir, 'corona.db')

db = SQLAlchemy(app)


#class dynamic_map(db.Model):
#    pass

###### Route when nothing is specified in the url######
@app.route('/')
def index():
    return render_template('base.html')



if __name__ == '__main__':
    app.run(debug = True)
