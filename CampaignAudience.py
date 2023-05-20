import streamlit as st
import pandas as pd

# Function to read the CSV file from the bucket
def read_csv_from_bucket():
    try:
        df = pd.read_csv("./leads.csv")
        return df
    except Exception as e:
        st.error(f"Error reading CSV file: {e}")

def create_campaign():
    # st.write("Welcome to the Create Email Campaign")
    st.image("./summary.png", use_column_width=True)

    # Button to trigger reading the CSV file
    if st.button("Generate Campaign Audience"):
        df = read_csv_from_bucket()
        if df is not None:
            st.dataframe(df)