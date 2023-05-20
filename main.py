import streamlit as st
from streamlit_option_menu import option_menu

import CampaignAudience, Home, GenerateEmail

v_menu=["Home", "Create Audiences", "Generate Email"]

with st.sidebar:

    # st.header("Select Option")

    selected = option_menu(
        menu_title=None,  # required
        options=v_menu,  # required
        icons=None,  # optional
        menu_icon="menu-down",  # optional
        default_index=0,  # optional
    )

if selected=="Home":
    Home.create()

if selected=="Create Audiences":
    CampaignAudience.create_campaign()

if selected=="Generate Email":
    GenerateEmail.generate()