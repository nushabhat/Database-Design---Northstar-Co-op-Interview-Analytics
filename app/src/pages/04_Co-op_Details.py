import streamlit as st
import pandas as pd
import requests
from modules.nav import SideBarLinks
from datetime import datetime

# Page config
st.set_page_config(layout="wide")
SideBarLinks()

st.title("Co-op Details")

# Check if a co-op was selected
if 'selected_company_id_co_op_id' not in st.session_state:
    st.error("No co-op selected. Please select a co-op from the search results.")
    if st.button("Back to Search"):
        st.switch_page("pages/03_Co-op_List.py")
else:
    # Fetch co-op details from API
    response = requests.get(f"http://api:4000/s/get_coop_details/{st.session_state['selected_company_id_co_op_id']}")
    
    if response.status_code == 200:
        data = response.json()
        coop = data['coop_details']
        notes = data['notes']
        
        # Display company and role information in a card-like format
        st.markdown("""
        <style>
        .info-card {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Company and Role Details
        with st.container():
            st.markdown('<div class="info-card">', unsafe_allow_html=True)
            st.markdown(f"## {coop['CompanyName']} - {coop['RoleName']}")
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### Company Details")
                st.write(f"**Sector:** {coop['Sector']}")
                st.write(f"**Address:** {coop['CompanyAddress']}")
                
            with col2:
                st.markdown("### Role Details")
                st.write(f"**Industry:** {coop['Industry']}")
                st.write(f"**Interview Rounds:** {coop['InterviewRounds']}")
                st.write(f"**Difficulty Rating:** {coop['DifficultyRating']}/5.0")
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Notes Section
        st.markdown("## Student Notes and Experiences")
        if notes:
            for note in notes:
                with st.expander(f"Note from {note['StudentName']} - {note['DatePublished']}"):
                    st.write(note['Summary'])
                    st.caption(f"Posted by: {note['AdminName'] or 'Unknown Admin'}")
        else:
            st.info("No notes available for this co-op position yet.")
        
        # Action buttons
        st.divider()
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Back to Search Results"):
                st.switch_page("pages/03_Co-op_List.py")
        
    else:
        st.error("Failed to load co-op details. Please try again later.")
        if st.button("Back to Search Results"):
            st.switch_page("pages/03_Co-op_List.py")