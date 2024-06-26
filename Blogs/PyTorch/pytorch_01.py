import streamlit as st


def pytorch01():
    st.title("PyTorch Fundamentals")

    # st.markdown(""" # PyTorch Fundamentals
    # ![PyTorch Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/PyTorch_logo_icon.svg/45px-PyTorch_logo_icon.svg.png)""")
    st.markdown("""
    PyTorch is an open source machine learning and deep learning framework.
    """)

    st.markdown("### Importing Library")
    st.code("""
    import torch
    print(torch.__version__) #Check Version of Pytorch
    """, language="python")
    st.code("Output : 2.2.1+cu121")

    st.markdown("""### Introduction To Tensors
A Tensor is a mathematical object that can represent physical properties using multiple directions. 
Tensors are a generalization of scalars, vectors, and matrices into higher-dimensional spaces. 
They are typically grids of numbers called N-way arrays.
 """)

    st.code("""scalar = torch.tensor(7)
scalar""")
    st.code("Output : tensor(7)")
    st.code("""vector = torch.tensor([7,7])
vector""")
    st.code("Output : tensor([7, 7])")






