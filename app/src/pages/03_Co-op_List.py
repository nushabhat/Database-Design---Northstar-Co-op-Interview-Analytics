import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks

# Page title
st.set_page_config(layout="wide")

SideBarLinks()

st.title("Co-op Search Results")

# Check if search results and parameters exist in session state
if 'search_results' not in st.session_state or 'search_params' not in st.session_state:
    st.error("No search results found. Please go back and perform a search.")
    
    # Button to go back to the home page
    if st.button("Go Back"):
        st.switch_page("home")
else:
    # Display search criteria as colored ovals
    st.markdown("### Search Criteria:")
    criteria = st.session_state['search_params']
    
    # Use HTML-like formatting for the colored ovals
    criteria_html = f"""
    <div style="display: flex; gap: 10px; margin-bottom: 20px;">
        <div style="background-color: #ffcccb; color: #000; padding: 10px 20px; border-radius: 20px;">Industry: {criteria.get('industry', 'N/A')}</div>
        <div style="background-color: #add8e6; color: #000; padding: 10px 20px; border-radius: 20px;">Company Name: {criteria.get('company_name', 'N/A')}</div>
        <div style="background-color: #90ee90; color: #000; padding: 10px 20px; border-radius: 20px;">Role Name: {criteria.get('role_name', 'N/A')}</div>
    </div>
    """
    st.markdown(criteria_html, unsafe_allow_html=True)
    # Display search results in a nicely formatted table
    results = st.session_state['search_results']
    
    if results:
        st.subheader("Results Found")
        # Convert results to a DataFrame for better display
        results_df = pd.DataFrame(results)
        st.dataframe(results_df)
    else:
        st.info("No results found for your search criteria.")

    # Action buttons
    st.divider()
    col1, _ = st.columns(2)
    
    with col1:
        if st.button("New Search"):
            st.switch_page("pages/00_Co-op_Student_Home.py")
