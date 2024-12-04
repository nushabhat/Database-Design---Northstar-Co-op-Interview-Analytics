# Home page for students that would like to review a co-op
import logging
import os
import pandas as pd
import streamlit as st
from modules.nav import SideBarLinks
from datetime import datetime

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

    # Dictionary to store user responses
    responses = {}

    # Dynamically render survey questions
    for index, row in questions_df.iterrows():
        question = row["Question"]
        question_type = row["Type"]
        options = row["Options"]

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
        # Add a timestamp for the submission
        responses["Submission Time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save data to a CSV file
        file_path = "experience_submissions.csv"
        file_exists = os.path.exists(file_path)

        # Convert responses to a DataFrame and save it
        df = pd.DataFrame([responses])
        df.to_csv(file_path, mode='a', index=False, header=not file_exists)

        st.success("Thank you! Your experience has been submitted.")
