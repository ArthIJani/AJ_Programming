import streamlit as st
from . import PyTorch  # Assuming PyTorch is a folder containing blog functions
from Blogs.PyTorch.pytorch_list import list_blogs  # Assuming pytorch_list.py defines list_blogs
from .PyTorch.pytorch_01 import pytorch01  # Assuming pytorch_01.py defines pytorch01 function
from .ML_From_Scratch.knn import knn  # Assuming knn.py defines knn function


def get_blog_titles():
    """
  This function returns a list of titles for all available blogs.
  """
    # Replace with the logic to retrieve blog titles from your file structure
    blog_titles = ["Blog 1: KNN From Scratch", "Blog 2: Pytorch Fundamentals"]
    return blog_titles


def show_blog(blog_title):
    """
  This function displays the content for a specific blog based on the title.
  """
    if blog_title == "Blog 1: KNN From Scratch":
        knn()
    elif blog_title == "Blog 2: Pytorch Fundamentals":
        pytorch01()
    else:
        st.write("Blog not found.")


def blog():
    """
      This function defines the layout and navigation for the blog app.
      """
    # Title and description for your blog app
    st.title("Machine Learning From Scratch")
    st.write("Learn about ML Algorithm in Details")

    # Assuming Streamlit version 1.0.0 or later
    selected_blog = st.selectbox("Select a Blog", options=get_blog_titles())

    # Call the function to display the selected blog content
    show_blog(selected_blog)

