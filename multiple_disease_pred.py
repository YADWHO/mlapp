# -*- coding: utf-8 -*-
"""
Created on Wed May 22 18:22:56 2024

@author: yadhu
"""
import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import warnings
warnings.filterwarnings('ignore')

#loading the saved models

diabetes_model=pickle.load(open("diabetes_model.sav",'rb'))
heart_model=pickle.load(open("heart_model.sav",'rb'))
parkinsons_model=pickle.load(open("parkinsons_model.sav",'rb'))

#creating the sidebars for navigation

with st.sidebar:
    
    selected=option_menu('Multiple Disease Prediction System',['Diabetes Prediction','Heart Disease Prediction','Parkinsons prediction'],
                         icons=['activity','heart','person'],default_index=0)

if(selected=='Diabetes Prediction'):
    st.title('Diabetes Prediction')
    
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies=st.text_input("No of Pregnancies")
    with col2:
        
        Glucose=st.text_input("Glucose Level")
    with col3:
        BloodPressure=st.text_input("Blood Pressure")
    
    with col1:
        
        SkinThickness=st.text_input("Skin Thickness")
    with col2:
        Insulin=st.text_input("Insulin level")
    
    with col3:
        BMI=st.text_input("BMI")
    with col1:
        
        DiabetesPedigreeFunction=st.text_input("DPF")
    with col2:
        Age=st.text_input("Age")
        
    
    Pregnancies=int(Pregnancies)
    Glucose=int(Glucose)
    BloodPressure=int(BloodPressure)
    SkinThickness=int(SkinThickness)
    Insulin=int(Insulin)
    BMI=float(BMI)
    DiabetesPedigreeFunction=float(DiabetesPedigreeFunction)
    Age=int(Age)
    
    #code for prediction
    d_diagnosis=''
    
    #creating a button
    if(st.button('Diabetes Test Result')):
        inp=[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
        #input to np
        input_np=np.asarray(inp)

        #reshaping input
        input_rs=input_np.reshape(1,-1)

        #predicting
        pred=diabetes_model.predict(input_rs)

        if(pred[0]==0):
            d_diagnosis= "not diabetic"
        else:
            d_diagnosis= "diabetic"
    
    st.success(d_diagnosis)
    
    
      
    
if(selected=='Heart Disease Prediction'):
    st.title('Heart Disease Prediction')
    
    age=st.text_input("age in years")
    sex=st.text_input("sex:1 for male 0:for female")
    cp=st.text_input("chest pain type")
    trestbps=st.text_input("resting blood pressure (in mm Hg on admission to the hospital")
    chol=st.text_input("serum cholestoral in mg/dl")
    fbs=st.text_input("fasting blood sugar &gt; 120 mg/dl) (1 = true; 0 = false")
    restecg=st.text_input("resting electrocardiographic results")
    thalach=st.text_input("maximum heart rate achieved")
    exang=st.text_input("exercise induced angina (1 = yes; 0 = no)")
    oldpeak=st.text_input("ST depression induced by exercise relative to rest")
    slope=st.text_input("the slope of the peak exercise ST segment")
    ca=st.text_input("number of major vessels (0-3) colored by flourosopy")
    thal=st.text_input("thal:1 = normal; 2 = fixed defect; 3 = reversable defect")
    
    age=int(age)
    sex=int(sex)
    cp=int(cp)
    trestbps=int(trestbps)
    chol=int(chol)
    fbs=int(fbs)
    restecg=int(restecg)
    thalach=int(thalach)
    exang=int(exang)
    oldpeak=float(oldpeak)
    slope=int(slope)
    ca=int(ca)
    thal=int(thal)
    
    h_diagnosis=''
    
    #creating a button
    if(st.button('Heart Test Result')):
        inp=[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        #input to np
        input_np=np.asarray(inp)

        #reshaping input
        input_rs=input_np.reshape(1,-1)

        #predicting
        pred=heart_model.predict(input_rs)

        if(pred[0]==0):
            h_diagnosis= "no heart disease"
        else:
            h_diagnosis= "heart disease"
    
    st.success(h_diagnosis)
      
    
if(selected=='Parkinsons prediction'):
    st.title('Parkinsons Prediction')
    
    Fo=st.text_input("Average vocal fundamental frequency")
    Fhi=st.text_input("Maximum vocal fundamental frequency")
    Flo=st.text_input("Minimum vocal fundamental frequency")
    Jitter=st.text_input("MDVP:Jitter %")
    Jitter_abs=st.text_input("MDVP:Jitter abs")
    RAP=st.text_input("MDVP:RAP")
    PPQ=st.text_input("MDVP:PPQ")
    DDP=st.text_input("Jitter:DDP")
    Shimmer=st.text_input("MDVP:Shimmer")
    Shimmer_dB=st.text_input("MDVP:Shimmer db")
    APQ3=st.text_input("Shimmer:APQ3")
    APQ5=st.text_input("Shimmer APQ5")
    APQ=st.text_input("MDVP:APQ")
    DDA=st.text_input("Shimmer:DDA")
    NHR=st.text_input("NHR")
    HNR=st.text_input("HNR")
    RPDE=st.text_input("RPDE")
    DFA=st.text_input("DFA")
    Spread1=st.text_input("Spread1")
    Spread2=st.text_input("Spread2")
    D2=st.text_input("D2")
    PPE=st.text_input("PPE")
      
    
    Fo=float(Fo)
    Fhi=float(Fhi)
    Flo=float(Flo)
    Jitter=float(Jitter)
    Jitter_abs=float(Jitter_abs)
    RAP=float(RAP)
    PPQ=float(PPQ)
    DDP=float(DDP)
    Shimmer=float(Shimmer)
    Shimmer_dB=float(Shimmer_dB)
    APQ3=float(APQ3)
    APQ5=float(APQ5)
    APQ=float(APQ)
    DDA=float(DDA)
    NHR=float(NHR)
    HNR=float(HNR)
    RPDE=float(RPDE)
    DFA=float(DFA)
    Spread1=float(Spread1)
    Spread2=float(Spread2)
    D2=float(D2)
    PPE=float(PPE)
    
    p_diagnosis=''
    
    #creating a button
    if(st.button('Parkinsons Test Result')):
        inp=[Fo,Fhi,Flo,Jitter,Jitter_abs,RAP,PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,Spread1,Spread2,D2,PPE]
        #input to np
        input_np=np.asarray(inp)

        #reshaping input
        input_rs=input_np.reshape(1,-1)

        #predicting
        pred=parkinsons_model.predict(input_rs)

        if(pred[0]==0):
            p_diagnosis= "No Parkinsons"
        else:
            p_diagnosis= "Parkinsons"
    
    st.success(p_diagnosis)