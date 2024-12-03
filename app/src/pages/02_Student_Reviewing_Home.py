# home page for students that would like to review a co-op
import logging
logger = logging.getLogger(__name__)

import streamlit as st
import requests
from modules.nav import SideBarLinks
import pandas as pd
import os  # Importing the os module
from datetime import datetime

SideBarLinks()

# Navigation to the experience submission page from another page
st.title("Experience Submission")

# Form for experience submission
with st.form("experience_form"):
    st.header("Experience Submission")
    # Collecting Company Information
    company_name = st.text_input("1. Company Name")
    role_name = st.text_input("2. Role Name")
    interview_date = st.text_input("3. Month/Year of Interview (e.g., Oct 2024)")
    industry = st.text_input("4. Company Industry")

    # Interview types selection
    interview_types = st.multiselect(
        "5. Please select interview types",
        ["Excel workbook", "Technical questions", "Leetcode questions", "Case Interview", "Behavioral"],
    )

   # Difficulty rating
    st.write("6. How difficult would you rate this interview?")

    # Mapping the options to decimal values
    difficulty_rating = st.radio(
        "",
        options=[1.0, 2.0, 3.0, 4.0, 5.0],  # Use decimal values instead of emojis
        index=2,  # Default to middle value (3.0)
        format_func=lambda x: f"{x}"  # Option label with value and description
    )

    # Elaboration on difficulty
    difficulty_elaboration = st.text_area("7. Please elaborate on your rating in question 6")

    # Academic statistics
    st.write("8. Please provide the following academic statistics (answers will be anonymous):")

    graduation_year = st.text_input("• Graduation Year (e.g., 2025)")
    major = st.text_input("• Major(s)")
    minor = st.text_input("• Minor(s)")
    gpa = st.text_input("• GPA")
    num_internships = st.number_input("• Quantity of previous co-ops/internships:", min_value=0, step=1)
    num_extracurriculars = st.number_input("• Quantity of extracurriculars:", min_value=0, step=1)
    num_academic_extracurriculars = st.number_input("• Quantity of academic extracurriculars:", min_value=0, step=1)
    leadership_position = st.radio(
        "• Do you hold leadership positions in these extracurriculars?",
        options=["Yes", "No"],
        horizontal=True
    )

    # Form submission
    submitted = st.form_submit_button("Submit Experience")

    if submitted:
        # Prepare data for API
        data = {
            "company_name": company_name,
            "role_name": role_name,
            "interview_date": interview_date,
            "industry": industry,
            "interview_types": interview_types,
            "difficulty_rating": difficulty_rating,
            "difficulty_elaboration": difficulty_elaboration,
            "graduation_year": graduation_year,
            "major": major,
            "minor": minor,
            "gpa": gpa,
            "num_internships": num_internships,
            "num_extracurriculars": num_extracurriculars,
            "num_academic_extracurriculars": num_academic_extracurriculars,
            "leadership_position": leadership_position,
            "student_id": "12345"  # Replace with actual logic to fetch student ID
        }

        # Define API endpoint
        api_url = "http://api:4000/e/submit_experience"  # Replace with your Flask app URL

        try:
            # Make POST request to the Flask API
            response = requests.post(api_url, json=data)

            # Check response from the server
            if response.status_code == 200:
                st.success("Thank you! Your experience has been submitted successfully.")
            else:
                st.error(f"Failed to submit experience. Error: {response.json().get('error', 'Unknown error')}")
        except Exception as e:
            st.error(f"An error occurred while submitting your experience: {str(e)}")