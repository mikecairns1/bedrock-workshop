# 1 Open templates_app.py
# 2 import statements
import streamlit as st #all streamlit commands will be available through the "st" alias
import templates_lib as glib #reference to local lib script

# 3 Add page title config
st.set_page_config(page_title="Prompt Templates") #HTML title
st.title("Prompt Templates") #page title

# 4 Add input elements
noun = st.text_input("Noun")
adjective = st.text_input("Adjective")
verb = st.text_input("Verb")
go_button = st.button("Go", type="primary") #display a primary button

# 5 Add output elements
if go_button: #code in this if block will be run when the button is clicked
    with st.spinner("Working..."): #show a spinner while the code in this with block runs
        response_content = glib.get_text_response(noun=noun, adjective=adjective, verb=verb) #call the model through the supporting library
        st.write(response_content) #display the response content

# 6 Save file