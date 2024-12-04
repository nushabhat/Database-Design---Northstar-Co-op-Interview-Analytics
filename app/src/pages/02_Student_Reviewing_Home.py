# Home page for students that would like to review a co-op
import logging
import os
import pandas as pd
import streamlit as st
import requests
from modules.nav import SideBarLinks
from datetime import datetime

SideBarLinks()

# Navigation to the experience submission page from another page
# Logging setup
logger = logging.getLogger(__name__)

# Set up navigation
SideBarLinks()

# Title for the experience submission page
st.title("Experience Submission")

# Load survey questions from CSV
questions_file = "survey_questions.csv"
if os.path.exists(questions_file):
    questions_df = pd.read_csv(questions_file)
else:
    st.error("Survey questions file not found.")
    st.stop()

# Form for experience submission
with st.form("experience_form"):
    st.header("Experience Submission")
    # Collecting Company Information
    company_name = st.text_input("1. Company Name")
    role_name = st.text_input("2. Role Name")
    interview_date = st.text_input("3. Month/Year of Interview (e.g., Oct 2024)")
    industry = st.text_input("4. Company Industry")

    # Dictionary to store user responses
    responses = {}

    # Dynamically render survey questions
    for index, row in questions_df.iterrows():
        question = row["Question"]
        question_type = row["Type"]
        options = row["Options"]

   # Difficulty rating
    st.write("6. How difficult would you rate this interview?")

    # Mapping the options to decimal values
    difficulty_rating = st.radio(
        "",
        options=[1.0, 2.0, 3.0, 4.0, 5.0],  # Use decimal values instead of emojis
        index=2,  # Default to middle value (3.0)
        format_func=lambda x: f"{x}"  # Option label with value and description
    )
        # Render input fields based on the question type
        if question_type == "text":
            responses[question] = st.text_input(f"{index + 1}. {question}")
        elif question_type == "number":
            responses[question] = st.number_input(f"{index + 1}. {question}", min_value=0, step=1)
        elif question_type == "multiselect":
            options_list = options.split(",") if options else []
            responses[question] = st.multiselect(f"{index + 1}. {question}", options=options_list)
        elif question_type == "radio":
            options_list = options.split(",") if options else []
            responses[question] = st.radio(f"{index + 1}. {question}", options=options_list, horizontal=True)

    # Form submission button
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
        # Add a timestamp for the submission
        responses["Submission Time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save data to a CSV file
        file_path = "experience_submissions.csv"
        file_exists = os.path.exists(file_path)

        # Convert responses to a DataFrame and save it
        df = pd.DataFrame([responses])
        df.to_csv(file_path, mode='a', index=False, header=not file_exists)

            # Check response from the server
            if response.status_code == 200:
                st.success("Thank you! Your experience has been submitted successfully.")
            else:
                st.error(f"Failed to submit experience. Error: {response.json().get('error', 'Unknown error')}")
        except Exception as e:
            st.error(f"An error occurred while submitting your experience: {str(e)}")