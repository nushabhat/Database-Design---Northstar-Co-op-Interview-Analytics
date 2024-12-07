import logging
import streamlit as st
from modules.nav import SideBarLinks
import pandas as pd
import os  # Importing the os module
from datetime import datetime
import matplotlib.pyplot as plt

# Set up logging
logger = logging.getLogger(__name__)

# Navigation
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
        avg_extracurriculars = df["num_extracurriculars"].mean()

        # Display statistics
        st.subheader("Average Statistics for Filtered Data")
        st.write(f"- **Average GPA:** {avg_gpa:.2f}")
        st.write(f"- **Average Number of Extracurriculars:** {avg_extracurriculars:.2f}")

        # Generate trends for scatter plot comparison
        attribute1 = st.selectbox("Select Attribute (X-Axis)", options=["gpa", "num_extracurriculars", "num_internships"], index=0)
        attribute2 = st.selectbox("Select Attribute (Y-Axis)", options=["difficulty_rating", "num_academic_extracurriculars"], index=0)

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
