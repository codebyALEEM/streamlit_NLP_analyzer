import streamlit as st
import pickle 
import nlp_functions

with open(r"C:\Users\VICTUS\Desktop\mastering git\Practise git\streamlit_NLP_analyzer\nlp_functions.pkl","rb") as f:
    nlp = pickle.load(f)
    
    
st.title("NLP Text Processor")

text = st.text_area("Enter your text here",height=200)

if text:
    col1,col2 = st.columns(2)
    with col1:
        if st.button("Tokenize"):
            st.write(nlp["tokenize"](text))
        if st.button("Stemming"):
            st.write(nlp["stem"](text))       
        if st.button("Lemmatization"):
            st.write(nlp["lemmatize"](text))
            
    with col2:
        if st.button("POS Tagging"):
            st.write(nlp["pos"](text))
        if st.button("Name Entity Recognition"):
            st.write(nlp["ner"](text))
        