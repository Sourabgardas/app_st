import streamlit as st
import pandas as pd

st.title("DLR Report")
if st.session_state.authenticated:
    st.session_state.date_chosen = st.date_input("Pick a date")
    st.session_state.project = st.selectbox("Select your project", ["Select", "Ramky Odyssey", "Candeur Twins", "Candeur 40"], index=0)
    st.session_state.in_ex = st.selectbox("Select Internal/External", ["Select", "Internal", "External"], index=0)
    st.session_state.block = st.selectbox("Select your block", ["Select", "A", "B", "C", "D"], index=0)
    st.session_state.cpartner = st.selectbox("Select your channel partner name", ["Select", "Raghu", "Baa"], index=0)
    st.session_state.contractor = st.selectbox("Select your contractor", ["Select", "Nissar", "Sourab"], index=0)
    st.session_state.manpower = st.number_input("Total No.of manpower", min_value=0)
    st.session_state.work_area = st.radio("Select work area", ["Select", "floor-1", "floor-2", "floor-3"])
    if st.button("Submit"):
        df = pd.DataFrame({"date_chosen": [st.session_state.date_chosen], "project": [st.session_state.project], "in_ex": [st.session_state.in_ex], "block": [st.session_state.block], "cpartner": [st.session_state.cpartner], "contractor": [st.session_state.contractor], "manpower": [st.session_state.block], "work_area": [st.session_state.work_area]})
        st.success("Successfully submitted")
        df.to_csv("submit.csv", index=False)
            
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.success("Logged out")
        st.switch_page("app.py")  # Redirect to login page
else:
    st.error("You're not logged in!")


