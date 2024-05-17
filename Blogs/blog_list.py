import streamlit as st
import pandas as pd  # Assuming you're using pandas for data manipulation

# Sample data for tables
data1 = {'col1': [1, 2, 3], 'col2': ['A', 'B', 'C']}
data2 = {'col3': [4, 5, 6], 'col4': ['D', 'E', 'F']}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)


def table1():
    st.subheader("Table 1")
    st.write(df1)


def table2():
    st.subheader("Table 2")
    st.write(df2)


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

