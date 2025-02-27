import streamlit as st

# Set page title
st.title("Login!")

# Initialize session state for authentication
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Dummy credentials (for demo purposes)
USER_CREDENTIALS = {"admin": "password123"}
username = st.text_input("Username", key="username")
password = st.text_input("Password", type="password", key="password")
# Login form
if not st.session_state.authenticated:
    #print(username, password)
    login_button = st.button("Login")

    if login_button:
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            #print('success')
            st.session_state.authenticated = True
            st.success("Login successful! 🎉")
            st.switch_page("pages/home.py")
            #st.rerun()
        else:
            st.error("Invalid username or password. Try again!")

# Show content after login
#if st.session_state.authenticated:
#    st.subheader(f"Welcome, {username}! 🎉")
#    st.write("You have successfully logged in.")
#    if st.button("Logout"):
#        st.session_state.authenticated = False
#        st.rerun()
