
from flask import Flask, redirect, request, render_template
import pickle
import numpy as np
import pandas as pd

app=Flask(__name__)

@app.route("/")
def fun1():
    return render_template("info.html")

@app.route("/predict", methods = ["post"])
def fun2():
    nm = request.form['name']
    age = int(request.form['age'])
    sex = request.form['gender']
    bmi = int(request.form['bmi'])
    children = int(request.form['num_child'])
    smoker = request.form['smoker']
    region = request.form['region'] 
 
    health_dict = { 'age': [age],
        'sex': [sex],
       'bmi':[bmi],
        'children': [children],
        'smoker': [smoker],
        'region': [region]
              }
    
    df_test = pd.DataFrame(health_dict)

    mymodel = pickle.load(open('premium_pred.pkl', "rb"))
    premium = round(mymodel.predict(df_test)[0],2)
    
    #return "<h1> hi {} <br/> your predicted Premium Amount is {} </h1>".format(nm,premium)
    #return f"<h1> hi {nm} <br/> your predicted Premium Amount is {premium} </h1>"
    #return f"<h1> hi "+nm+"<br/> your predicted Premium Amount is "+premium+"</h1>"
    return render_template("second.html", name = nm , premium = premium )

    
if __name__ == "__main__" :
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=8080)

