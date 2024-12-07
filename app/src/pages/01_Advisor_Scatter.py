import logging
import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
from modules.nav import SideBarLinks


# Set up logging
logger = logging.getLogger(__name__) 

# Navigation
SideBarLinks()

# Load the submissions data
file_path = "dummy_data_advisor.csv"

if os.path.exists(file_path):
    df = pd.read_csv(file_path)

    industry = st.session_state.get("industry", None)
    company_name = st.session_state.get("company_name", None)
    role_name = st.session_state.get("role_name", None)

     # Apply filters
    if industry:
        df = df[df["industry"] == industry]
    if company_name:
        df = df[df["company_name"].str.contains(company_name, case=False)]
    if role_name:
        df = df[df["role_name"].str.contains(role_name, case=False)]

    # Generate trends for scatter plot comparison
    attribute1 = st.selectbox("Select Attribute (X-Axis)", options=["gpa", "num_extracurriculars", "num_internships"], index=0)
    attribute2 = st.selectbox("Select Attribute (Y-Axis)", options=["difficulty_rating"], index=0)

    # Simulate Scatter Plot
    trend_data = df[[attribute1, attribute2]].dropna()  # Drop NaN values if any
    st.write(f"#### Comparison: {attribute1} vs {attribute2}")

    # Plotting a scatter plot using matplotlib
    plt.figure(figsize=(5, 3))  # Adjusted size to make it smaller
    plt.scatter(trend_data[attribute1], trend_data[attribute2], color='blue', alpha=0.6)
    plt.title(f'{attribute1} vs {attribute2}')
    plt.xlabel(attribute1)
    plt.ylabel(attribute2)
    st.pyplot(plt)  # Display the plot in Streamlit

else:
    st.error("No data found for the selected filters.")

# Logging Information
logger.info("Page rendered successfully.")
