import streamlit as st 
import pandas as pd
import random

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

openai_api_key = "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"

# load data
df = pd.read_csv("./leads.csv")

def generate():

    # App framework
    st.title('Campaing Email Generator')
    prompt = st.text_input('Enter customer id:') 

    # Llms
    llm = OpenAI(openai_api_key=openai_api_key, temperature=0.7)

    if prompt: 
        customer = df[df['lead_id'] == prompt]
        utm_source = customer['lead_origin'].values[0]
        funnel_stage = random.choice(['awareness','consideration','conversion'])
        product = customer['lead_business_segment'].values[0]
        user_persona = random.choice(['Tech Enthusiast','Fashionista','Foodie','Sports Fanatic','Traveler','Movie Buff','Music Lover','Bookworm','Fitness Enthusiast','Gamer'])
        interest = customer['lead_business_segment'].values[0]

        input_template = "Write a personalized email with 200 words limit to persuade a customer to buy a product with the information \n \
            funnel stage={funnel_stage}\n \
            UTM Source={utm_source}\n \
            Product={product}\n \
            User Persona={user_persona}\n \
            Interest={interest}"\
            .format(funnel_stage=funnel_stage, utm_source=utm_source, product=product, user_persona=user_persona, interest=interest)

        st.text_area("Request to generate email:", value=input_template, height=200)
            
        generated_email = llm(prompt=input_template)
        st.text_area("Generated email", value=generated_email, height=600)

