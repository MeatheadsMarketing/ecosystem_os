
import streamlit as st
from zip_ingestor_engine import process_zip

def render():
    st.title("📦 Ecosystem Zip Ingestor")
    uploaded_zip = st.file_uploader("Upload a .zip file to inject into ecosystem_os", type="zip")
    if uploaded_zip:
        with open("temp_uploaded.zip", "wb") as f:
            f.write(uploaded_zip.read())
        result = process_zip("temp_uploaded.zip")
        st.success("Injection Complete")
        st.json(result)
