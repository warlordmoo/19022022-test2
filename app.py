#!/usr/bin/env python
# coding: utf-8

# In[31]:


from flask import Flask


# In[32]:


app = Flask(__name__)


# In[33]:


from flask import request, render_template
import  joblib

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        rates = request.form.get("rates")
        print (rates)
        model = joblib.load("DBSReg")
        pred = model.predict ([[float(rates)]])
        s1 = "Predict DBS Share price base on Linear Regression model is : " + str(pred[0][0])
        model = joblib.load("DBSDT")
        pred = model.predict ([[float(rates)]])
        s2 = "Predict DBS Share price base on Decision Tree model is : " + str(pred[0])
        model = joblib.load("DBSNN")
        pred = model.predict ([[float(rates)]])
        s3 = "Predict DBS Share price base on Neural Network model is : " + str(pred[0])
        return(render_template("index.html", result1=s1, result2=s2, result3=s3))
    else:
        return(render_template("index.html", result1="2", result2="2", result3="2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




