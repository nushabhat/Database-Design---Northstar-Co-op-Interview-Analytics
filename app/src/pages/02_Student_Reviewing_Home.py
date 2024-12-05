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

# Button to navigate to ML Model Management page
if st.button('Submit Experience', type='primary', use_container_width=True):
    st.switch_page('pages/02_Student_experience.py')