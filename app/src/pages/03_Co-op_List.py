
#Should include a list of co-ops based on the searched tags

import streamlit as st
import pandas as pd
import os

st.title("Co-op List")

# load experience submissions data
file_path = "experience_submissions.csv"

# filters for coop search
st.sidebar.header("Search Filters")

# search by tags/keywords
tags = st.sidebar.multiselect(
    options=data.columns
)

search_keyword = st.sidebar.text_input(
    "Enter a keyword to filter results (optional)"
)

# show results
if tags:
    filtered_data = data.copy()

    for tag in tags:
        filter_values = st.sidebar.multiselect(f"Filter by {tag}", options=filtered_data[tag].unique())
        if filter_values:
            filtered_data = filtered_data[filtered_data[tag].isin(filter_values)]

    if search_keyword:
        filtered_data = filtered_data[
            filtered_data.apply(lambda row: search_keyword.lower() in row.astype(str).str.lower().to_string(), axis=1)
        ]

    st.write(f"### Matching Co-op Experiences ({len(filtered_data)} results)")
    st.dataframe(filtered_data)
else:
    st.write("### All Co-op Experiences")
    st.dataframe(data)
