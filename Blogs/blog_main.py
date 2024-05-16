import streamlit as st
from . import PyTorch
from .ML_From_Scratch.knn import knn
from .PyTorch.pytorch_01 import pytorch01


def blog():
    pytorch01()
    knn()
    """
      This function defines the layout and navigation for the blog app.
      """
    # Title and description for your blog app
    st.title("My Awesome Blog App")
    st.write("A collection of insightful blogs on various topics.")

    # Display options for different blogs
    selected_blog = st.selectbox("Select a Blog", available_options=pages.get_blog_titles())

    # Call the function to display the selected blog content
    PyTorch.show_blog(selected_blog)


def get_blog_titles():
    """
  This function returns a list of titles for all available blogs.
  """
    blog_titles = ["Blog 1: Introduction to Data Science", "Blog 2: Building a Web App with Streamlit"]
    return blog_titles


def show_blog(blog_title):
    """
  This function displays the content for a specific blog based on the title.
  """
    if blog_title == "Blog 1: Introduction to Data Science":
        st.header("Blog 1: Introduction to Data Science")
        # Add content for blog 1 here (text, images, etc.)
    elif blog_title == "Blog 2: Building a Web App with Streamlit":
        st.header("Blog 2: Building a Web App with Streamlit")
        # Add content for blog 2 here
    else:
        st.write("Blog not found.")
