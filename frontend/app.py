import streamlit as st
import requests

st.title("Summarisation Assistant")

option = st.selectbox(
    "Would you like to paste a url or directly paste text",
    ("Link", "Text")
)

url_input=""
text_input=""

if option == "Link":
    url_input=st.text_input("Enter the URL please")
elif option == "Text":
    text_input=st.text_area("Paste/Type the text here please")


if st.button('Summarise Please!'):
    with st.spinner(":brain: Thinking"):
        response = requests.post("http://localhost:8000/api/summarise", json={"url":url_input, "text":text_input})
        
        if response.status_code == 200:
            summary = response.json().get("summary","")
            if summary == "":
                st.error("Error encountered!")
            st.write(summary)
        else:
            st.error("Error encountered!")
