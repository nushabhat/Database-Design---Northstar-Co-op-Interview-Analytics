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
st.title('System Admin Home Page')

# Button to navigate to ML Model Management page
if st.button('Update ML Models', type='primary', use_container_width=True):
    st.switch_page('pages/21_ML_Model_Mgmt.py')

# Button to navigate to Survey Questions Management page
if st.button('Update Survey Questions', type='primary', use_container_width=True):
    st.switch_page('pages/22_Survey_Questions_Mgmt.py')

# Button to navigate to Admin Users Mgmt page
if st.button('Preview Users', type='primary', use_container_width=True):
    st.switch_page('pages/23_Admin_Users_Mgmt.py')
    