from flask import Blueprint,jsonify,request
import numpy as np
import pandas as pd
import gensim
from nltk.stem import PorterStemmer 
from nltk.tokenize import RegexpTokenizer
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import gensim
from gensim.parsing.preprocessing import strip_numeric 
from gensim.parsing.preprocessing import strip_non_alphanum
from gensim.parsing.preprocessing import strip_punctuation
from gensim.parsing.preprocessing import strip_punctuation2
from gensim.parsing.preprocessing import strip_multiple_whitespaces
from gensim.parsing.preprocessing import strip_tags
from gensim.parsing.preprocessing import stem_text
from gensim.parsing.preprocessing import preprocess_string

model_predictor= Blueprint('model_predictor',__name__)
model =pickle.load(open('g', 'rb'))
v=pickle.load(open("tb","rb"))
ratings=[0,1]
filters=[strip_numeric,strip_multiple_whitespaces,strip_non_alphanum,strip_punctuation,strip_punctuation,strip_punctuation2,strip_tags,stem_text]


def clean(string):
     words=preprocess_string(string,filters)
     return " ".join(word.lower() for word in words)

st=PorterStemmer()
tk=RegexpTokenizer(r'[a-zA-z\']+')
#v=TfidfVectorizer(stop_words='english',analyzer="word")
def tokenize(te):
    return[st.stem(word) for word in tk.tokenize(te.lower())]      

@model_predictor.route('/predict', methods=["POST"])
def predict_values():
    content = request.get_json()
    predstring = content["input"]
    print("hello")
    print("hello")
    gf=clean(predstring)
    rk=tokenize(gf)
    x=v.transform(rk)
    r=model.predict(x) 
    print("hello")
    print("PREDICTIONS :")
    print(r)
    return jsonify(
    {
      "review" : str(r[0])
    }             
            
)
