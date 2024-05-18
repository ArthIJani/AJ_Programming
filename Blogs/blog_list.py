import streamlit as st
import pandas as pd  # Assuming you're using pandas for data manipulation

# Sample data for tables
data1 = {'col1': ["Blog 1: KNN From Scratch"]}
df1 = pd.DataFrame(data1)


def table1():
    st.subheader("Table 1")
    st.write(df1)


def table2():
    st.subheader("Table 2")
    # st.write(df2)


def blog_list():
    """
  This function defines the layout for the app with a selection box and conditional logic.
  """
    selected_table = st.sidebar.selectbox("Select a Table", options=["Table 1", "Table 2"])

    if selected_table == "Table 1":
        table1()
    elif selected_table == "Table 2":
        table2()
    else:
        st.write("Invalid selection.")

