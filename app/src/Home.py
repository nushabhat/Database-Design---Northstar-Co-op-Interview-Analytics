##################################################
# This is the main/entry-point file for the 
# sample application for your project
##################################################

# Set up basic logging infrastructure
import logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# import the main streamlit library as well
# as SideBarLinks function from src/modules folder
import streamlit as st
from modules.nav import SideBarLinks

# streamlit supports reguarl and wide layout (how the controls
# are organized/displayed on the screen).
st.set_page_config(layout = 'wide')

# If a user is at this page, we assume they are not 
# authenticated.  So we change the 'authenticated' value
# in the streamlit session_state to false. 
st.session_state['authenticated'] = False

# Use the SideBarLinks function from src/modules/nav.py to control
# the links displayed on the left-side panel. 
# IMPORTANT: ensure src/.streamlit/config.toml sets
# showSidebarNavigation = false in the [client] section
SideBarLinks(show_home=True)

# ***************************************************
#    The major content of this page
# ***************************************************

# set the title of the page and provide a simple prompt. 
logger.info("Loading the Home page...")
st.title('NORTHSTAR')
st.write('\n\n')
st.write('### Welcome to NorthStar Technologies! As which user would you like to log in?')

# For each of the user personas for which we are implementing
# functionality, we put a button on the screen that the user 
# can click to MIMIC logging in as that mock user. 

# if st.button("Act as Emma, a Student Looking for a Co-op", 
#             type = 'primary', 
#             use_container_width=True):
#     # when user clicks the button, they are now considered authenticated
#     st.session_state['authenticated'] = True
#     # we set the role of the current user
#     st.session_state['role'] = 'co-op_student'
#     # we add the first name of the user (so it can be displayed on 
#     # subsequent pages). 
#     st.session_state['first_name'] = 'Emma'
#     # finally, we ask streamlit to switch to another page, in this case, the 
#     # landing page for this particular user type
#     logger.info("Logging in as Co-op Student Persona")
#     st.switch_page('pages/00_Co-op_Student_Home.py')

# if st.button('Act as Holly, a Co-op Advisor', 
#             type = 'primary', 
#             use_container_width=True):
#     st.session_state['authenticated'] = True
#     st.session_state['role'] = 'co-op_advisor'
#     st.session_state['first_name'] = 'Holly'
#     st.switch_page('pages/01_Co-op_Advisor_Home.py')

# if st.button('Act as System Administrator', 
#             type = 'primary', 
#             use_container_width=True):
#     st.session_state['authenticated'] = True
#     st.session_state['role'] = 'administrator'
#     st.session_state['first_name'] = 'SysAdmin'
#     st.switch_page('pages/20_Admin_Home.py')
    
# if st.button('Act as Raaya, a Student with Co-op Experience', 
#             type = 'primary', 
#             use_container_width=True):
#     st.session_state['authenticated'] = True
#     st.session_state['role'] = 'student_reviewing'
#     st.session_state['first_name'] = 'Raaya'
#     st.switch_page('pages/02_Student_Reviewing_Home.py')

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cabin:wght@400;700&display=swap');

    body {
        font-family: 'Cabin', sans-serif;
    }

    .button-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        margin-top: 30px; /* Adds spacing below the title */
    }

    .custom-button {
        display: inline-block;
        width: 400px; /* Button width */
        height: 100px; /* Increased button height */
        margin: 20px 0; /* Spacing between buttons */
        font-size: 20px; /* Larger font size */
        font-weight: bold;
        color: white;
        background-color: #007bff; /* Streamlit blue */
        border: none;
        border-radius: 15px;
        text-align: center;
        line-height: 100px; /* Vertically centers the text */
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .custom-button:hover {
        background-color: #0056b3; /* Hover color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Button container to center all buttons
st.markdown('<div class="button-container">', unsafe_allow_html=True)

if st.button("Act as Emma, a Student Looking for a Co-op", key="emma"):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'co-op_student'
    st.session_state['first_name'] = 'Emma'
    st.experimental_rerun()

if st.button("Act as Raaya, a Student with Co-op Experience", key="raaya"):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'student_reviewing'
    st.session_state['first_name'] = 'Raaya'
    st.experimental_rerun()

if st.button("Act as Holly, a Co-op Advisor", key="holly"):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'co-op_advisor'
    st.session_state['first_name'] = 'Holly'
    st.experimental_rerun()

if st.button("Act as System Administrator", key="admin"):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'administrator'
    st.session_state['first_name'] = 'SysAdmin'
    st.experimental_rerun()

# Close the button container div
st.markdown('</div>', unsafe_allow_html=True)