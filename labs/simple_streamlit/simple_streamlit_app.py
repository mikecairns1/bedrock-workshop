# 1 Open simple_streamlit_app.py
# 2 Import statements
import streamlit as st #all streamlit commands will be available through the "st" alias

# 3 Add page title and config
st.set_page_config(page_title="Streamlit Demo") #HTML title
st.title("Streamlit Demo") #page title

# 4 Add input elements
color_text = st.text_input("What's your favorite color?") #display a text box
go_button = st.button("Go", type="primary") #display a primary button

# 5 Add the output elements
if go_button: #code in this if block will be run when the button is clicked

    st.write(f"I like {color_text} too!") #display the response content

# 6 Save the file