import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
app = Flask(__name__)
model = pickle.load(open('profit.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = [[int(x) for x in request.form.values()]]
    prediction = model.predict(x_test)
    print(prediction)
    output=prediction[0]
    
    if(output==0):
        return render_template('index.html', prediction_text='This is a suspicious website')
    elif(output==-1):
         return render_template('index.html', prediction_text='This is a Phishing website')
    else:
        return render_template('index.html', prediction_text='This is a legitimate website')
if __name__=="__main__":
    app.run(debug=True)