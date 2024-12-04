import logging
import requests
import streamlit as st
from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)

st.set_page_config(layout='wide')

SideBarLinks()

st.title("Search for Co-ops")

col1, col2 = st.columns(2)

# Define the API endpoint
API_URL = "http://api:4000/s/industries"


# Fetch industries from the API
def get_industries():
    try:
        print("Hello", flush=True)
        response = requests.get(API_URL,timeout=10)
        print("API request successful", flush=True)
        response.raise_for_status()
        print("Raise for status", flush=True)
        industries = response.json()
        print("Response saved in", flush=True)
        return [""] + industries
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching industries: {e}")
        st.text(f"Debug Info: {e.__class__.__name__} - {e}")
        return [""]



# Get industries dynamically
industries = get_industries()
#st.write(industries)

with col1:
    industry = st.selectbox(
        'Industry:',
        options=industries,  # Dynamically populated options
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

