import logging
import pandas as pd
import streamlit as st
import requests
from modules.nav import SideBarLinks

# Set up the page configuration
st.set_page_config(layout="wide")

# Sidebar navigation
SideBarLinks()

# Title for Users Management Page
st.title("User Management")

# Function to fetch all student data from the API
def get_students_data():
    api_url = "http://api:4000/a/get_all_students"  # API endpoint
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return pd.DataFrame(response.json())  # Convert JSON data to a pandas DataFrame
        else:
            st.error(f"Failed to fetch data: {response.status_code}")
            return pd.DataFrame()  # Return empty DataFrame if the API call fails
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame()  # Return empty DataFrame on error
    
def edit_student(student_id, updates):
    try:
        response = requests.put("http://api:4000/a/edit_student", json={"id": int(student_id), **updates})
        
        #st.write("Request sent to API:", {"id": student_id, **updates})  # Debugging: log request data
        #st.write("API Response:", response.status_code, response.text)  # Debugging: log API response
        if response.status_code == 200:
            st.success("Student information updated successfully!")
        else:
            st.error(f"Failed to update student: {response.json().get('error', 'Unknown error')}")
    except Exception as e:
        st.error(f"Error updating student: {e}")

# Fetch students data
try:
    students_df = get_students_data()

    if not students_df.empty:
        # Display the students' information
        st.subheader("All Students")
        st.dataframe(students_df, use_container_width=True)

        # Option to display student details or perform admin actions
        st.subheader("Student Actions")

        selected_student = st.selectbox("Select a student to view details or perform actions:", students_df["UserName"])

        # Display selected student's details
        student_details = students_df[students_df["UserName"] == selected_student].iloc[0]
        st.write(f"**Student ID:** {student_details['ID']}")
        st.write(f"**Graduation Year:** {student_details['GraduationYear']}")
        st.write(f"**Major:** {student_details['Major']}")
        st.write(f"**Minor:** {student_details['Minor']}")
        st.write(f"**Email Address:** {student_details['EmailAddress']}")
        st.write(f"**Number of Previous Co-ops:** {student_details['NumPreviousCoops']}")
        st.write(f"**GPA:** {student_details['GPA']}")
        st.write(f"**Advisor ID:** {student_details['AdvisorID']}")


    else:
        st.warning("No students found.")

except Exception as e:
    st.error(f"Error fetching student data: {e}")

# Admin actions
st.subheader("Admin Actions")
col1 = st.columns(1)[0]


# Ensure session state variables are initialized
if "editing_student" not in st.session_state:
    st.session_state.editing_student = False
if "updated_values" not in st.session_state:
    st.session_state.updated_values = {}
if "student_data" not in st.session_state:
    st.session_state.student_data = {}

# Admin actions
with col1:
    # Start editing when the Edit button is pressed
    if st.button(f"Edit {selected_student}"):
        st.session_state.editing_student = True
        st.info(f"Editing {selected_student}")

    # If editing mode is active, show the input fields
    if st.session_state.editing_student:
        st.write("### Update Student Information")

        # Loop over fields and pre-fill them
        for field in ['GraduationYear', 'Major', 'Minor', 'EmailAddress', 'NumPreviousCoops', 'GPA', 'AdvisorID']:
            input_key = f"{field}_{selected_student}"  # Unique key for each input

            # Initialize the field in session state if not already set
            if input_key not in st.session_state:
                st.session_state[input_key] = str(student_details[field])

            # Create input fields and track changes
            st.session_state[input_key] = st.text_input(
                f"Update {field}:", value=st.session_state[input_key]
            )

        # Save changes button
    if st.button("Save Changes"):
            # Collect updated values, ensuring serialization
            updated_values = {
                field: int(st.session_state[f"{field}_{selected_student}"]) if field in ['GraduationYear', 'NumPreviousCoops', 'AdvisorID']
                else float(st.session_state[f"{field}_{selected_student}"]) if field == 'GPA'
                else st.session_state[f"{field}_{selected_student}"]
                for field in ['GraduationYear', 'Major', 'Minor', 'EmailAddress', 'NumPreviousCoops', 'GPA', 'AdvisorID']
                if st.session_state[f"{field}_{selected_student}"] != str(student_details[field])
            }

            if updated_values:
                try:
                    # Call the function to save updated values
                    edit_student(student_details['ID'], updated_values)
                    st.success("Changes saved successfully.")

                    # Update session state with new values
                    st.session_state.student_data.update(updated_values)
                    st.session_state.editing_student = False  # Exit editing mode
                except Exception as e:
                    st.error(f"Error saving changes: {e}")
                    print(f"Error saving changes: {e}", flush=True)
            else:
                st.warning("No changes made.")


# Go Back Button
if st.button("⬅️ Go Back", type='secondary'):
    st.switch_page("/appcode/pages/20_Admin_Home.py")
