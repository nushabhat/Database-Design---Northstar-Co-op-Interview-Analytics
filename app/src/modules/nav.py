# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st


#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")


def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")

#### ------------------------ log out ------------------------
# Example: if you had a button, ensure it's unique with a key
def LogOut():
    if st.sidebar.button("Logout", key="advisor_logout_button"):
        # Your logout logic here
        pass


#### ------------------------ Co-op Advisor ------------------------
def AdvisorNav():
    st.sidebar.page_link("pages/01_Advisor_Statistics_Table.py", label = "Advisor Table", icon = "👨‍💻")
    st.sidebar.page_link("pages/01_Advisor_Scatter.py", label = "Scatterplot", icon = "📈")
    st.sidebar.page_link("pages/01_Advisor_Histogram.py", label = "Histogram", icon = "📶")


#### ------------------------ Student Searching ------------------------
def SearchStudentNav():
    st.sidebar.page_link("pages/00_Co-op_Student_Home.py", label = "Student Searching Page", icon = "👀")
def CoopList(): 
    st.sidebar.page_link("pages/03_Co-op_List.py", label = "Co-op List", icon = "👀")
def CoopDetails():  
    st.sidebar.page_link("pages/04_Co-op_Details.py", label = "Co-op Details", icon = "👀")
    

#### ------------------------ Student Reviewing ------------------------
def ReviewStudentNav():
    # Link to the student reviewing page
    st.sidebar.page_link("pages/02_Student_Reviewing_Home.py", label="Student Reviewing Page", icon="✍🏻")
    


#### ------------------------ System Admin Role ------------------------
def AdminPageNav():
    st.sidebar.page_link("pages/20_Admin_Home.py", label="System Admin", icon="🖥️")
def DeleteStudent():
    st.sidebar.page_link("pages/21_delete_student.py", label="Delete Users", icon="🖥️")
def ManageSurvey():
    st.sidebar.page_link("pages/22_Survey_Questions_Mgmt.py", label="Manage Survey Questions", icon="📋")
def ManageUsers():
    st.sidebar.page_link("pages/23_Admin_Users_Mgmt.py", label="Manage Users", icon="📋")

# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
    """

    # add a logo to the sidebar always
    st.sidebar.image("assets/logo.png", width=150)

    # If there is no logged in user, redirect to the Home (Landing) page
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")

    if show_home:
        # Show the Home page link (the landing page)
        HomeNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        if st.session_state["role"] == "co-op_student":
            ReviewStudentNav()
            SearchStudentNav()
            CoopList()
            CoopDetails()

        if st.session_state["role"] == "co-op_advisor":
            AdvisorNav()

        if st.session_state["role"] == "administrator":
            AdminPageNav()
            DeleteStudent()
            ManageSurvey()
            ManageUsers()
            

        if st.session_state["role"] == "student_reviewing":
            ReviewStudentNav()
            SearchStudentNav()
            CoopList()
            CoopDetails()


    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py")
