import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('App Administration Page')

# Function to fetch the student list
def fetch_students():
    try:
        # API endpoint for getting the student list
        api_url = "http://api:4000/s/get_students"
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()  # Return the list of students
        else:
            st.error(f"Failed to fetch students: {response.status_code}")
            return []
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return []

# Button to fetch and display the list of students
if st.button("Show All Students"):
    students = fetch_students()
    
    if students:
        # Display the student list in a table format
        st.write("### List of Students")
        st.table(students)  # Use Streamlit's table widget
    else:
        st.warning("No students found or unable to fetch data.")

st.write('\n\n')
# Prompt admin for input
st.header("Delete a Student")
username = st.text_input("Enter the student's username:")
student_id = st.text_input("Enter the student's ID:")

# Button to trigger deletion
if st.button("Delete Student"):
    if username and student_id:
        # Send DELETE request to the API
        api_url = "http://api:4000/a/delete_student"
        payload = {'username': username, 'id': student_id}
        
        try:
            # Send request
            response = requests.delete(api_url, json=payload)
            
            # Check the response status
            if response.status_code == 200:
                st.success(response.json().get('message', 'Student deleted successfully!'))
            elif response.status_code == 404:
                st.error(response.json().get('error', 'Student not found.'))
            elif response.status_code == 400:
                st.warning(response.json().get('error', 'Invalid input.'))
            else:
                st.error(f"Error: {response.status_code}. {response.text}")
        
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter both username and ID.")