# 1 Open streaming_app.py
# 2 import statements
import streaming_lib as glib  # reference to local lib script
import streamlit as st
from langchain.callbacks import StreamlitCallbackHandler

# 3 Add page title, config, and two column layout

st.set_page_config(page_title="Response Streaming")  # HTML title
st.title("Response Streaming")  # page title

# 4 Add input elements

input_text = st.text_area("Input text", label_visibility="collapsed")
go_button = st.button("Go", type="primary")  # display a primary button

# 5 Add output elements

if go_button:  # code in this if block will be run when the button is clicked
    #use an empty container for streaming output
    st_callback = StreamlitCallbackHandler(st.container())
    streaming_response = glib.get_streaming_response(prompt=input_text, streaming_callback=st_callback)

# 6 Save the file
