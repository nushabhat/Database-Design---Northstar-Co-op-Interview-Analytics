import logging
logger = logging.getLogger(__name__)
import sqlite3
import pandas as pd
import streamlit as st
from modules.nav import SideBarLinks

# Set page configuration
st.set_page_config(layout="wide")

# Sidebar navigation
SideBarLinks()

# Title for Users Management Page
st.title("User Management")

# Function to connect to the SQLite database and retrieve user data
def get_users_data():
    db_path = "database-files/northstar.sql"  # Path to the SQLite database file

    # Connect to the database
    conn = sqlite3.connect(db_path)
    query = "SELECT user_id, username, email, role, date_joined FROM users"  # Adjust table/column names
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Fetch users data
try:
    users_df = get_users_data()

    # Display the users' information
    st.subheader("All Users")
    st.dataframe(users_df, use_container_width=True)

    # Option to display user details or perform admin actions
    st.subheader("User Actions")

    selected_user = st.selectbox("Select a user to view details or perform actions:", users_df["username"])

    # Display selected user's details
    user_details = users_df[users_df["username"] == selected_user].iloc[0]
    st.write(f"**User ID:** {user_details['user_id']}")
    st.write(f"**Email:** {user_details['email']}")
    st.write(f"**Role:** {user_details['role']}")
    st.write(f"**Date Joined:** {user_details['date_joined']}")

    # Admin actions
    st.subheader("Admin Actions")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button(f"Delete {selected_user}"):
            st.warning(f"User {selected_user} has been deleted. (Simulated)")
            # Add code to delete user from the database

    with col2:
        if st.button(f"Edit {selected_user}"):
            st.info(f"Editing {selected_user}. (Simulated)")
            # Add code to edit user details

    with col3:
        if st.button(f"Reset Password for {selected_user}"):
            st.success(f"Password for {selected_user} has been reset. (Simulated)")
            # Add code to reset the user's password

except Exception as e:
    st.error(f"Error fetching user data: {e}")

# Go Back Button
if st.button("⬅️ Go Back", type='secondary'):
    st.switch_page("System_Admin_Home")
