import streamlit as st


st.set_page_config(
    page_title="AJ Programming",
    page_icon=":code:",
    layout="wide"
)

from home import home
from Blogs.blog_main import blog
from navigation import create_navigation_bar
from contact_us import display_contact_us
from style.style import apply_local_css


# tailwind_cdn = "https://cdn.tailwindcss.com"
# st.write(f'<script src="{tailwind_cdn}">', unsafe_allow_html=True)

# Navigation bar
selected_page = create_navigation_bar()

try:
    if selected_page == "Home":
        home()
    elif selected_page == "Blogs":
        blog()
    elif selected_page == "Contact Us":
        display_contact_us()
    else:
        st.error(f"Invalid page selection: {selected_page}")
except Exception as e:
    # Handle errors during content display
    st.error(f"An error occurred: {e}")


# Apply local CSS for styling (optional)
apply_local_css("style/style.css")
