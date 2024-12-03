import logging
import os
import pandas as pd
import streamlit as st
from modules.nav import SideBarLinks

# Logging setup
logger = logging.getLogger(__name__)

# Set page configuration
st.set_page_config(layout='wide')

# Sidebar navigation
SideBarLinks()

# Title for System Admin Home Page
st.title('System Admin Home Page')

# Button to navigate to ML Model Management page
if st.button('Update ML Models', type='primary', use_container_width=True):
    st.switch_page('pages/21_ML_Model_Mgmt.py')

# File to store survey questions
questions_file = "survey_questions.csv"

# Load existing questions if the file exists, else initialize an empty DataFrame
if os.path.exists(questions_file):
    questions_df = pd.read_csv(questions_file)
else:
    questions_df = pd.DataFrame(columns=["Question", "Type", "Options"])

# Title for the Survey Admin Panel
st.title("Survey Admin Panel - Manage Survey Questions")

# Display existing survey questions
st.subheader("Existing Survey Questions")
if questions_df.empty:
    st.write("No questions available.")
else:
    for index, row in questions_df.iterrows():
        st.write(f"**{index + 1}. {row['Question']}**")
        st.write(f"**Type:** {row['Type']}")
        if row["Type"] in ["multiselect", "radio"]:
            st.write(f"**Options:** {row['Options']}")

        # Edit and Delete buttons side by side
        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"Edit Question {index + 1}", key=f"edit_{index}"):
                st.session_state["edit_index"] = index
        with col2:
            if st.button(f"Delete Question {index + 1}", key=f"delete_{index}"):
                questions_df.drop(index, inplace=True)
                questions_df.reset_index(drop=True, inplace=True)
                questions_df.to_csv(questions_file, index=False)
                st.experimental_rerun()

# Adding or Editing Questions
st.subheader("Add or Edit Survey Question")

# If editing, load the current question data, else initialize empty fields
if "edit_index" in st.session_state:
    edit_index = st.session_state["edit_index"]
    current_question = questions_df.loc[edit_index, "Question"]
    current_type = questions_df.loc[edit_index, "Type"]
    current_options = questions_df.loc[edit_index, "Options"]
else:
    edit_index = None
    current_question = ""
    current_type = "text"
    current_options = ""

# Input fields for question, type, and options
question = st.text_input("Question", value=current_question)
question_type = st.selectbox(
    "Question Type",
    options=["text", "number", "multiselect", "radio"],
    index=["text", "number", "multiselect", "radio"].index(current_type)
)

# Show options input only if type is multiselect or radio
options = ""
if question_type in ["multiselect", "radio"]:
    options = st.text_area(
        "Options (comma-separated)",
        value=current_options,
        placeholder="Option 1, Option 2, Option 3"
    )

# Save or Update button for questions
if st.button("Save Question"):
    if question_type in ["multiselect", "radio"] and not options:
        st.error("Please provide options for multiselect or radio questions.")
    else:
        # Prepare new question data
        new_question = {
            "Question": question,
            "Type": question_type,
            "Options": options.strip() if options else ""
        }

        # Save or update the question
        if edit_index is not None:
            questions_df.loc[edit_index] = new_question
            del st.session_state["edit_index"]
        else:
            questions_df = pd.concat([questions_df, pd.DataFrame([new_question])], ignore_index=True)

        # Save to CSV and reload
        questions_df.to_csv(questions_file, index=False)
        st.success("Question saved successfully.")
        st.experimental_rerun()

# Clear Edit State button (Optional)
if "edit_index" in st.session_state:
    if st.button("Cancel Edit"):
        del st.session_state["edit_index"]
        st.experimental_rerun()
