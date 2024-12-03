import logging
import requests
import streamlit as st
from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)

st.set_page_config(layout='wide')

SideBarLinks()

st.title("Search for Co-ops")

col1, col2 = st.columns(2)

with col1:
    industry = st.selectbox(
        'Industry:',
        options=['', 'Tech', 'Healthcare', 'Finance', 'Education'],  # Example options
        help='Select the industry you are interested in'
    )
with col2:
    company_name = st.text_input(
        'Company Name:',
        placeholder='Enter the company name'
    )

role_name = st.text_input('Role Name:', placeholder='Enter the role you want')

logger.info(f'Industry: {industry}')
logger.info(f'Company Name: {company_name}')
logger.info(f'Role Name: {role_name}')

if st.button('Search', type='primary', use_container_width=True):
    if not industry:
        st.error("Please select an industry to search.")
    else:
        api_url = "http://api:4000/s/search_coops"
        params = {
            "industry": industry,
            "company_name": company_name,
            "role_name": role_name
        }
        try:
            response = requests.get(api_url, params=params)
            response.raise_for_status()  # Check for request errors
            results = response.json()

            # Store results in session state
            st.session_state['search_results'] = results
            st.session_state['search_params'] = params

            st.switch_page("pages/03_Co-op_List.py")
        except requests.exceptions.RequestException as e:
            st.error(f"Failed to fetch search results: {e}")