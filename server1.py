# File to test index.html layout

########## IMPORTS ##########
# Import flask for web applications.
import flask as fl

# Numpy for numerical arrays.
import numpy as np

# pickle for saving and restoring ML models.
import joblib

# For restoring a keras model.
from tensorflow.keras.models import load_model

# Import my polnomial regression model.
polyreg = joblib.load("poly-reg.pkl")
# Need poly features to make a prediction for [[x, x^2, x^3]]
print(polyreg.predict([[23, 529, 12167]])) # shape ok but manually doing polynomial features

# Import my SVM regression model.
svmreg = joblib.load("svm-reg.pkl")


# Import my neural network model.
model = load_model("neural-nw.h5")
# Test make a prediction - ok
print(model.predict([[23]])) 

########## Create a new web application ##########
app = fl.Flask(__name__)

########## Add root app ##########
@app.route('/')
def home():
    # return "Hello Liz"
    return app.send_static_file('index.html')

########## Tell flask to make model 1 available at /model1 ##########
# model 1 is polynomial regression
# file: poly-reg.pkl
# How to get the data into this function? Via the url, goes with request.
@app.route('/api/model1/<int:w>')
# curl test at 127.0.0.1:5000/api/model1/10 ok
def model1(w):
    return {"value": w * 2} # works with curl & on page
    #return {"value": np.random.randint(1, 5)}

    # Make the prediction using our model.

########## Tell flask to make model 2 available at /model2 ##########
# model 2 is support vector machine regression
# file: svm-reg.pkl
# How to get the data into this function? Via the url, goes with request.
@app.route('/api/model2/<int:w>')
# curl test at 127.0.0.1:5000/api/model2/5 ok
def model2(w):
    return {"value": w * w} # works with curl & on page

    # Make the prediction using our model.
    
    
########## Tell flask to make model 3 available at /model3 ##########
# model 3 is a sequential neural network
# file: neural-nw.h5
# How to get the data into this function? Via the url, goes with request.
@app.route('/api/model3/<int:w>')
# curl test at 127.0.0.1:5000/api/model3/5 ok

def model3(w):
    # return "Wind speed is " + str(w) # works with curl
    # return {"value": w * w} # works with curl & on page

    # Make the prediction using our model
    p = model.predict([[w]]) # TypeError: Object of type ndarray is not JSON serializable if try to return this
    print(p) # test - [[99.785995]]
    print(p[0][0]) # test - 99.785995 TypeError: Object of type float32 is not JSON serializable if try this
    return {"value": str(p[0][0])} # Object must be a string
    