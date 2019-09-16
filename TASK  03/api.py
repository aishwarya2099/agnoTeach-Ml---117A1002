from flask import Blueprint,jsonify,request
import numpy as np
import pandas as pd
import gensim
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
grec_predictor= Blueprint('grec_predictor',__name__)
grec =pickle.load(open('g', 'rb'))
v=pickle.load(open("tb","rb"))
#ratings=[0,1]
@grec_predictor.route('/predict', methods=["POST"])
def predict_values():
    content = request.get_json()
    predstring = content["input"]
    print("hello")
    print("hello")
    print("hello")
    r=grec(predstring)
    print("PREDICTIONS :")
    print(r)
    return jsonify(
    {
      "review" : str(r[0])
    }             
            
)