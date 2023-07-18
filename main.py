# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 20:44:14 2023

@author: harik
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class model_input(BaseModel):
    
    Gender : int
    Married : int
    Dependents : int
    Education : int
    Self_Employed : int
    ApplicantIncome : int
    CoapplicantIncome :  float
    LoanAmount : float
    Loan_Amount_Term : float
    Credit_History : float 
    Property_Area : int 
    
    

# loading the saved model
loan_model = pickle.load(open('loan_prediction_model.sav','rb'))


@app.post('/loan_prediction')
def diabetes_pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    gen = input_dictionary['Gender']
    mar = input_dictionary['Married']
    dep = input_dictionary['Dependents']
    edu = input_dictionary['Education']
    se = input_dictionary['Self_Employed']
    ai = input_dictionary['ApplicantIncome']
    ci = input_dictionary['CoapplicantIncome']
    la = input_dictionary['LoanAmount']
    lat = input_dictionary['Loan_Amount_Term']
    ch = input_dictionary['Credit_History']
    pa = input_dictionary['Property_Area']


    input_list = [gen, mar, dep, edu, se, ai, ci, la, lat, ch, pa]
    
    prediction = loan_model.predict([input_list])
    
    if prediction[0] == 0:
        return 'Not eligible for loan'
    
    else:
        return 'Eligible for loan'
