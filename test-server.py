# File to test index.html layout

# Import flask for web applications
import flask as fl

# Numpy for numerical arrays
import numpy as np

# pickle for saving and restoring ML models
import joblib

# For restoring a keras model
from tensorflow.keras.models import load_model

# Import my polnomial regression model
polyreg = joblib.load("poly-reg.pkl")
# Need poly features to make a prediction for [[x, x^2, x^3]]
print(polyreg.predict([[23, 529, 12167]])) # shape ok but manually doing poly feat

# Import my SVM regression model
svmreg = joblib.load("svm-reg.pkl")

# Import my neural network model
model = load_model("neural-nw.h5")
# Test make a prediction - ok
print(model.predict([[23]])) 

# Create a new web application
app = fl.Flask(__name__)

# Add root app
@app.route('/')
def home():
    # return "Hello Liz"
    return app.send_static_file('index.html')

# Tell flask to make model 1 available at /model1
@app.route('/api/model1')
def model1():
    return {"value": np.random.randint(1, 5)}

# Tell flask to make model 2 available at /model2
@app.route('/api/model2')
def model2():
    return {"value": np.random.randint(10, 15)}

