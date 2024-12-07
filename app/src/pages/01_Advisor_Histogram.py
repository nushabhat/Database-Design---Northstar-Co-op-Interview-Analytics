import logging
import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

# Set up logging
logger = logging.getLogger(__name__)

from modules.nav import SideBarLinks
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
   
    # Histogram for distribution of attributes
    st.subheader("The Distribution of Attributes")
    # Allow the user to select the attribute to display on the histogram
    attribute_to_plot = st.selectbox(
        "Select an Attribute to Plot",
        options=["graduation_year", "major", "minor"]
    )

    # Convert the selected column to string if necessary
    df[attribute_to_plot] = df[attribute_to_plot].astype(str)

    # Plot the value counts as a bar chart
    fig, ax = plt.subplots(figsize=(5, 3))  # Adjusted size for histogram

    # Plot the distribution of the selected attribute
    df[attribute_to_plot].value_counts().plot(kind="bar", ax=ax)

    # Add title and labels
    plt.title(f"Distribution of {attribute_to_plot.capitalize()}")
    plt.ylabel("Count")
    st.pyplot(fig)  # Display the plot in Streamlit

else:
    st.error("No data found for the selected filters.")

# Footer Section
st.markdown("---")
st.write("Designed for enhanced student counseling and efficient data management.")

# Logging Information
logger.info("Page rendered successfully.")
