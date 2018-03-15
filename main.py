from flask import Flask,render_template
from sqlalchemy import create_engine,Column, String, Integer, Date,asc, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import *

app = Flask(__name__)

@app.route('/FeatureRequestDetails')
def featureRequestDetails():
    """ featureRequestDetails function is used to display featureRequestDetails html page"""
    return render_template('featureRequestDetails.html')

@app.route('/')
def featureRequestForm():
    """ featureRequestForm function is used to display featureRequestForm html page"""
    return render_template('featureRequestForm.html')

app.config.from_object(Config)
	
if __name__ == '__main__':
  app.run()
