import streamlit as st

from Blogs.blog_list import blog_list

st.set_page_config(
    page_title="Attendance System",
    page_icon=":code:",
    layout="wide"
)


from Blogs.blog_main import blog
from navigation import create_navigation_bar

tailwind_cdn = "https://cdn.tailwindcss.com"
st.write(f'<script src="{tailwind_cdn}">', unsafe_allow_html=True)

# Navigation bar
selected_page = create_navigation_bar()

try:
    if selected_page == "Home":
        pass
    elif selected_page == "Blogs":
        blog_list()
    elif selected_page == "Contact Us":
        pass
    else:
        st.error(f"Invalid page selection: {selected_page}")
except Exception as e:
    # Handle errors during content display
    st.error(f"An error occurred: {e}")
