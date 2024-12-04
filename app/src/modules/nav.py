# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st


#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")


def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")


#### ------------------------ Co-op Advisor ------------------------
def AdvisorNav(): 
    st.sidebar.page_link("pages/01_Co-op_Advisor_Home.py", label = "Advisory Page", icon = "👩‍💼")


#### ------------------------ Student Searching ------------------------
def SearchStudentNav():
    st.sidebar.page_link("pages/00_Co-op_Student_Home.py", label = "Student Searching Page", icon = "👀")

#### ------------------------ Student Reviewing ------------------------
def ReviewStudentNav():
    st.sidebar.page_link("pages/02_Student_Reviewing_Home.py", label = "Student Reviewing Page", icon = "✍🏻")

#### ------------------------ Examples for Role of pol_strat_advisor ------------------------
def PolStratAdvHomeNav():
    st.sidebar.page_link(
        "pages/00_Pol_Strat_Home.py", label="Political Strategist Home", icon="👤"
    )


def WorldBankVizNav():
    st.sidebar.page_link(
        "pages/01_World_Bank_Viz.py", label="World Bank Visualization", icon="🏦"
    )


def MapDemoNav():
    st.sidebar.page_link("pages/02_Map_Demo.py", label="Map Demonstration", icon="🗺️")


## ------------------------ Examples for Role of usaid_worker ------------------------
def ApiTestNav():
    st.sidebar.page_link("pages/12_API_Test.py", label="Test the API", icon="🛜")


def PredictionNav():
    st.sidebar.page_link(
        "pages/11_Prediction.py", label="Regression Prediction", icon="📈"
    )


def ClassificationNav():
    st.sidebar.page_link(
        "pages/13_Classification.py", label="Classification Demo", icon="🌺"
    )


#### ------------------------ System Admin Role ------------------------
def AdminPageNav():
    st.sidebar.page_link("pages/20_Admin_Home.py", label="System Admin", icon="🖥️")
    st.sidebar.page_link(
        "pages/21_ML_Model_Mgmt.py", label="ML Model Management", icon="🏢"
    )


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
            # PolStratAdvHomeNav()
            # WorldBankVizNav()
            # MapDemoNav()
            AdvisorNav()
            ReviewStudentNav()
            AdminPageNav()
            HomeNav()

        if st.session_state["role"] == "co-op_advisor":
            # PredictionNav()
            # ApiTestNav()
            # ClassificationNav()
            SearchStudentNav()
            ReviewStudentNav()
            AdminPageNav()
            HomeNav()


        if st.session_state["role"] == "administrator":
            SearchStudentNav()
            

        if st.session_state["role"] == "student_reviewing":
            AdminPageNav()
            # TO-DO: 
            # add student reviewing pages here

    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py")
