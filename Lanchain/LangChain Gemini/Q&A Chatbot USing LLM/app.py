# Q&A Chatbot
from langchain.llms import OpenAI
from langchain_google_genai import GoogleGenerativeAI

#from dotenv import load_dotenv

#load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
os.environ["GOOGLE_API_KEY"] = "AIzaSyBN4-KvKQbf83ooMqZYeVdUKZO6VpNNNNw"


## Function to load OpenAI model and get respones

def get_openai_response(question="I AM AI"):
    # llm=OpenAI(model_name="text-davinci-003",temperature=0.5)
    llm = GoogleGenerativeAI(model="gemini-pro", temperature=0.6)
    response=llm(question)
    return response

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input=st.text_input("Input: ",key="input")
if input:
    response=get_openai_response(input)

submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)




