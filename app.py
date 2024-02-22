import streamlit as st
import pickle
import pandas as pd

pickle_in = open("classifier.pkl",'rb')
classifier = pickle.load(pickle_in)

def predict_cc_fraud(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o):
    prediction = classifier.predict([[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o]])
    print(prediction)
    return prediction

def main():
    st.title('Credit Card Detection')
    st.divider()
    # Prediction Model
    st.subheader('Model for Prediction',divider='rainbow')
    a = st.text_input("Input V1:","Type Here")
    b = st.text_input("Input V2:", "Type Here")
    c = st.text_input("Input V3:", "Type Here")
    d = st.text_input("Input V4:", "Type Here")
    e = st.text_input("Input V5:", "Type Here")
    f = st.text_input("Input V6:", "Type Here")
    g = st.text_input("Input V7:", "Type Here")
    h = st.text_input("Input V9:", "Type Here")
    i = st.text_input("Input V10:", "Type Here")
    j = st.text_input("Input V11:", "Type Here")
    k = st.text_input("Input V12:", "Type Here")
    l = st.text_input("Input V14:", "Type Here")
    m = st.text_input("Input V16:", "Type Here")
    n = st.text_input("Input V17:", "Type Here")
    o = st.text_input("Input V18:", "Type Here")

    result = ''
    if st.button("Predict"):
        result=predict_cc_fraud(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o)
        if result == [0]:
            st.text('This is not a Fraud')
        else:
            st.text('This is a Fraud')
    st.success("The Prediction is {}".format(result))
    st.divider()

if __name__=='__main__':
    main()
