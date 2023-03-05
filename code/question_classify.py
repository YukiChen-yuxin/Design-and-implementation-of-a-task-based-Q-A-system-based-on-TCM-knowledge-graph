
# coding: utf-8

import numpy as np
import pandas as pd
import jieba
import json
from joblib import dump, load
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import random
from sklearn import metrics
import warnings
warnings.filterwarnings("ignore")

class question_classify():
    #参数
    def __init__(self):
        self.model=load('model/NBmodel.joblib')
        self.tf=load('model/tf-idf.joblib')
        
        
        
    def classify_question(self,test_word):
        test_temp=jieba.cut(test_word)
        tt=''
        for word in test_temp:
            tt+=word+' '
        test_features = self.tf.transform([tt])
        label=self.model.predict(test_features)[0]
        #['L1类_回答方法.txt','L2类_回答症状.txt','L3类_回答释名.txt','L4类_回答气味.txt','L5类_回答子部.txt','L6类_回答部门.txt']
        if label==1:
            return('L1')
        elif label==2:
            return('L2')
        elif label==3:
            return('L3')
        elif label==4:
            return('L4')
        elif label==5:
            return('L5')
        elif label==6:
            return('L6')
        else:
            return(-1)

if __name__=="__main__":
    
    classify = question_classify()
    text = "属于哪个部啊"
    result = classify.classify_question(text)