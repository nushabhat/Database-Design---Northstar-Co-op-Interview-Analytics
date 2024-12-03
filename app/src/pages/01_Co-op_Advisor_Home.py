#home page for co-op advisors

# home page for students that would like to review a co-op
import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import pandas as pd
import os  # Importing the os module
from datetime import datetime

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

# Graphical Section
st.subheader("Interview Trends")
st.write("Explore data trends based on selected attributes:")

# Placeholder chart (scatter plot example)
st.write("#### Attribute Comparison")
attribute1 = st.selectbox("Select Attribute (X-Axis)", options=["GPA", "Years of Experience", "Leadership Roles"], index=0)
attribute2 = st.selectbox("Select Attribute (Y-Axis)", options=["Acceptance Rate", "Interview Success", "Offers Received"], index=0)

# Simulated Scatter Plot
data = pd.DataFrame({
    attribute1: [3.2, 3.4, 3.6, 3.8, 4.0],
    attribute2: [60, 65, 70, 75, 80]
})
st.line_chart(data)

# Average Acceptance Statistics Section
st.subheader("Average Acceptance Statistics")
st.write(
    """
    - **3.67 GPA**
    - **2+ Extracurriculars**
    - **1+ Leadership Positions**
    - **Finance Major**
    - **2 Previous Co-ops**
    """
)

# Footer Section
st.markdown("---")
st.write("Designed for enhanced student counseling and efficient data management.")

# Logging Information
logger.info("Page rendered successfully.")

