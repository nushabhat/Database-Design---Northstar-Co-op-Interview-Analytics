import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# About this App")

st.markdown (
    """
    This is our app for CS 3200 Course Project.  

    NorthStar Technologies is a data-driven app designed to empower students by simplifying and enhancing the interview preparation process for co-op roles. This platform collects detailed, student-submitted insights on interview experiences, covering factors like interview difficulty, types of technical questions, behavioral topics, number of rounds, etc.. By gathering this information from students who have previously completed interviews, Northstar provides an accessible, centralized source of valuable information, sparing students the need to rely solely on networking to understand what to expect in their interview process. The statistics provided by NorthStar will also act as a guide for University Student Advisors looking to aid their students on their co-op journey by identifying relevant positions with preparatory advice intertwined.
    With Northstar’s interactive ratings and reviews, students can anonymously connect with peers who are preparing for similar roles, using a chat system to exchange tips and insights specific to their field or industry. The platform also features tailored filters, allowing users to easily search and sort posts by co-op type, company, and industry, simplifying their search process. By offering real-time community support and streamlined access to relevant information, Northstar helps students approach their co-op interviews confidently and clearly.


    Project Name: Northstar Technologies
    Team Name: The BigDippas
    Team Members: Quillian Alewine, Sarah Cooper, San Yan, Nusha Bhat, Lucia Yaniz 

    """
        )
