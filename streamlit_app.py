import streamlit as st

# Define the pages
main_page = st.Page("main_page.py", title="Main Page", icon="👋")
page_2 = st.Page("setup_intro.py", title="Setting up streamlit", icon="⚙️")
page_3 = st.Page("data_viz.py", title="How to Data", icon="📊")

# Set up navigation
pg = st.navigation([main_page, page_2, page_3])

# Run the selected page
pg.run()