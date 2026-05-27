import streamlit as st


def footer_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content: cenetr; items-align:center">
                <p style="font-weight:bold; color:white;"> © 2026 Snap Class | Built by Praveena Pawar | Powered by Streamlit </p>
        </div>
                

            """, unsafe_allow_html=True)
    



def footer_dashbord():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content: cenetr; items-align:center">
                <p style="font-weight:bold; color:black;"> © 2026 Snap Class | Built by Praveena Pawar | Powered by Streamlit </p>
        </div>
                

            """, unsafe_allow_html=True)