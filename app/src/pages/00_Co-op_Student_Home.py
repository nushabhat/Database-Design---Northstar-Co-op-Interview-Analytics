import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

# Set up Streamlit page layout
st.set_page_config(layout='wide')

# Show appropriate sidebar links for the role of the currently logged-in user
SideBarLinks()

# Page title and header
st.title(f"Hi, {st.session_state['first_name']}...")
st.write('')
st.write('')
st.write('### What interview are you looking to prep for today?')

# Dropdown options for Industry (Replace these with all unique industries)
options1 = [' ', 'Option 1', 'Option 2', 'Option 3']


st.markdown("""
    <style>
        .dropdown-label,
        .input-label {
            font-size: 18px; /* Set font size for all labels */
            margin-bottom: 5px; /* Reduce spacing */
        }
        .streamlit-button {
            font-size: 18px; /* Set font size for button */
        }
        .stTextInput, .stSelectbox {
            font-size: 18px; /* Set font size for input fields */
        }
    </style>
    <div class="dropdown-label">Industry <span style='color: red;'>*</span></div>
""", unsafe_allow_html=True)

# Dropdown menu for Industry
search_input1 = st.selectbox('', options1)
st.write('')

# Input fields with updated labels
st.markdown('<div class="input-label">Company Name</div>', unsafe_allow_html=True)
search_input2 = st.text_input('', placeholder='Enter company name')
st.write('')

st.markdown('<div class="input-label">Role Name</div>', unsafe_allow_html=True)
search_input3 = st.text_input('', placeholder='Enter role name')
st.write('')

if st.button('Search', type='primary', use_container_width=True):
    logger.info(f"Search terms: {search_input1}, {search_input2}, {search_input3}")

    if not search_input1 or search_input1 == ' ':  # Validate dropdown selection
        st.error("Industry field is required. Please select a value.")
    else:
        st.switch_page('pages/03_Co-op_List.py')
