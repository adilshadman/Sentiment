import streamlit as st
from textblob import TextBlob
st.sidebar.title("Contact Details")
st.sidebar.markdown("**Gmail:** shad42521@gmail.com")
st.sidebar.markdown("**LinkedIn:** [Shadman adil](https://www.linkedin.com/in/shadmanadil/)",unsafe_allow_html=True)
st.sidebar.markdown("**GitHub:** [Shadman adil](https://github.com/adilshadman?tab=repositories)",unsafe_allow_html=True)
st.sidebar.title("About Project")
st.sidebar.text("""This project aims to analyze
and classify the sentiment of
text data into three categories:
Positive, Negative, and Neutral.   
The goal is to provide businesses
and individuals with insights into
customer feedback and opinions
to make better-informed decisions.""")

st.title("Sentiment Analysis Project")
text=st.text_input("**Enter text**")
btn=st.button("Predict")

if btn:
    blob=TextBlob(text)
    sent=blob.sentiment[0]
    if sent<0:
        st.error("Negative Sentiment")
        st.image("neg_senti.jpg")
    elif sent>0:
        st.success("Positive Sentiment")
        st.image("pos_senti.jpg")
    else:
        st.warning("Neutral Sentiment")
        st.image("neutral_senti.jpg")






    



