import streamlit as st

import Blogs.PyTorch.pytorch_01


def home():
    st.title("Welcome to AJ Programming Blogs")
    st.subheader("Welcome to your one-stop shop for insightful content!")

    # Hero image (optional)
    # Replace 'image.jpg' with your actual image path
    # st.image("image.jpg", use_column_width=True)

    # Latest blog post section
    st.header("Latest Post")

    # Replace these placeholders with your actual content
    latest_title = "**PyTorch Fundamentals**"
    latest_excerpt = "PyTorch is an open source machine learning and deep learning framework."
    latest_date = "May 19, 2024"

    # Display information with markdown
    st.markdown(f"# {latest_title}")
    st.markdown(f"{latest_excerpt}")
    st.write(f"**Published:** {latest_date}")

    # Button to link to the full post (optional)
    # Replace 'link' with the actual URL of your full post
    if st.button("Read the Full Post"):
        # Blogs.PyTorch.pytorch_01.pytorch01()
        st.write("Blogs")

    # Blog categories or tags (optional)
    st.header("Explore by Category")

    # Replace these with your actual categories/tags and links
    categories = [
        {"name": "Technology", "link": "#"},
        {"name": "Data Science", "link": "#"},
        {"name": "Life & Style", "link": "#"},
    ]

    for category in categories:
        st.markdown(f"- [{category['name']}]({category['link']})")

    # Social media links (optional)
    st.header("Connect With Us")

    # Replace these with your social media links
    social_links = [
        {"icon": "fa-brands fa-twitter", "link": "#"},
        {"icon": "fa-brands fa-facebook", "link": "#"},
        {"icon": "fa-brands fa-instagram", "link": "#"},
    ]

    for link in social_links:
        st.write(f"<i class='{link['icon']}'></i>", unsafe_allow_html=True)
        st.write(link["link"])
