import flask
from flask import request
app=flask.Flask(__name__)
app.config['DEBUG']=True

from flask_cors import CORS
CORS(app)

@app.route('/')
def default():
    return'<h1> API server is working </'


@app.route('/predict')
def predict():
    from joblib import dump, load
    model=load('marriage.joblib')
    age_predict=model.predict([[request.args['gender'],
                                request.args['religion'],
                                request.args['mother_tongue'],
                                request.args['profession'],
                                request.args['location'],
                                request.args['country'],
                                request.args['caste1'],
                                request.args['height_cms']])
    
    return str(age_predict)
app.run()
