# File to test index.html layout

# Import flask for web applications
import flask as fl

# Numpy for numerical arrays
import numpy as np

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
    return {"Model 1 value ": np.random.randint(1, 5)}

# Tell flask to make model 2 available at /model2
@app.route('/api/model2')
def model2():
    return {"Model 2 value ": np.random.randint(10, 15)}

