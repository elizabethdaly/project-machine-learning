# File to serve up machine learning models using flask
# Front end in index.html
# app.py is a copy of MLserver.py edited to go to PythonAnywhere hopefully

########## IMPORTS ##########
# Import flask for web applications.
import flask as fl

# Numpy for numerical arrays.
import numpy as np

# pickle for saving and restoring ML models.
import joblib

# For restoring a keras model.
from tensorflow.keras.models import load_model

# To fix pythonanywhere probelm
#import sklearn

# Import my polnomial regression model-in same dir
polyreg = joblib.load("/home/elizabethdaly/mysite/poly-reg.pkl")

# Import my SVM regression model and the scaler to apply to x before predict.
svmreg = joblib.load("/home/elizabethdaly/mysite/svm-reg.pkl")
scaler = joblib.load("/home/elizabethdaly/mysite/scalerX.pkl")

# Import my neural network model.
#model = load_model("/home/elizabethdaly/mysite/neural-nw.h5")

########## Create a new web application ##########
app = fl.Flask(__name__)

########## Add root app ##########
@app.route('/')
def home():
    # Access static content over the pre-configured /static/
    return app.send_static_file('index.html')

########## Tell flask to make model 1 available at /model1 ##########
# model 1 is polynomial regression
# file: poly-reg.pkl
# How to get the data into this function? Via the url, goes with request.
@app.route('/api/model1/<int:w>')
# curl test at 127.0.0.1:5000/api/model1/10 ok
def model1(w):
    # Make the prediction using our model with w, w^2, w^3.
    p = polyreg.predict([[w, w ** 2, w ** 3]])
    return {"value": str(p[0])} # Object must be a string.

########## Tell flask to make model 2 available at /model2 ##########
# model 2 is support vector machine regression
# file: svm-reg.pkl
# scaler: scalerX.pkl
@app.route('/api/model2/<int:w>')
# curl test at 127.0.0.1:5000/api/model2/5 ok
def model2(w):
    # Make the prediction using our model.
    p = svmreg.predict(scaler.transform([[w]]))
    return {"value": str(p[0])} # Object must be a string.
   
########## Tell flask to make model 3 available at /model3 ##########
# model 3 is a sequential neural network
# file: neural-nw.h5
# How to get the data into this function? Via the url, goes with request.
# Comment out as errors on PA
#@app.route('/api/model3/<int:w>')
#def model3(w):
#    p = model.predict([[w]]) # TypeError: Object of type ndarray is not JSON serializable if try to return this
#    return {"value": str(p[0][0])} # Object must be a string