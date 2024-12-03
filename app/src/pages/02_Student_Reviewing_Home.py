# home page for students that would like to review a co-op
import logging
logger = logging.getLogger(__name__)

import streamlit as st
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
    difficulty_rating = st.radio(
        "",
        options=["😞", "😐", "😊"],
        index=1,
        horizontal=True
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
        # Saving data to a CSV file
        data = {
            "Company Name": company_name,
            "Role Name": role_name,
            "Interview Date": interview_date,
            "Industry": industry,
            "Interview Types": ", ".join(interview_types),
            "Difficulty Rating": difficulty_rating,
            "Difficulty Elaboration": difficulty_elaboration,
            "Graduation Year": graduation_year,
            "Major": major,
            "Minor": minor,
            "GPA": gpa,
            "Previous Internships": num_internships,
            "Extracurriculars": num_extracurriculars,
            "Academic Extracurriculars": num_academic_extracurriculars,
            "Leadership Position": leadership_position,
            "Submission Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        # Append to CSV file if exists, otherwise create it
        file_path = "experience_submissions.csv"
        file_exists = os.path.exists(file_path)

        df = pd.DataFrame([data])
        df.to_csv(file_path, mode='a', index=False, header=not file_exists)

        st.success("Thank you! Your experience has been submitted.")
