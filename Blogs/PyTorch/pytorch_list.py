import os
import streamlit as st


def list_blogs(folder_path):
    """
    This function lists all blogs inside a folder and displays them in a blog website format,
    using st.title for the blog title.

    Args:
        folder_path (str): Path to the folder containing blog files.
    """
    blogs = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".py") or filename.endswith(".py"):  # Adjust for your file extension
            blogs.append(filename)

    if not blogs:
        st.write("No blog posts found.")
        return

    # Display blog titles with links
    for blog in blogs:
        st.push()  # Create a new section for each blog entry
        # Assuming your blog files have an associated st.title within them
        title = st.session_state[f"blog_{blog}"]  # Access title from session state
        st.markdown(f"## [{title}](/{blog})")  # Link to individual blog post (replace / with actual path if needed)
        st.pop()  # End the section


# Example usage
# folder_path = "path/to/your/blogs"  # Replace with your actual folder path
# list_blogs(folder_path)
