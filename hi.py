import streamlit as st

def main():
    st.header("this is title")
    name = st.text_input("enter your name")

    col1, col2 = st.columns(2, gap='small')

    with col1:
        if st.button("hi", type="primary", key="btn1", width="stretch"):
            print("hi", name)

    with col2:
        if st.button("Bye", type="secondary",  key="btn2", width="stretch"):
            print("bye", name) 

    st.markdown("""
            <h1> hello world </h1> 
            <style>
                button{
                    background:orange !important ;
                }
                    </style> 
    """, unsafe_allow_html=True) # know we can run the HTML code here  
main()