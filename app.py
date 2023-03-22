import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)
#load the model
model1=pickle.load(open('model1.pkl','rb'))
scaler=pickle.load(open('scaling.pkl','rb'))


@app.route('/') #home page
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():  #store the i/p in json format from post method 
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data=scaler.transform(np.array(list(data.values())).reshape(1,-1))
    output=model1.predict(new_data)
    print(output[0])
    return jsonify(output[0])

if __name__=="__main__":
    app.run(debug=True)