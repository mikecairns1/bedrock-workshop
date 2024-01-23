# 1 Open image_appy.py
# 2 Add the import statements
import streamlit as st #all streamlit commands will be available through the "st" alias
import image_lib as glib #reference to local lib script

# 3 Add the page title config and column layout
st.set_page_config(layout="wide", page_title="Image Generation") #set the page width wider to accommodate columns

st.title("Image Generation") #page title

col1, col2 = st.columns(2) #create 2 columns

# 4 Add the input elements

with col1: #everything in this with block will be placed in column 1
    st.subheader("Image generation prompt") #subhead for this column
    
    prompt_text = st.text_area("Prompt text", height=200, label_visibility="collapsed") #display a multiline text box with no label
    
    process_button = st.button("Run", type="primary") #display a primary button

# 5 Add the output elements
with col2: #everything in this with block will be placed in column 2
    st.subheader("Result") #subhead for this column
    
    if process_button: #code in this if block will be run when the button is clicked
        with st.spinner("Drawing..."): #show a spinner while the code in this with block runs
            generated_image = glib.get_image_response(prompt_content=prompt_text) #call the model through the supporting library
        
        st.image(generated_image) #display the generated image


# 6 Save the file