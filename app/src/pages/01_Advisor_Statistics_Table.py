import logging
import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import math


# Set up logging
logger = logging.getLogger(__name__)

# Navigation
from modules.nav import SideBarLinks
SideBarLinks()

# Page Title
st.title("Act as Holly Daize, Co-op Advisor for Students")

# Header
st.header("Interview Statistics Dashboard")

# Filters Section
st.subheader("Filter Data")
col1, col2, col3 = st.columns(3)

with col1:
    industry = st.selectbox("Industry", options=["Technology", "Finance", "Healthcare", "Education"], index=0)

with col2:
    company_name = st.text_input("Company Name", placeholder="Enter company name")

with col3:
    role_name = st.text_input("Role Name", placeholder="Enter role name")

# Placeholder for selected filters
st.write("### Selected Filters")
st.write(f"- **Industry:** {industry}")
if company_name:
    st.write(f"- **Company Name:** {company_name}")
if role_name:
    st.write(f"- **Role Name:** {role_name}")

# Load the submissions data
file_path = "dummy_data_advisor.csv"

if os.path.exists(file_path):
    df = pd.read_csv(file_path)

    # Apply filters based on user selection
    if industry:
        df = df[df["industry"] == industry]
    if company_name:
        df = df[df["company_name"].str.contains(company_name, case=False)]
    if role_name:
        df = df[df["role_name"].str.contains(role_name, case=False)]

    # Display filtered data
    st.write(f"### Filtered Data (Total Submissions: {len(df)})")
    st.dataframe(df)

    # Calculate statistics from the filtered data
    if len(df) > 0:
        # Average GPA
        avg_gpa = df["gpa"].astype(float).mean()
        # Average number of extracurriculars
        avg_extracurriculars = math.floor(df["num_extracurriculars"].mean())
        # Find the most common major
        if "major" in df.columns and not df["major"].isnull().all():
            most_common_major = df["major"].value_counts().idxmax()
        else:
            most_common_major = "No data available"

        if "minor" in df.columns and not df["minor"].isnull().all():
            most_common_minor = df["minor"].value_counts().idxmax()
        else:
            most_common_minor = "No data available"

        avg_internships = math.floor(df['num_internships'].astype(int).mean())
        # Display statistics
        st.subheader("Average Statistics for Filtered Data")
        st.write(f"- **Average GPA:** {avg_gpa:.2f}")
        st.write(f"- **Average Number of Extracurriculars:** {avg_extracurriculars:.2f}")
        st.write(f"- **Most Common Major:** {most_common_major}")
        st.write(f"- **Most Common Minor:** {most_common_minor}")
        st.write(f"- **Average Number of Internships:** {avg_internships}")

        st.session_state["industry"] = industry
        st.session_state["company_name"] = company_name
        st.session_state["role_name"] = role_name
        
        # Button to navigate to scatter plot page
        if st.button('Go to Scatter Plot', type='primary', use_container_width=True):
            st.switch_page('pages/01_Advisor_Scatter.py')

        # Button to navigate to histogram page
        if st.button('Go to Histogram', type='primary', use_container_width=True):
            st.switch_page('pages/01_Advisor_Histogram.py')
else:
    st.error("No data found for the selected filters.")

# Logging Information
logger.info("Page rendered successfully.")
