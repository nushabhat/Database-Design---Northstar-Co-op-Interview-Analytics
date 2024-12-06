# Home page for students that would like to review a co-op

import logging
import streamlit as st
from modules.nav import SideBarLinks

# Logging setup
logger = logging.getLogger(__name__)

# Set page configuration
st.set_page_config(layout='wide')

# Sidebar navigation
SideBarLinks()

# Title for System Admin Home Page
st.title('Student Reviewing Home')

# Button to navigate to submit expereince
if st.button('Submit Experience', type='primary', use_container_width=True):
    st.switch_page('pages/02_Student_experience.py')

# Button to navigate to access other student functions
if st.button('Main Student Functions', type='primary', use_container_width=True):
    st.switch_page('pages/00_Co-op_Student_Home.py')